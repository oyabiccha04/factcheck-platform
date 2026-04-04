#!/usr/bin/env python3
"""
ボクシング興行向け: 指定チャンネル内を YouTube Data API v3 で検索し、
試合日前の「予想動画」候補（タイトル・URL）を列挙する。

API キーはリポジトリ直下の `.env` の YOUTUBE_API_KEY を load_dotenv のあと os.getenv で参照（コードに直書きしない）。

使い方:
  pip install -r scripts/requirements-boxing-youtube.txt
  copy .env.example .env
  python scripts/boxing_youtube_prediction_scan.py --event data/events/boxing-2024-02-24-event-06.json

オプション:
  --channels  チャンネル一覧 JSON
  --days-before / --end-before-match-days / --max-results
  --json-out  結果 JSON（既定: data/tmp/youtube-scan-latest.json）
  --skip-json  JSON ファイルを書かない
  --no-title-filter  タイトルに「予想」「勝敗」が無い動画も残す
  --include-rizin-queries  RIZIN 系の検索語も試す（MMA 向け）
  --apply-to-event  スキャン後に --event の興行 JSON を更新（動画 source / prediction）

  スキャン JSON だけを後から当てる場合:
  python scripts/apply_event_from_scan_file.py data/tmp/scan.json data/events/boxing-2024-02-24-event-06.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
from pathlib import Path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CHANNELS = REPO_ROOT / "data/observation-masters/boxing-youtube-channels-v1.json"
DEFAULT_JSON_OUT = REPO_ROOT / "data/tmp/youtube-scan-latest.json"


def _load_dotenv() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return
    load_dotenv(REPO_ROOT / ".env")


_load_dotenv()

# マスター channel label へ寄せる（公式チャンネルがマスタにある発言者のみ自動更新対象）
SPEAKER_TO_CHANNEL_LABEL: dict[str, str] = {
    "村田諒太": "村田諒太",
    "具志堅用高": "具志堅用高",
    "内山高志": "内山高志",
    "渡嘉敷勝男": "渡嘉敷・竹原・畑山",
    "竹原慎二": "渡嘉敷・竹原・畑山",
    "畑山隆則": "渡嘉敷・竹原・畑山",
    "細川バレンタイン": "細川バレンタイン",
    "京口紘人": "京口紘人",
    "亀田興毅": "亀田興毅",
    "山中慎介": "山中慎介",
    "長谷川穂積": "長谷川穂積",
    "飯田覚士": "飯田覚士",
}


def load_channels(path: Path) -> list[dict]:
    data = json.loads(path.read_text(encoding="utf-8"))
    ch = data.get("channels") or []
    out = []
    for row in ch:
        label = row.get("label") or row.get("name")
        cid = row.get("channel_id")
        if label and cid:
            out.append({"label": str(label), "channel_id": str(cid)})
    return out


def load_event_context(event_path: Path) -> dict:
    raw = json.loads(event_path.read_text(encoding="utf-8"))
    meta = raw.get("event_meta") or {}
    date_str = meta.get("date")
    if not date_str:
        raise SystemExit("イベント JSON に event_meta.date がありません。")

    cards = raw.get("cards") or []
    main = next((c for c in cards if c.get("card_id") == "main"), cards[0] if cards else None)
    bouts = (main or {}).get("bouts") or []
    bout = bouts[0] if bouts else {}
    red = (bout.get("red") or "").strip()
    blue = (bout.get("blue") or "").strip()
    if not red or not blue:
        raise SystemExit("メインカードの red/blue から検索語を組み立てられません。--query を指定してください。")

    discipline = (meta.get("discipline") or "").strip().lower()
    return {
        "base_query": f"{red} {blue}",
        "match_date": str(date_str)[:10],
        "red": red,
        "blue": blue,
        "discipline": discipline,
    }


def build_search_query_variants(
    base_query: str,
    red: str,
    blue: str,
    *,
    include_rizin: bool,
) -> list[str]:
    """苗字のみの単純クエリを避け、試合・予想・勝敗を含む語を優先して並べる。"""
    variants: list[str] = []
    seen: set[str] = set()

    def add(q: str) -> None:
        q = " ".join(q.split())
        if q and q not in seen:
            seen.add(q)
            variants.append(q)

    if red and blue:
        add(f"{red} {blue} 試合予想")
        add(f"{red} {blue} 勝敗 予想")
        add(f"{red} {blue} ボクシング 予想")
        add(f"{blue} 試合予想")
        add(f"{red} 試合予想")
        add(f"{blue} 勝敗 予想")
        add(f"{red} 勝敗 予想")
    if include_rizin:
        if blue:
            add(f"{blue} RIZIN 勝利予想")
        if red:
            add(f"{red} RIZIN 勝利予想")
        if red and blue:
            add(f"{red} {blue} RIZIN 勝利予想")
        if not red and not blue:
            add(f"{base_query} RIZIN 勝利予想")

    add(f"{base_query} 試合予想")
    add(f"{base_query} 勝敗 予想")
    add(f"{base_query} ボクシング 予想")
    add(base_query)
    return variants


def title_matches_prediction_focus(title: str) -> bool:
    if not title:
        return False
    return ("予想" in title) or ("勝敗" in title)


def search_channel_videos(
    youtube,
    channel_id: str,
    q: str,
    match_date_str: str,
    days_before: int,
    end_before_match_days: int,
    max_results: int,
):
    match_date = dt.datetime.strptime(match_date_str, "%Y-%m-%d")
    start = match_date - dt.timedelta(days=days_before)
    end = match_date - dt.timedelta(days=end_before_match_days)
    published_after = start.isoformat() + "Z"
    published_before = end.isoformat() + "Z"

    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        q=q,
        publishedAfter=published_after,
        publishedBefore=published_before,
        type="video",
        maxResults=min(50, max_results),
    )
    return request.execute().get("items") or []


def collect_videos_for_channel(
    youtube,
    channel_id: str,
    query_variants: list[str],
    match_date_str: str,
    days_before: int,
    end_before_match_days: int,
    max_results: int,
    apply_title_filter: bool,
) -> tuple[list[dict], list[str]]:
    """クエリ候補を順に試し、重複を除いた動画リストと、ヒットに使ったクエリ一覧を返す。"""
    out: list[dict] = []
    seen_ids: set[str] = set()
    queries_used: list[str] = []

    for q in query_variants:
        if len(out) >= max_results:
            break
        items = search_channel_videos(
            youtube,
            channel_id,
            q,
            match_date_str,
            days_before,
            end_before_match_days,
            50,
        )
        got_any = False
        for item in items:
            sn = item.get("snippet") or {}
            title = sn.get("title") or ""
            if apply_title_filter and not title_matches_prediction_focus(title):
                continue
            vid = (item.get("id") or {}).get("videoId")
            if not vid or vid in seen_ids:
                continue
            seen_ids.add(vid)
            got_any = True
            out.append(item)
            if len(out) >= max_results:
                break
        if got_any and q not in queries_used:
            queries_used.append(q)

    return out, queries_used


def report_label_to_first_video(report: dict) -> dict[str, dict]:
    """channel label -> 先頭動画メタ（url, title, queries_used）"""
    out: dict[str, dict] = {}
    for ch in report.get("channels") or []:
        if ch.get("error"):
            continue
        label = ch.get("label") or ""
        vids = ch.get("videos") or []
        if not label or not vids:
            continue
        v0 = vids[0]
        out[label] = {
            "url": v0.get("url") or "",
            "title": v0.get("title") or "",
            "queries_used": ch.get("queries_used") or [],
        }
    return out


def apply_report_to_event_json(
    event_path: Path,
    report: dict,
    *,
    confirm_date: str,
) -> tuple[int, list[str]]:
    """
    動画タイプの statement のうち、マスターに紐づく発言者の source / prediction を更新する。
    戻り値: (更新件数, メッセージログ)
    """
    raw = json.loads(event_path.read_text(encoding="utf-8"))
    statements = raw.get("statements") or []
    label_map = report_label_to_first_video(report)
    log: list[str] = []
    updated = 0

    for st in statements:
        sp = (st.get("speaker") or {}).get("name") or ""
        sp = str(sp).strip()
        ch_label = SPEAKER_TO_CHANNEL_LABEL.get(sp)
        if not ch_label:
            continue
        src = st.get("source") or {}
        if src.get("type") != "video":
            continue
        pred = st.get("prediction") or {}
        meta = label_map.get(ch_label)
        if not meta or not meta.get("url"):
            note = (
                f"YouTube Data API 検索（scripts/boxing_youtube_prediction_scan.py）で該当なし（"
                f"チャンネル: {ch_label}、タイトルに予想/勝敗を含む候補なし）。確認日: {confirm_date}。"
            )
            pred["source_note"] = note
            log.append(f"{sp}: 該当動画なし → source_note のみ更新")
            updated += 1
            continue

        url = meta["url"]
        title = meta["title"]
        qu = ", ".join(meta.get("queries_used") or []) or "（同一クエリ内）"
        src["url"] = url
        pred["source_url"] = url
        pred["source_note"] = (
            f"YouTube Data API v3（boxing_youtube_prediction_scan.py）。"
            f"チャンネル: {ch_label}。先頭候補タイトル: {title}。ヒットした検索語: {qu}。確認日: {confirm_date}。"
        )
        src["timestamp"] = "不明"
        log.append(f"{sp}: {url}")
        updated += 1

    event_path.write_text(json.dumps(raw, ensure_ascii=False, indent=4), encoding="utf-8")
    return updated, log


def main() -> int:
    parser = argparse.ArgumentParser(description="ボクシング予測動画候補を YouTube API で列挙")
    parser.add_argument("--query", "-q", help="検索の基準語（--event 未使用時は必須）")
    parser.add_argument("--match-date", "-d", help="試合日 YYYY-MM-DD（--event 未使用時は必須）")
    parser.add_argument("--event", "-e", type=Path, help="興行 JSON から対戦カード・日付を取得")
    parser.add_argument("--channels", type=Path, default=DEFAULT_CHANNELS, help="チャンネル一覧 JSON")
    parser.add_argument("--days-before", type=int, default=30)
    parser.add_argument("--end-before-match-days", type=int, default=1)
    parser.add_argument("--max-results", type=int, default=3)
    parser.add_argument(
        "--json-out",
        type=Path,
        default=DEFAULT_JSON_OUT,
        help="結果 JSON の出力先（既定: data/tmp/youtube-scan-latest.json）",
    )
    parser.add_argument("--skip-json", action="store_true", help="JSON ファイルを書かない")
    parser.add_argument("--no-title-filter", action="store_true", help="タイトル「予想」「勝敗」フィルタを無効化")
    parser.add_argument(
        "--include-rizin-queries",
        action="store_true",
        help="RIZIN 系の検索語も試す（格闘技・イベントに合わせて）",
    )
    parser.add_argument(
        "--apply-to-event",
        action="store_true",
        help="スキャン結果で --event で指定した興行 JSON の動画 source / prediction を上書き保存する",
    )
    parser.add_argument(
        "--confirm-date",
        default="2026-04-04",
        help="source_note に記す確認日（既定: 2026-04-04）",
    )
    args = parser.parse_args()

    api_key = os.getenv("YOUTUBE_API_KEY", "").strip()
    if not api_key:
        print(
            "環境変数 YOUTUBE_API_KEY が未設定です。"
            "リポジトリ直下の `.env` に YOUTUBE_API_KEY=... を書くか、"
            "システムの環境変数に設定してください。",
            file=sys.stderr,
        )
        return 1

    red, blue = "", ""
    if args.event:
        event_path = args.event if args.event.is_absolute() else REPO_ROOT / args.event
        ctx = load_event_context(event_path)
        query = args.query or ctx["base_query"]
        match_date = args.match_date or ctx["match_date"]
        red, blue = ctx["red"], ctx["blue"]
        include_rizin = args.include_rizin_queries or ("rizin" in (ctx.get("discipline") or ""))
    else:
        if not args.query or not args.match_date:
            print("--query と --match-date、または --event が必要です。", file=sys.stderr)
            return 1
        query = args.query
        match_date = args.match_date
        include_rizin = args.include_rizin_queries

    query_variants = build_search_query_variants(query, red, blue, include_rizin=include_rizin)
    apply_filter = not args.no_title_filter

    ch_path = args.channels if args.channels.is_absolute() else REPO_ROOT / args.channels
    if not ch_path.is_file():
        print(f"チャンネルファイルが見つかりません: {ch_path}", file=sys.stderr)
        return 1

    channels = load_channels(ch_path)
    if not channels:
        print("channels が空です。", file=sys.stderr)
        return 1

    youtube = build("youtube", "v3", developerKey=api_key, cache_discovery=False)

    report = {
        "base_query": query,
        "query_variants": query_variants,
        "match_date": match_date,
        "published_window": {
            "days_before": args.days_before,
            "end_before_match_days": args.end_before_match_days,
        },
        "title_filter": {
            "enabled": apply_filter,
            "title_must_contain_any_of": ["予想", "勝敗"] if apply_filter else [],
        },
        "channels": [],
    }

    print(f"--- 基準クエリ: {query} ---")
    print(f"--- 検索語候補（順に試行）: {len(query_variants)} パターン ---")
    print(
        f"--- 掲載期間: 試合日 {match_date} の {args.days_before} 日前 〜 "
        f"試合の {args.end_before_match_days} 日前まで ---"
    )
    print(f"--- タイトルフィルタ: {'予想/勝敗 を含む動画のみ' if apply_filter else 'オフ'} ---\n")

    for row in channels:
        name = row["label"]
        cid = row["channel_id"]
        try:
            items, used_q = collect_videos_for_channel(
                youtube,
                cid,
                query_variants,
                match_date,
                args.days_before,
                args.end_before_match_days,
                args.max_results,
                apply_filter,
            )
        except HttpError as e:
            print(f"【{name}】 API エラー: {e}", file=sys.stderr)
            report["channels"].append(
                {
                    "label": name,
                    "channel_id": cid,
                    "error": str(e),
                    "queries_used": [],
                    "videos": [],
                }
            )
            continue

        entry = {
            "label": name,
            "channel_id": cid,
            "queries_used": used_q,
            "videos": [],
        }
        if items:
            print(f"【{name}】（ヒットした検索語: {', '.join(used_q) or '（なし）'}）")
            for item in items:
                sn = item.get("snippet") or {}
                title = sn.get("title") or ""
                vid = (item.get("id") or {}).get("videoId")
                if not vid:
                    continue
                url = f"https://www.youtube.com/watch?v={vid}"
                pub = sn.get("publishedAt") or ""
                passed = title_matches_prediction_focus(title) if apply_filter else True
                print(f"  - タイトル: {title}")
                print(f"    URL: {url}")
                entry["videos"].append(
                    {
                        "title": title,
                        "url": url,
                        "publishedAt": pub,
                        "title_matches_prediction_focus": passed,
                    }
                )
            print()
        else:
            print(f"【{name}】 該当動画なし\n")
        report["channels"].append(entry)

    if not args.skip_json:
        out_path = args.json_out if args.json_out.is_absolute() else REPO_ROOT / args.json_out
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"JSON を書きました: {out_path}")

    if args.apply_to_event:
        if not args.event:
            print("--apply-to-event には --event が必要です。", file=sys.stderr)
            return 1
        event_path = args.event if args.event.is_absolute() else REPO_ROOT / args.event
        if not event_path.is_file():
            print(f"イベントファイルが見つかりません: {event_path}", file=sys.stderr)
            return 1
        n, log = apply_report_to_event_json(event_path, report, confirm_date=args.confirm_date)
        print(f"\n--- イベント JSON を更新しました（対象 {n} 件）: {event_path} ---")
        for line in log:
            print(line)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
