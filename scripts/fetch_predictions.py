#!/usr/bin/env python3
"""
ボクシング予想発言の自動抽出パイプライン
========================================
使い方:
  python fetch_predictions.py <YouTube URL> [--event "井上尚弥 vs 中谷潤人"] [--speakers "竹原慎二,畑山隆則,渡嘉敷勝男"]

必要なもの:
  pip install yt-dlp anthropic

処理の流れ:
  1. yt-dlp で自動字幕（日本語）をダウンロード
  2. 字幕テキストをClaude Sonnetに渡して話者分離・予想抽出
  3. standard-log-v1.2-json 形式の statements[] を出力

環境変数:
  ANTHROPIC_API_KEY: Anthropic APIキー
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# ── 定数 ──────────────────────────────────────────
KNOWN_CHANNELS = {
    "ぶっちゃけチャンネル": ["渡嘉敷勝男", "竹原慎二", "畑山隆則"],
    "KOD LAB": ["内山高志"],
    "内山高志KOチャンネル": ["内山高志"],
    "前向き教室": ["細川バレンタイン"],
    "細川バレンタイン": ["細川バレンタイン"],
    "具志堅用高のネクストチャレンジ": ["具志堅用高"],
    "飯田覚士ボクシング塾": ["飯田覚士"],
    "和氣慎吾": ["和氣慎吾"],
    "リーゼントチャンネル": ["和氣慎吾"],
}

SPEAKER_DB = {
    "渡嘉敷勝男": {"role": "boxer", "affiliation": "元WBA世界ライトフライ級王者"},
    "竹原慎二": {"role": "boxer", "affiliation": "元WBA世界ミドル級王者"},
    "畑山隆則": {"role": "boxer", "affiliation": "元WBA世界スーパーフェザー級・ライト級2階級制覇王者"},
    "内山高志": {"role": "boxer", "affiliation": "元WBA世界スーパーフェザー級王者"},
    "細川バレンタイン": {"role": "youtuber", "affiliation": "元日本スーパーライト級王者"},
    "具志堅用高": {"role": "boxer", "affiliation": "元WBA世界ライトフライ級王者"},
    "山中慎介": {"role": "commentator", "affiliation": "元WBC世界バンタム級王者"},
    "亀田大毅": {"role": "boxer", "affiliation": "元WBA世界フライ級・IBF世界スーパーフライ級王者"},
    "京口紘人": {"role": "boxer", "affiliation": "元世界2階級制覇王者"},
    "長谷川穂積": {"role": "commentator", "affiliation": "元世界3階級制覇王者"},
    "飯田覚士": {"role": "boxer", "affiliation": "元WBA世界スーパーフライ級王者"},
    "和氣慎吾": {"role": "commentator", "affiliation": "Wake Riseボクシングジム"},
}


def get_subtitles(url: str, lang: str = "ja") -> tuple[str, dict]:
    """yt-dlp で自動字幕を取得。(字幕テキスト, 動画メタデータ) を返す"""

    with tempfile.TemporaryDirectory() as tmpdir:
        # まずメタデータ取得
        meta_cmd = [
            "yt-dlp", "--dump-json", "--no-download", url
        ]
        print(f"[1/3] メタデータ取得中... ", end="", flush=True)
        result = subprocess.run(meta_cmd, capture_output=True, text=True, timeout=60)
        if result.returncode != 0:
            print(f"失敗")
            print(f"  エラー: {result.stderr[:200]}")
            sys.exit(1)
        meta = json.loads(result.stdout)
        print(f"OK: {meta.get('title', '?')[:60]}")

        # 字幕取得
        sub_path = os.path.join(tmpdir, "sub")
        sub_cmd = [
            "yt-dlp",
            "--write-auto-sub",
            "--sub-lang", lang,
            "--sub-format", "vtt",
            "--skip-download",
            "-o", sub_path,
            url
        ]
        print(f"[2/3] 自動字幕ダウンロード中... ", end="", flush=True)
        result = subprocess.run(sub_cmd, capture_output=True, text=True, timeout=120)

        # 字幕ファイルを探す
        vtt_files = list(Path(tmpdir).glob("*.vtt"))
        if not vtt_files:
            # 日本語字幕がない場合、言語指定なしで再試行
            sub_cmd[sub_cmd.index("--sub-lang") + 1] = f"{lang},{lang}-orig"
            subprocess.run(sub_cmd, capture_output=True, text=True, timeout=120)
            vtt_files = list(Path(tmpdir).glob("*.vtt"))

        if not vtt_files:
            print("失敗（自動字幕なし）")
            print("  この動画には自動字幕が利用できません。")
            sys.exit(1)

        vtt_text = vtt_files[0].read_text(encoding="utf-8")
        print(f"OK ({len(vtt_text)} chars)")

        # VTTをプレーンテキストに変換
        plain = vtt_to_plain(vtt_text)
        print(f"  プレーンテキスト: {len(plain)} chars")

        return plain, meta


def vtt_to_plain(vtt: str) -> str:
    """VTT字幕をプレーンテキストに変換（重複行を除去）"""
    lines = []
    seen = set()
    for line in vtt.split("\n"):
        # タイムスタンプ行やヘッダを除去
        if re.match(r"^\d{2}:\d{2}", line):
            continue
        if line.startswith("WEBVTT") or line.startswith("Kind:") or line.startswith("Language:"):
            continue
        if "-->" in line:
            continue
        # HTMLタグ除去
        clean = re.sub(r"<[^>]+>", "", line).strip()
        if not clean:
            continue
        # 重複除去（VTT自動字幕は同じ行が繰り返される）
        if clean not in seen:
            seen.add(clean)
            lines.append(clean)

    return "\n".join(lines)


def guess_speakers_from_meta(meta: dict) -> list[str]:
    """動画メタデータからスピーカーを推定"""
    title = meta.get("title", "")
    description = meta.get("description", "")
    channel = meta.get("channel", "")
    uploader = meta.get("uploader", "")

    speakers = set()

    # チャンネル名から推定
    for ch_key, ch_speakers in KNOWN_CHANNELS.items():
        if ch_key in channel or ch_key in uploader or ch_key in title:
            speakers.update(ch_speakers)

    # タイトル・概要欄からスピーカーDB内の名前を検索
    text = title + " " + description
    for name in SPEAKER_DB:
        if name in text:
            speakers.add(name)

    return list(speakers)


def extract_with_claude(subtitle_text: str, meta: dict, event_name: str,
                         speakers_hint: list[str], url: str) -> list[dict]:
    """Claude Sonnet API で話者分離・予想抽出"""
    try:
        import anthropic
    except ImportError:
        print("エラー: anthropic パッケージが必要です。 pip install anthropic")
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("エラー: 環境変数 ANTHROPIC_API_KEY を設定してください。")
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)

    title = meta.get("title", "不明")
    channel = meta.get("channel", meta.get("uploader", "不明"))
    upload_date = meta.get("upload_date", "不明")
    if upload_date and len(upload_date) == 8:
        upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"

    speakers_info = ""
    if speakers_hint:
        speakers_info = f"この動画の出演者（推定）: {', '.join(speakers_hint)}\n"
        for sp in speakers_hint:
            if sp in SPEAKER_DB:
                info = SPEAKER_DB[sp]
                speakers_info += f"  - {sp}: {info['role']}, {info['affiliation']}\n"

    # 字幕が長すぎる場合はトリム（Sonnetの入力制限を考慮）
    max_chars = 80000
    if len(subtitle_text) > max_chars:
        subtitle_text = subtitle_text[:max_chars] + "\n\n[...字幕テキストが長すぎるため切り詰め]"

    prompt = f"""以下はボクシング関連のYouTube動画の自動字幕テキストです。
この動画から、ボクシングの試合予想に関する発言を抽出してください。

## 動画情報
- タイトル: {title}
- チャンネル: {channel}
- 公開日: {upload_date}
- URL: {url}
- 対象試合: {event_name}
{speakers_info}

## 自動字幕テキスト
{subtitle_text}

## 抽出ルール
1. 各出演者の試合予想（勝者予想・勝ち方の予想）を個別に抽出する
2. **話者の特定**: 字幕中の呼びかけ（「トさん」「竹原さん」等）、口調、文脈から話者を推定する
3. **直接引用を優先**: 可能な限り発言者の実際の言葉をraw_textに入れる。要約ではなく引用。
4. **あいまいな予想も記録**: 「ちょっと○○かな」「可能性はある」等の留保付き発言もそのまま保持
5. **条件付き予想**: 「判定ならA、KOならB」のような条件分岐はそのまま記録（一方だけ採用しない）
6. **話者が特定できない場合**: speaker_nameを "不明（要確認）" とし、推定理由をnoteに書く
7. **予想でない発言は除外**: 試合分析・展望でも勝者を示唆しない発言は含めない
8. 対象試合: {event_name} に関する発言のみ抽出。他の試合の話は除外。

## 出力形式
JSON配列で出力してください。各要素は以下の構造:
```json
[
  {{
    "speaker_name": "発言者名",
    "speaker_confidence": "high/medium/low",
    "speaker_reasoning": "話者を特定した根拠（呼びかけ、口調など）",
    "raw_text": "実際の発言（字幕テキストからの引用）",
    "normalized_text": "予想内容の要約（留保表現を保持）",
    "expected_winner": "予想した勝者名 or 不明 or 条件付き",
    "expected_method": "KO/TKO/判定/不明/条件付き",
    "nuance": "断定/やや自信あり/留保付き/条件付き/言及のみ",
    "subtitle_timestamp_approx": "字幕中でこの発言が出現するおおよその位置（冒頭/中盤/終盤）",
    "note": "補足（文脈、他の発言者との関係など）"
  }}
]
```

JSON配列のみを出力してください。説明文は不要です。"""

    print(f"[3/3] Claude Sonnet で話者分離・予想抽出中... ", end="", flush=True)
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )

    text = response.content[0].text
    print("OK")

    # JSON部分を抽出
    json_match = re.search(r'\[[\s\S]*\]', text)
    if not json_match:
        print("警告: JSONの抽出に失敗。生のレスポンスを表示します:")
        print(text)
        return []

    try:
        predictions = json.loads(json_match.group())
    except json.JSONDecodeError as e:
        print(f"警告: JSONパースエラー: {e}")
        print("生のレスポンス:")
        print(text)
        return []

    return predictions


def to_statements(predictions: list[dict], url: str, meta: dict,
                   event_id: str, upload_date: str) -> list[dict]:
    """抽出結果を standard-log-v1.2-json の statements 形式に変換"""
    statements = []
    for i, pred in enumerate(predictions, 1):
        sp_name = pred.get("speaker_name", "不明")
        sp_info = SPEAKER_DB.get(sp_name, {"role": "unknown", "affiliation": "不明"})
        confidence = pred.get("speaker_confidence", "unknown")

        stmt = {
            "statement_id": f"stmt-{event_id}-{i:03d}-draft",
            "statement_date": upload_date,
            "speaker": {
                "name": sp_name,
                "role": sp_info["role"],
                "affiliation": sp_info["affiliation"]
            },
            "content": {
                "raw_text": pred.get("raw_text", ""),
                "normalized_text": pred.get("normalized_text", "")
            },
            "source": {
                "type": "video",
                "url": url,
                "timestamp": pred.get("subtitle_timestamp_approx", "不明")
            },
            "prediction": {
                "exists": pred.get("expected_winner", "不明") != "不明",
                "predictor_name": sp_name,
                "source_url": url,
                "source_note": f"yt-dlp自動字幕 + Claude Sonnet抽出（{__import__('datetime').date.today()}）。"
                               f"話者確信度: {confidence}。"
                               f"推定根拠: {pred.get('speaker_reasoning', 'N/A')}。"
                               f"ニュアンス: {pred.get('nuance', 'N/A')}。"
                               f"{pred.get('note', '')}",
                "expected_winner": pred.get("expected_winner", "不明"),
                "expected_method": pred.get("expected_method", "不明"),
            },
            "verification": {
                "status": "pending",
                "verification_date": None,
                "winner": None,
                "method": None,
                "actual_outcome": None,
                "notes": ""
            },
            "_draft_meta": {
                "speaker_confidence": confidence,
                "speaker_reasoning": pred.get("speaker_reasoning", ""),
                "nuance": pred.get("nuance", ""),
                "needs_human_review": confidence in ("low", "medium"),
                "pipeline": "yt-dlp + claude-sonnet"
            }
        }
        statements.append(stmt)

    return statements


def main():
    parser = argparse.ArgumentParser(description="ボクシング予想発言の自動抽出")
    parser.add_argument("url", help="YouTube動画のURL")
    parser.add_argument("--event", "-e", required=True,
                        help="対象試合名（例: '井上尚弥 vs 中谷潤人'）")
    parser.add_argument("--event-id", "-i", default=None,
                        help="イベントID（例: 'boxing-2026-05-02'）。未指定なら自動生成")
    parser.add_argument("--speakers", "-s", default=None,
                        help="出演者名（カンマ区切り）。未指定ならチャンネル名から推定")
    parser.add_argument("--output", "-o", default=None,
                        help="出力JSONファイルパス。未指定なら標準出力")
    parser.add_argument("--raw-subtitle", action="store_true",
                        help="字幕テキストだけ出力して終了（デバッグ用）")

    args = parser.parse_args()

    # 1. 字幕取得
    subtitle_text, meta = get_subtitles(args.url)

    if args.raw_subtitle:
        print("\n=== 字幕テキスト ===")
        print(subtitle_text)
        return

    # 2. スピーカー推定
    if args.speakers:
        speakers = [s.strip() for s in args.speakers.split(",")]
    else:
        speakers = guess_speakers_from_meta(meta)
        if speakers:
            print(f"  推定スピーカー: {', '.join(speakers)}")
        else:
            print("  スピーカー推定できず。字幕の文脈から推定します。")

    # 3. Claude で抽出
    predictions = extract_with_claude(subtitle_text, meta, args.event, speakers, args.url)

    if not predictions:
        print("予想発言が見つかりませんでした。")
        return

    # 4. statements 形式に変換
    upload_date = meta.get("upload_date", "")
    if upload_date and len(upload_date) == 8:
        upload_date = f"{upload_date[:4]}-{upload_date[4:6]}-{upload_date[6:]}"

    event_id = args.event_id or f"boxing-draft-{upload_date}"
    statements = to_statements(predictions, args.url, meta, event_id, upload_date)

    # 5. 出力
    output = {
        "_pipeline_info": {
            "source_url": args.url,
            "video_title": meta.get("title", ""),
            "channel": meta.get("channel", ""),
            "upload_date": upload_date,
            "event": args.event,
            "extraction_date": str(__import__("datetime").date.today()),
            "tool": "fetch_predictions.py (yt-dlp + Claude Sonnet)"
        },
        "statements": statements
    }

    json_str = json.dumps(output, ensure_ascii=False, indent=4)

    if args.output:
        Path(args.output).write_text(json_str, encoding="utf-8")
        print(f"\n保存: {args.output}")
    else:
        print(f"\n=== 抽出結果 ({len(statements)}件) ===")
        print(json_str)

    # 要確認フラグのサマリー
    needs_review = [s for s in statements if s.get("_draft_meta", {}).get("needs_human_review")]
    if needs_review:
        print(f"\n⚠ 要確認: {len(needs_review)}件（話者確信度がmedium/low）")
        for s in needs_review:
            dm = s["_draft_meta"]
            print(f"  - {s['statement_id']}: {s['speaker']['name']} "
                  f"(confidence={dm['speaker_confidence']}, reason={dm['speaker_reasoning'][:50]})")


if __name__ == "__main__":
    main()
