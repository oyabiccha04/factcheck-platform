# 格闘技ログ: Gemini再抽出プロンプト集（正本）

このファイルを正本として運用します（Gemini依頼文の参照先）。

- 対象: `data/events/*.json`（格闘技ログ全般）
- 適用範囲: RIZIN/UFC/ボクシング/キック/MMA ほか
- 観測基準: `PROJECT_CHARTER.md` の Tier A/Tier B（Tier B は登録者数 + 影響力）

## 運用

- Gemini依頼文は本ファイル名（`MARTIAL_ARTS_GEMINI_PROMPTS.md`）を基準に参照する
- 既存の `docs/BOXING_WORLD_TITLE_GEMINI_PROMPTS.md` は互換用（旧名称）として扱う
- 件数要件は最新運用として **最低15件** を基準にする
- 予測抽出では **日本国内の予測・一次情報を優先** する
- 同条件で比較できる場合は海外ソースより国内ソースを優先し、国内だけで件数要件を満たせない場合のみ海外ソースで補完する
- 実行時は対象イベントに応じて `event_id` / `event_name` / `target_bout` を差し替える
- **混在興行（MMA + キック等）**：各 bout に正しい **`discipline`**（例: `MMA` / `KICKBOXING`）を必ず付与する。`statements[].prediction.target` は **カードの red vs blue 表記と一致**させる（サイト上の種目別予測者ランキングが bout・target から種目を判定するため）

## 参照

- 互換ファイル（旧名称）: `docs/BOXING_WORLD_TITLE_GEMINI_PROMPTS.md`
- ルール正本: `PROJECT_CHARTER.md`

---

## ONEチャンピオンシップ 対象試合一覧（差し込み用）

| # | event_id | target_bout | event_date | 確定結果 |
|---|---|---|---|---|
| 1 | one-165 | スーパーレック・キアトモー9 vs 武尊 | 2024-01-28 | スーパーレック・キアトモー9 / 判定 |
| 2 | one-167 | シッティチャイ・シッソンピーノン vs 野杁正明 | 2024-06-08 | シッティチャイ・シッソンピーノン / 判定 |
| 3 | one-friday-fights-81 | 武尊 vs タン・ジン | 2024-09-27 | 武尊 / KO |
| 4 | one-friday-fights-92 | リウ・メンヤン vs 野杁正明 | 2024-12-20 | リウ・メンヤン / 判定 |
| 5 | one-170 | シャキール・アル・テクリティ vs 野杁正明 | 2025-01-24 | 野杁正明 / KO |
| 6 | one-172 | ロッタン・ジットムアンノン vs 武尊 | 2025-03-23 | ロッタン・ジットムアンノン / KO |
| 7 | one-172 | タワンチャイ・PK・センチャイ vs 野杁正明 | 2025-03-23 | 野杁正明 / TKO |
| 8 | one-173 | スーパーボン・シンハー・マウィン vs 野杁正明 | 2025-11-16 | スーパーボン・シンハー・マウィン / 判定 |
| 9 | one-173 | 武尊 vs デニス・ピューリック | 2025-11-16 | 武尊 / TKO |
| 10 | one-173 | 与座優貴 vs スーパーレック・キアトモー9 | 2025-11-16 | 与座優貴 / 判定 |
| 11 | one-173 | マラット・グレゴリアン vs 安保瑠輝也 | 2025-11-16 | マラット・グレゴリアン / 判定 |
| 12 | one-samurai-1 | ロッタン・ジットムアンノン vs 武尊 | 2026-04-29 | 未確定 |
| 13 | one-samurai-1 | ジョナサン・ハガティー vs 与座優貴 | 2026-04-29 | 未確定 |

---

## 実行版（one-165 / ONE 165: Superlek vs. Takeru）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-165
- event_name: ONE 165: Superlek vs. Takeru
- event_date: 2024-01-28
- timezone: Asia/Tokyo
- target_bout: スーパーレック・キアトモー9 vs 武尊

# 確定結果（正本）
- winner: スーパーレック・キアトモー9
- method: 判定
- notes: ONEフライ級キックボクシング世界タイトルマッチ。武尊のONEデビュー戦。有明アリーナ

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する（日本語記事/動画/SNS、日本国内メディア、日本で活動する発信者を優先）
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 同条件で比較できる場合は海外ソースより国内ソースを優先する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note にその旨を簡潔に残す

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）
- 対象試合と無関係なURLは採用しない

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者/解説系発信者（登録者10万人以上を原則。未満でも影響力が高ければ対象）
- predictor_name は必ず個人名で記録する（媒体名・編集部名・集合ラベルは禁止）
- 1本の動画で複数人が予測している場合は、人物ごとに別レコードで出力する

# 件数要件
- statements は最低 15 件を目標に抽出する
- 一次情報で条件を満たす予測が 15 件未満の場合は、無理に捏造せず取得できた件数だけ返す

# 抽出ルール（厳守）
- 対象は「勝者方向の予測」（誰が勝つ/有利）
- prediction.target は「スーパーレック・キアトモー9 vs 武尊」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は スーパーレック・キアトモー9、method は 判定
- verification の actual_outcome は事実記述のみ（評価語禁止）
- statement_id は stmt-one-165-### 形式で採番（001開始）
- source.url はすべて生URLのみ（Markdown記法禁止）
- 同一人物が同一勝者方向を複数回述べている場合は最も明確な1件のみ

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-165-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-165-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "スーパーレック・キアトモー9 vs 武尊",
        "expected_outcome": "例: スーパーレック・キアトモー9が判定勝ち",
        "deadline": "2024-01-28"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2024-01-28",
        "winner": "スーパーレック・キアトモー9",
        "method": "判定",
        "actual_outcome": "スーパーレック・キアトモー9が判定3-0で防衛",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-167 / ONE 167: Tawanchai vs. Nattawut 2）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-167
- event_name: ONE 167: Tawanchai vs. Nattawut 2
- event_date: 2024-06-08
- timezone: Asia/Bangkok
- target_bout: シッティチャイ・シッソンピーノン vs 野杁正明

# 確定結果（正本）
- winner: シッティチャイ・シッソンピーノン
- method: 判定
- notes: フェザー級キックボクシング。野杁正明のONEデビュー戦。バンコク・インパクトアリーナ

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する
- 不足の場合は charter_update_candidates に理由を記載

# 抽出ルール（厳守）
- prediction.target は「シッティチャイ・シッソンピーノン vs 野杁正明」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は シッティチャイ・シッソンピーノン、method は 判定
- statement_id は stmt-one-167-### 形式（001開始）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-167-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-167-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "シッティチャイ・シッソンピーノン vs 野杁正明",
        "expected_outcome": "例: シッティチャイ・シッソンピーノンが判定勝ち",
        "deadline": "2024-06-08"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2024-06-08",
        "winner": "シッティチャイ・シッソンピーノン",
        "method": "判定",
        "actual_outcome": "シッティチャイ・シッソンピーノンが判定3-0勝ち",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-friday-fights-81 / ONE Friday Fights 81）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-friday-fights-81
- event_name: ONE Friday Fights 81
- event_date: 2024-09-27
- timezone: Asia/Bangkok
- target_bout: 武尊 vs タン・ジン

# 確定結果（正本）
- winner: 武尊
- method: KO
- round: 2
- notes: フライ級キックボクシング。武尊のONE初勝利。ルンピニースタジアム

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（ただしONE Friday Fights は注目度が低い可能性あり。不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「武尊 vs タン・ジン」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は 武尊、method は KO
- statement_id は stmt-one-friday-fights-81-### 形式（001開始）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-friday-fights-81-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-friday-fights-81-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "武尊 vs タン・ジン",
        "expected_outcome": "例: 武尊がKO勝ち",
        "deadline": "2024-09-27"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2024-09-27",
        "winner": "武尊",
        "method": "KO",
        "actual_outcome": "武尊が2RでKO勝ち",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-friday-fights-92 / ONE Friday Fights 92）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-friday-fights-92
- event_name: ONE Friday Fights 92: Sitthichai vs. Shadow
- event_date: 2024-12-20
- timezone: Asia/Bangkok
- target_bout: リウ・メンヤン vs 野杁正明

# 確定結果（正本）
- winner: リウ・メンヤン
- method: 判定
- notes: フェザー級キックボクシング。リウ・メンヤンのONEデビュー戦。ルンピニースタジアム

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「リウ・メンヤン vs 野杁正明」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は リウ・メンヤン、method は 判定
- statement_id は stmt-one-friday-fights-92-### 形式（001開始）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-friday-fights-92-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-friday-fights-92-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "リウ・メンヤン vs 野杁正明",
        "expected_outcome": "例: 野杁正明が判定勝ち",
        "deadline": "2024-12-20"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2024-12-20",
        "winner": "リウ・メンヤン",
        "method": "判定",
        "actual_outcome": "リウ・メンヤンが判定3-0勝ち",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-170 / ONE 170: Tawanchai vs. Superbon II）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-170
- event_name: ONE 170: Tawanchai vs. Superbon II
- event_date: 2025-01-24
- timezone: Asia/Bangkok
- target_bout: シャキール・アル・テクリティ vs 野杁正明

# 確定結果（正本）
- winner: 野杁正明
- method: KO
- round: 2
- notes: ONEフェザー級キックボクシング暫定世界タイトルマッチ。バンコク・インパクトアリーナ

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「シャキール・アル・テクリティ vs 野杁正明」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は 野杁正明、method は KO
- statement_id は stmt-one-170-### 形式（001開始）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-170-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-170-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "シャキール・アル・テクリティ vs 野杁正明",
        "expected_outcome": "例: 野杁正明がKO勝ち",
        "deadline": "2025-01-24"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2025-01-24",
        "winner": "野杁正明",
        "method": "KO",
        "actual_outcome": "野杁正明が2RでKO勝ち（ONEフェザー級キックボクシング暫定王座獲得）",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-172a / ONE 172: ロッタン vs 武尊）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-172
- event_name: ONE 172: Takeru vs. Rodtang
- event_date: 2025-03-23
- timezone: Asia/Tokyo
- target_bout: ロッタン・ジットムアンノン vs 武尊

# 確定結果（正本）
- winner: ロッタン・ジットムアンノン
- method: KO
- round: 1
- time: 1:20
- notes: フライ級キックボクシング スーパーファイト（非タイトルマッチ）。さいたまスーパーアリーナ

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「ロッタン・ジットムアンノン vs 武尊」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は ロッタン・ジットムアンノン、method は KO
- statement_id は stmt-one-172-### 形式（001開始）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-172-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-172-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "ロッタン・ジットムアンノン vs 武尊",
        "expected_outcome": "例: 武尊がKO勝ち",
        "deadline": "2025-03-23"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2025-03-23",
        "winner": "ロッタン・ジットムアンノン",
        "method": "KO",
        "actual_outcome": "ロッタン・ジットムアンノンが1R 1:20でKO勝ち",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-172b / ONE 172: タワンチャイ vs 野杁正明）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-172
- event_name: ONE 172: Takeru vs. Rodtang
- event_date: 2025-03-23
- timezone: Asia/Tokyo
- target_bout: タワンチャイ・PK・センチャイ vs 野杁正明

# 確定結果（正本）
- winner: 野杁正明
- method: TKO
- round: 3
- time: 1:55
- notes: ONEフェザー級キックボクシング暫定世界タイトルマッチ。野杁正明が暫定王座獲得。さいたまスーパーアリーナ

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「タワンチャイ・PK・センチャイ vs 野杁正明」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は 野杁正明、method は TKO
- statement_id は stmt-one-172-### 形式（※one-172aと通し番号にする場合は事前に最終番号を確認して続番で採番）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-172-XXX",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-172-XXX",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "タワンチャイ・PK・センチャイ vs 野杁正明",
        "expected_outcome": "例: 野杁正明がTKO勝ち",
        "deadline": "2025-03-23"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2025-03-23",
        "winner": "野杁正明",
        "method": "TKO",
        "actual_outcome": "野杁正明が3R 1:55でTKO勝ち（ONEフェザー級キックボクシング暫定王座獲得）",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-173a / ONE 173: スーパーボン vs 野杁正明）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-173
- event_name: ONE 173: Superbon vs. Noiri
- event_date: 2025-11-16
- timezone: Asia/Tokyo
- target_bout: スーパーボン・シンハー・マウィン vs 野杁正明

# 確定結果（正本）
- winner: スーパーボン・シンハー・マウィン
- method: 判定
- notes: ONEフェザー級キックボクシング王座統一戦（スーパーボン=正規王者、野杁=暫定王者）。5R。有明アリーナ

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「スーパーボン・シンハー・マウィン vs 野杁正明」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は スーパーボン・シンハー・マウィン、method は 判定
- statement_id は stmt-one-173-### 形式（001開始）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-173-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-173-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "スーパーボン・シンハー・マウィン vs 野杁正明",
        "expected_outcome": "例: 野杁正明が判定勝ち",
        "deadline": "2025-11-16"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2025-11-16",
        "winner": "スーパーボン・シンハー・マウィン",
        "method": "判定",
        "actual_outcome": "スーパーボン・シンハー・マウィンが判定3-0勝ち（王座統一）",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-173b / ONE 173: 武尊 vs デニス・ピューリック）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-173
- event_name: ONE 173: Superbon vs. Noiri
- event_date: 2025-11-16
- timezone: Asia/Tokyo
- target_bout: 武尊 vs デニス・ピューリック

# 確定結果（正本）
- winner: 武尊
- method: TKO
- round: 2
- time: 2:49
- notes: フライ級キックボクシング。武尊がパフォーマンス・オブ・ザ・ナイト受賞（4ダウン奪取）。有明アリーナ

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「武尊 vs デニス・ピューリック」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は 武尊、method は TKO
- statement_id は stmt-one-173-### 形式（※one-173aと通し番号にする場合は最終番号を確認して続番で採番）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-173-XXX",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-173-XXX",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "武尊 vs デニス・ピューリック",
        "expected_outcome": "例: 武尊がTKO勝ち",
        "deadline": "2025-11-16"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2025-11-16",
        "winner": "武尊",
        "method": "TKO",
        "actual_outcome": "武尊が2R 2:49でTKO勝ち",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-173c / ONE 173: 与座優貴 vs スーパーレック・キアトモー9）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-173
- event_name: ONE 173: Superbon vs. Noiri
- event_date: 2025-11-16
- timezone: Asia/Tokyo
- target_bout: 与座優貴 vs スーパーレック・キアトモー9

# 確定結果（正本）
- winner: 与座優貴
- method: 判定
- notes: バンタム級キックボクシング。与座優貴が判定3-0勝ち。有明アリーナ

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「与座優貴 vs スーパーレック・キアトモー9」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は 与座優貴、method は 判定
- statement_id は stmt-one-173-### 形式（続番で採番）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-173-XXX",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-173-XXX",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "与座優貴 vs スーパーレック・キアトモー9",
        "expected_outcome": "例: 与座優貴が判定勝ち",
        "deadline": "2025-11-16"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2025-11-16",
        "winner": "与座優貴",
        "method": "判定",
        "actual_outcome": "与座優貴が判定3-0勝ち",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-173d / ONE 173: マラット・グレゴリアン vs 安保瑠輝也）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-173
- event_name: ONE 173: Superbon vs. Noiri
- event_date: 2025-11-16
- timezone: Asia/Tokyo
- target_bout: マラット・グレゴリアン vs 安保瑠輝也

# 確定結果（正本）
- winner: マラット・グレゴリアン
- method: 判定
- notes: フェザー級キックボクシング。安保が体重超過（155.4lb）。有明アリーナ

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「マラット・グレゴリアン vs 安保瑠輝也」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification の winner は マラット・グレゴリアン、method は 判定
- statement_id は stmt-one-173-### 形式（続番で採番）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-173-XXX",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-173-XXX",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "マラット・グレゴリアン vs 安保瑠輝也",
        "expected_outcome": "例: 安保瑠輝也が判定勝ち",
        "deadline": "2025-11-16"
      },
      "verification": {
        "status": "resolved",
        "verification_date": "2025-11-16",
        "winner": "マラット・グレゴリアン",
        "method": "判定",
        "actual_outcome": "マラット・グレゴリアンが判定3-0勝ち",
        "notes": "一次情報URLに基づく事実",
        "source_note": "根拠URL: "
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-samurai-1a / ONE Samurai 1: ロッタン vs 武尊 ※未開催）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-samurai-1
- event_name: ONE Samurai 1: Rodtang vs. Takeru II
- event_date: 2026-04-29
- timezone: Asia/Tokyo
- target_bout: ロッタン・ジットムアンノン vs 武尊

# 確定結果
- ※ 本イベントは未開催（2026-04-29）のため verification は unresolved で返す

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「ロッタン・ジットムアンノン vs 武尊」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification.status は「unresolved」（試合未実施）
- verification の winner / method / actual_outcome はすべて「不明」
- statement_id は stmt-one-samurai-1-### 形式（001開始）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-samurai-1-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-samurai-1-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "ロッタン・ジットムアンノン vs 武尊",
        "expected_outcome": "例: 武尊がKO勝ち",
        "deadline": "2026-04-29"
      },
      "verification": {
        "status": "unresolved",
        "verification_date": "不明",
        "winner": "不明",
        "method": "不明",
        "actual_outcome": "不明",
        "notes": "2026-04-29 開催予定。試合後に outcome と照合して resolved に更新する",
        "source_note": ""
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 実行版（one-samurai-1b / ONE Samurai 1: ハガティー vs 与座優貴 ※未開催）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: one-samurai-1
- event_name: ONE Samurai 1: Rodtang vs. Takeru II
- event_date: 2026-04-29
- timezone: Asia/Tokyo
- target_bout: ジョナサン・ハガティー vs 与座優貴

# 確定結果
- ※ 本イベントは未開催（2026-04-29）のため verification は unresolved で返す

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する
- 予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note に記載

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- YouTube（youtube.com）を検索対象に必ず含める
- URLは生URLで出力する（Markdownリンク禁止）

# 観測する予測者（CHARTER準拠）
- Tier A: 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B: 格闘技を扱う有名YouTuber/配信者（登録者10万人以上を原則）
- predictor_name は必ず個人名で記録する

# 件数要件
- statements は最低 15 件を目標に抽出する（不足の場合は charter_update_candidates に理由を記載）

# 抽出ルール（厳守）
- prediction.target は「ジョナサン・ハガティー vs 与座優貴」に完全一致
- method は: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明" のみ
- verification.status は「unresolved」（試合未実施）
- verification の winner / method / actual_outcome はすべて「不明」
- statement_id は stmt-one-samurai-1-### 形式（※one-samurai-1aと通し番号にする場合は最終番号を確認して続番で採番）
- source.url はすべて生URLのみ（Markdown記法禁止）

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-one-samurai-1-XXX",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": { "name": "個人名", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
      "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
      "source": { "type": "video|article|sns", "url": "一次情報URL", "timestamp": "mm:ss または 不明" },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.nameと同一",
        "source_url": "source.urlと同一",
        "source_ref": "statement_id=stmt-one-samurai-1-XXX",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier判定メモ。",
        "expected_winner": "勝者名または不明",
        "expected_method": "判定|KO|TKO|不明",
        "target": "ジョナサン・ハガティー vs 与座優貴",
        "expected_outcome": "例: 与座優貴が判定勝ち",
        "deadline": "2026-04-29"
      },
      "verification": {
        "status": "unresolved",
        "verification_date": "不明",
        "winner": "不明",
        "method": "不明",
        "actual_outcome": "不明",
        "notes": "2026-04-29 開催予定。試合後に outcome と照合して resolved に更新する",
        "source_note": ""
      }
    }
  ],
  "charter_update_candidates": []
}
```

---

## 受け取り後の運用（ONEイベント編集側）

- Geminiが返したJSONを受け取ったら、必ず以下を最低検査する
  - URL実在性（生URLのみ / Markdown記法が混入していないか）
  - `prediction.target` が各イベントのターゲット文字列と完全一致しているか
  - `statement_id` の採番が `stmt-<event_id>-###` 形式になっているか
- 問題ないレコードのみ各イベントJSONの `statements[]` へ追記
- one-172 / one-173 は複数回に分けて抽出するため、statement_id の通し番号が重複しないように注意
  - 例: one-172a で 001〜015 を使用したら、one-172b は 016〜 から採番
- 未開催イベント（one-samurai-1）は試合後に `verification.status` を `resolved` に更新し、`winner` / `method` / `actual_outcome` を事実で埋める

