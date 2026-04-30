# 予想発言自動抽出パイプライン

## セットアップ（初回のみ）

```bash
pip install yt-dlp anthropic
```

Anthropic APIキーを環境変数に設定:
```bash
# Windows (PowerShell)
$env:ANTHROPIC_API_KEY = "sk-ant-..."

# Mac/Linux
export ANTHROPIC_API_KEY="sk-ant-..."
```

## 基本的な使い方

```bash
# ぶっちゃけチャンネルの動画から井上vs中谷の予想を抽出
python scripts/fetch_predictions.py "https://www.youtube.com/watch?v=R3L-A0m-Sss" --event "井上尚弥 vs 中谷潤人"

# 出演者を明示的に指定（チャンネル名で推定できない場合）
python scripts/fetch_predictions.py "https://www.youtube.com/watch?v=xxxxx" --event "井上尚弥 vs 中谷潤人" --speakers "竹原慎二,畑山隆則,渡嘉敷勝男"

# JSONファイルに保存
python scripts/fetch_predictions.py "https://www.youtube.com/watch?v=R3L-A0m-Sss" --event "井上尚弥 vs 中谷潤人" --output draft_statements.json

# 字幕だけ確認（APIを使わない）
python scripts/fetch_predictions.py "https://www.youtube.com/watch?v=R3L-A0m-Sss" --event "dummy" --raw-subtitle
```

## 処理の流れ

```
YouTube URL
    │
    ▼
[yt-dlp] 自動字幕ダウンロード（API枠消費なし・無制限）
    │
    ▼
字幕テキスト（プレーン化・重複除去）
    │
    ▼
[Claude Sonnet] 話者分離 + 予想抽出
  - チャンネル名/概要欄から出演者を推定
  - 字幕中の呼びかけ・口調から話者を特定
  - 予想の確信度・ニュアンスも記録
    │
    ▼
statements[] JSON（draft）
  - _draft_meta.needs_human_review = true の箇所だけ人間が確認
```

## コスト目安

- yt-dlp: 無料（YouTube Data API不使用）
- Claude Sonnet API: 1動画あたり約$0.01〜0.05（字幕の長さによる）
  - 入力: 字幕テキスト約2万〜8万文字 → 約5K〜20Kトークン
  - 出力: 抽出結果 約1K〜2Kトークン
  - 10本の動画を処理しても$0.50以下

## 出力の読み方

`_draft_meta` フィールドに品質情報が入っています:

- `speaker_confidence`: high/medium/low — 話者特定の確信度
- `speaker_reasoning`: 話者を特定した根拠
- `nuance`: 断定/留保付き/条件付き — 予想のニュアンス
- `needs_human_review`: true なら人間の確認が必要

## 既存データへのマージ

出力されたdraft statementsは、手動で対象イベントのJSONにマージしてください。
マージ時に:
1. statement_id の "-draft" を外して正式な連番に変更
2. `_draft_meta` は参考情報として残すか削除
3. `needs_human_review: true` の項目は動画を確認してから確定

## 制限事項

- 自動字幕の精度は完璧ではない（特に固有名詞）
- 3人以上の対談では話者分離の精度が下がる → confidence=low の場合は要確認
- 動画に自動字幕がない場合は使えない（手動字幕のみの動画は稀）
