# 格闘技ログ: Gemini再抽出プロンプト集（実在URL強制版）

> ファイル名統一のため、今後の正本は `docs/MARTIAL_ARTS_GEMINI_PROMPTS.md` を使用してください。  
> 本ファイルは互換のため当面維持します。

この文書は `data/events/*.json` の `statements[]` を埋めるための、貼り付け用プロンプト集です。
ボクシングの実行例を含みますが、ルール自体は格闘技ログ全般（RIZIN/UFC/ボクシング等）に適用します。

## 適用範囲（固定）

- 本文書の Tier 定義・影響力基準・一次情報ルールは、格闘技ログ全般に適用する
- `event_id` / `event_name` / `target_bout` を対象イベントに差し替えれば、団体や競技が異なっても同じ運用で使用できる
- 「対象イベント一覧」はボクシングの実行例であり、他競技の適用を制限しない

## 共通ルール（厳守 / CHARTER反映）

- 出力は JSON 配列のみ（説明文禁止）
- 推測で埋めない
- URL は必ず実在する一次情報の生URL（`[text](url)` 形式禁止）
- URL は **プレーン文字列のみ**（`[` `]` `(` `)` を含む Markdown 形式を禁止）
- `prediction.target` は対象カード文字列と完全一致
- 勝者方向が取れない発言は原則出力しない
- 予測者は CHARTER に従い **個人名で統一**（媒体名・編集部名・集合ラベルは不可）
- 観測対象は CHARTER の範囲を優先（Tier A: 選手/指導者/著名解説者、Tier B: 格闘技系著名発信者）
- **日本国内の予測・一次情報を優先** する（日本語記事/動画/SNS、日本国内メディア、日本で活動する発信者を優先）
- 同条件で比較できる場合は海外ソースより国内ソースを優先し、国内だけで件数要件を満たせない場合のみ海外ソースで補完する
- 発言者が個人として特定できない場合のみ `speaker.name = "不明"` / `predictor_name = "不明"` を許容し、`source_note` に要確認理由を明記
- CHARTER/運用文書の更新が必要になりそうな気づきは、`charter_update_candidates[]` として別枠で返す（任意）
- `notes` / `actual_outcome` は事実記述のみ（「的中」「外れ」など評価語は禁止）

### CHARTER反映候補の収集ルール（Gemini向け）

- 収集対象は「運用ルール化すべき再発パターン」のみ（単発ミスは除く）
- 事実と根拠URLに紐づく候補のみ記載する（推測禁止）
- 候補は 0 件なら `[]` を返す（無理に作らない）
- 候補には「問題」「提案ルール」「影響範囲」を短く入れる

## 共通プロンプト（URL指定なし / コピペ用）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON 配列のみ（説明文禁止）。

# 対象イベント
- event_id: <EVENT_ID>
- event_name: <EVENT_NAME>
- event_date: <EVENT_DATE>
- timezone: 不明

# 対象試合（prediction.target はこの文字列に完全一致）
- <TARGET_BOUT>

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する（日本語記事/動画/SNS、日本国内メディア、日本で活動する発信者を優先）
- 同条件で比較できる場合は海外ソースより国内ソースを優先する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note にその旨を簡潔に残す

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- URLは生URLで出力する（Markdownリンク禁止）
- 対象試合と無関係なURLは採用しない

# 抽出ルール（厳守）
- 対象は「勝者方向の予測」（誰が勝つ/有利）
- 観測対象は CHARTER 準拠（Tier A/Tier B 優先。Tier Bは登録者数に加えて影響力も加味）
- predictor_name は個人名で統一（媒体名・編集部名・ブックメーカー名・AI名を使わない）
- 同一人物が同一試合へ同じ方向を複数回述べる場合は最も明確な1件のみ
- speaker.name / expected_winner / target が一意に確定できない場合は、推測で埋めない
- timestamp は分かる場合のみ（不明なら "不明"）
- 1件も無ければ [] を返す
- CHARTER反映候補があれば `charter_update_candidates` 配列を同時に返してよい

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
    "statement_id": "AUTO_ASSIGN_BY_EDITOR",
    "statement_date": "YYYY-MM-DD または 不明",
    "speaker": { "name": "個人名（不明なら \"不明\"）", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
    "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
    "source": { "type": "video|article|sns", "url": "一次情報URL（必須）", "timestamp": "mm:ss または hh:mm:ss または 不明" },
    "prediction": {
      "exists": true,
      "predictor_name": "speaker.name と同一（個人名）",
      "source_url": "source.url と同一",
      "source_ref": "AUTO_ASSIGN_BY_EDITOR",
      "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。要確認点があれば明記。",
      "expected_winner": "勝者（不明なら \"不明\"）",
      "expected_method": "判定|KO|TKO|不明",
      "target": "<TARGET_BOUT>",
      "expected_outcome": "例：Aが判定勝ち／Aが勝利／不明",
      "deadline": "<EVENT_DATE>"
    },
    "verification": {
      "status": "unresolved",
      "verification_date": "不明",
      "winner": "不明",
      "method": "不明",
      "actual_outcome": "不明",
      "notes": "編集側で events の outcome と照合して resolved に更新する"
    }
    }
  ],
  "charter_update_candidates": [
    {
      "title": "短い題名",
      "problem": "再発している運用上の問題を事実ベースで簡潔に記載",
      "proposed_rule": "CHARTERに追記するならこの1文、という形で記載",
      "scope": "prompts|events|verification|naming など",
      "evidence_urls": [
        "根拠URL1"
      ]
    }
  ]
}
```

## 共通プロンプト（コピペ用）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON 配列のみ（説明文禁止）。

# 対象イベント
- event_id: <EVENT_ID>
- event_name: <EVENT_NAME>
- event_date: <EVENT_DATE>
- timezone: 不明

# 対象試合（prediction.target はこの文字列に完全一致）
- <TARGET_BOUT>

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する（日本語記事/動画/SNS、日本国内メディア、日本で活動する発信者を優先）
- 同条件で比較できる場合は海外ソースより国内ソースを優先する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note にその旨を簡潔に残す

# 入力（一次情報URLのみ。Markdownリンク禁止）
<SOURCE_URLS>

# 抽出ルール（厳守）
- 対象は「勝者方向の予測」（誰が勝つ/有利）
- 同一人物が同一試合へ同じ方向を複数回述べる場合は最も明確な1件のみ
- speaker.name / expected_winner / target が一意に確定できない場合は、推測で埋めない
- timestamp は分かる場合のみ（不明なら "不明"）
- predictor_name は speaker.name と同一（個人名）

# 出力フォーマット（JSON配列のみ）
[
  {
    "statement_id": "AUTO_ASSIGN_BY_EDITOR",
    "statement_date": "YYYY-MM-DD または 不明",
    "speaker": { "name": "個人名（不明なら \"不明\"）", "role": "boxer|coach|commentator|youtuber|media|other|不明", "affiliation": "不明" },
    "content": { "raw_text": "短い引用", "normalized_text": "短い要約（任意）" },
    "source": { "type": "video|article|sns", "url": "一次情報URL（必須）", "timestamp": "mm:ss または hh:mm:ss または 不明" },
    "prediction": {
      "exists": true,
      "predictor_name": "speaker.name と同一",
      "source_url": "source.url と同一",
      "source_ref": "AUTO_ASSIGN_BY_EDITOR",
      "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。要確認点があれば明記。",
      "expected_winner": "勝者（不明なら \"不明\"）",
      "expected_method": "判定|KO|TKO|不明",
      "target": "<TARGET_BOUT>",
      "expected_outcome": "例：Aが判定勝ち／Aが勝利／不明",
      "deadline": "<EVENT_DATE>"
    },
    "verification": {
      "status": "unresolved",
      "verification_date": "不明",
      "winner": "不明",
      "method": "不明",
      "actual_outcome": "不明",
      "notes": "編集側で events の outcome と照合して resolved に更新する"
    }
  }
]
```

---

## 対象イベント一覧（差し込み用）

以下を共通プロンプトの `<EVENT_*>` / `<TARGET_BOUT>` に差し込んで使ってください。

1.
- EVENT_ID: `boxing-2022-11-01-event-01`
- EVENT_NAME: `WBC・WBO世界ライトフライ級王座統一戦 寺地拳四朗 vs 京口紘人`
- EVENT_DATE: `2022-11-01`
- TARGET_BOUT: `寺地拳四朗 vs 京口紘人`

2.
- EVENT_ID: `boxing-2022-12-13-event-02`
- EVENT_NAME: `世界バンタム級4団体王座統一戦 井上尚弥 vs ポール・バトラー`
- EVENT_DATE: `2022-12-13`
- TARGET_BOUT: `井上尚弥 vs ポール・バトラー`

3.
- EVENT_ID: `boxing-2023-04-08-event-03`
- EVENT_NAME: `WBA・WBC世界ライトフライ級 寺地拳四朗 vs アンソニー・オラスクアガ`
- EVENT_DATE: `2023-04-08`
- TARGET_BOUT: `寺地拳四朗 vs アンソニー・オラスクアガ`

4.
- EVENT_ID: `boxing-2023-07-25-event-04`
- EVENT_NAME: `WBC・WBO世界スーパーバンタム級 スティーブン・フルトン vs 井上尚弥`
- EVENT_DATE: `2023-07-25`
- TARGET_BOUT: `スティーブン・フルトン vs 井上尚弥`

5.
- EVENT_ID: `boxing-2023-12-26-event-05`
- EVENT_NAME: `世界スーパーバンタム級4団体王座統一戦 井上尚弥 vs マーロン・タパレス`
- EVENT_DATE: `2023-12-26`
- TARGET_BOUT: `井上尚弥 vs マーロン・タパレス`

6.
- EVENT_ID: `boxing-2024-02-24-event-06`
- EVENT_NAME: `WBC世界バンタム級 アレハンドロ・サンティアゴ vs 中谷潤人`
- EVENT_DATE: `2024-02-24`
- TARGET_BOUT: `アレハンドロ・サンティアゴ vs 中谷潤人`

7.
- EVENT_ID: `boxing-2024-05-06-event-07`
- EVENT_NAME: `世界スーパーバンタム級4団体防衛戦 井上尚弥 vs ルイス・ネリ`
- EVENT_DATE: `2024-05-06`
- TARGET_BOUT: `井上尚弥 vs ルイス・ネリ`

8.
- EVENT_ID: `boxing-2024-05-06-event-08`
- EVENT_NAME: `WBO世界バンタム級 ジェイソン・モロニー vs 武居由樹`
- EVENT_DATE: `2024-05-06`
- TARGET_BOUT: `ジェイソン・モロニー vs 武居由樹`

9.
- EVENT_ID: `boxing-2024-09-03-event-09`
- EVENT_NAME: `世界スーパーバンタム級4団体防衛戦 井上尚弥 vs テレンス・ジョン・ドヘニー`
- EVENT_DATE: `2024-09-03`
- TARGET_BOUT: `井上尚弥 vs テレンス・ジョン・ドヘニー`

10.
- EVENT_ID: `boxing-2024-09-03-event-10`
- EVENT_NAME: `WBO世界バンタム級 武居由樹 vs 比嘉大吾`
- EVENT_DATE: `2024-09-03`
- TARGET_BOUT: `武居由樹 vs 比嘉大吾`

11.
- EVENT_ID: `boxing-2024-10-13-event-11`
- EVENT_NAME: `WBA世界バンタム級 井上拓真 vs 堤聖也`
- EVENT_DATE: `2024-10-13`
- TARGET_BOUT: `井上拓真 vs 堤聖也`

12.
- EVENT_ID: `boxing-2025-01-24-event-12`
- EVENT_NAME: `世界スーパーバンタム級4団体防衛戦 井上尚弥 vs サム・グッドマン`
- EVENT_DATE: `2025-01-24`
- TARGET_BOUT: `井上尚弥 vs サム・グッドマン`

13.
- EVENT_ID: `boxing-2025-03-13-event-13`
- EVENT_NAME: `WBC世界フライ級 寺地拳四朗 vs ユーリ阿久井政悟`
- EVENT_DATE: `2025-03-13`
- TARGET_BOUT: `寺地拳四朗 vs ユーリ阿久井政悟`

14.
- EVENT_ID: `boxing-2025-05-28-event-14`
- EVENT_NAME: `WBO世界バンタム級 武居由樹 vs ユッタポン・トンディ`
- EVENT_DATE: `2025-05-28`
- TARGET_BOUT: `武居由樹 vs ユッタポン・トンディ`

15.
- EVENT_ID: `boxing-2025-09-14-event-15`
- EVENT_NAME: `世界スーパーバンタム級4団体防衛戦 井上尚弥 vs ムロジョン・アフマダリエフ`
- EVENT_DATE: `2025-09-14`
- TARGET_BOUT: `井上尚弥 vs ムロジョン・アフマダリエフ`

16.
- EVENT_ID: `boxing-2025-09-14-event-16`
- EVENT_NAME: `WBO世界バンタム級 武居由樹 vs クリスチャン・メディナ`
- EVENT_DATE: `2025-09-14`
- TARGET_BOUT: `武居由樹 vs クリスチャン・メディナ`

17.
- EVENT_ID: `boxing-2025-11-24-event-17`
- EVENT_NAME: `WBC世界バンタム級王座決定戦 那須川天心 vs 井上拓真`
- EVENT_DATE: `2025-11-24`
- TARGET_BOUT: `那須川天心 vs 井上拓真`

18.
- EVENT_ID: `boxing-2025-12-27-event-18`
- EVENT_NAME: `世界スーパーバンタム級4団体防衛戦 井上尚弥 vs アラン・デビッド・ピカソ`
- EVENT_DATE: `2025-12-27`
- TARGET_BOUT: `井上尚弥 vs アラン・デビッド・ピカソ`

19.
- EVENT_ID: `boxing-2026-02-05-event-19`
- EVENT_NAME: `WBA世界ライトヘビー級 ドミトリー・ビボル vs アルトゥール・ベテルビエフ`
- EVENT_DATE: `2026-02-05`
- TARGET_BOUT: `ドミトリー・ビボル vs アルトゥール・ベテルビエフ`

---

## 受け取り後の運用（編集側）

- 受け取ったレコードをそのまま取り込まず、必ず最低検査を実施
  - URL実在性
  - Markdown URL排除
  - `target` 一致確認
- 問題ないレコードのみ `statements[]` へ追記
- `statement_id` は `stmt-<event_id>-###` で採番
- `verification` は既存 `outcome` を根拠に `resolved` 化

---

## 結果記載専用プロンプト（Geminiへそのまま貼る）

```text
あなたは「予測→検証」ログの編集補助です。
目的は、対象イベントについて
1) 観測対象の予測者の「勝者方向の予測」を抽出し、
2) 試合結果（fact）で verification を埋める
ことです。
推測は禁止。出力は必ず JSON 配列のみ（説明文禁止）。

# 対象イベント（編集者が埋める）
- event_id: <EVENT_ID>
- event_name: <EVENT_NAME>
- event_date: <EVENT_DATE>
- target_bout: <TARGET_BOUT>   # 例: 井上尚弥 vs ルイス・ネリ（文字列一致）

# 入力URL（編集者が埋める）
- result_source_urls:
<RESULT_SOURCE_URLS>

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する（日本語記事/動画/SNS、日本国内メディア、日本で活動する発信者を優先）
- 同条件で比較できる場合は海外ソースより国内ソースを優先する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note にその旨を簡潔に残す

# 観測する予測者（CHARTER準拠・必須明記）
- Tier A（常に観測）:
  - 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B（常に観測）:
  - 格闘技を扱う有名YouTuber/配信者/解説系発信者（登録者10万人以上を原則。未満でも影響力が高ければ対象）
- 影響力の判断要素（いずれかを満たせば対象化を検討）:
  - 業界内での参照頻度が高い
  - 主要選手/主要媒体に継続的に引用される
  - 再生規模・反応規模が継続して大きい
  - 格闘技予測の継続発信実績がある
- predictor_name は必ず個人名で記録する（媒体名・編集部名・集合ラベルは禁止）
- 1本の動画で複数人が予測している場合は、人物ごとに別レコードで出力する
- 個人名を特定できない場合のみ speaker.name / predictor_name に "不明" を許容し、source_note に要確認理由を記載する

# 厳守ルール（CHARTER準拠）
- 一次情報に辿れる実在URLのみ使用する（生URL。Markdownリンク禁止）
- 対象試合以外の情報を混ぜない
- 対象は「勝者方向の予測」（誰が勝つ/有利）
- 勝者方向が無い発言は出力しない
- 不明項目は推測で埋めず "不明" を使う
- method は次のいずれかのみ: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明"
- winner は target_bout の2選手名のどちらか（確定できない場合のみ "不明"）
- verification.status は結果が確定した場合のみ "resolved"。未確定は "unresolved"
- verification_date は原則 event_date（結果確定日が別日で確実な場合のみその日付）
- notes/source_note には「どのURLを根拠にしたか」を簡潔に残す

# 出力フォーマット（JSON配列のみ）
[
  {
    "statement_id": "AUTO_ASSIGN_BY_EDITOR",
    "statement_date": "YYYY-MM-DD または 不明",
    "speaker": {
      "name": "個人名（不明なら \"不明\"）",
      "role": "boxer|coach|commentator|youtuber|media|other|不明",
      "affiliation": "不明"
    },
    "content": {
      "raw_text": "短い引用（本人の言い回し優先）",
      "normalized_text": "短い要約（任意）"
    },
    "source": {
      "type": "video|article|sns",
      "url": "一次情報URL（必須）",
      "timestamp": "mm:ss または hh:mm:ss または 不明"
    },
    "prediction": {
      "exists": true,
      "predictor_name": "speaker.name と同一（個人名）",
      "source_url": "source.url と同一",
      "source_ref": "AUTO_ASSIGN_BY_EDITOR",
      "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier A/B 判定メモ。要確認点があれば記載。",
      "expected_winner": "勝者（不明なら \"不明\"）",
      "expected_method": "判定|KO|TKO|不明",
      "target": "<TARGET_BOUT>",
      "expected_outcome": "例: Aが勝利／AがTKO勝ち／不明",
      "deadline": "<EVENT_DATE>"
    },
    "verification": {
      "status": "resolved または unresolved",
      "verification_date": "YYYY-MM-DD または 不明",
      "winner": "勝者名または不明",
      "method": "KO|TKO|判定|DQ|NC|不明",
      "actual_outcome": "事実のみを簡潔に記述",
      "notes": "一次情報URLに基づいて更新。必要なら要確認点を記載",
      "source_note": "根拠URL: <URL,...>"
    }
  }
]
```

### 使い方メモ（最短）

- 1イベントずつ実行する（混在防止）
- `result_source_urls` には公式/主要メディアの一次情報URLだけを貼る
- 返ってきた `outcome_update` を `cards[].bouts[].outcome` へ反映
- 返ってきた `verification_update` を `statements[].verification` へ反映

---

## 実行版（event-01 / そのまま貼り付け）

```text
あなたは「予測→検証」ログの編集補助です。
目的は、対象イベントについて
1) 観測対象の予測者の「勝者方向の予測」を抽出し、
2) 試合結果（fact）で verification を埋める
ことです。
推測は禁止。出力は必ず JSON 配列のみ（説明文禁止）。

# 対象イベント
- event_id: boxing-2022-11-01-event-01
- event_name: WBC・WBO世界ライトフライ級王座統一戦 寺地拳四朗 vs 京口紘人
- event_date: 2022-11-01
- target_bout: 寺地拳四朗 vs 京口紘人

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する（日本語記事/動画/SNS、日本国内メディア、日本で活動する発信者を優先）
- 同条件で比較できる場合は海外ソースより国内ソースを優先する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note にその旨を簡潔に残す

# 収集方針（URLはあなたが探索して特定）
- result_source_urls はあなたが探索し、実在する一次情報URLのみを採用する
- URL は必ず生URLで出力する（Markdownリンク禁止）
- 対象試合と無関係なURLは採用しない

# 観測する予測者（CHARTER準拠・必須明記）
- Tier A（常に観測）:
  - 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B（常に観測）:
  - 格闘技を扱う有名YouTuber/配信者/解説系発信者（登録者10万人以上を原則。未満でも影響力が高ければ対象）
- 影響力の判断要素（いずれかを満たせば対象化を検討）:
  - 業界内での参照頻度が高い
  - 主要選手/主要媒体に継続的に引用される
  - 再生規模・反応規模が継続して大きい
  - 格闘技予測の継続発信実績がある
- predictor_name は必ず個人名で記録する（媒体名・編集部名・集合ラベルは禁止）
- 1本の動画で複数人が予測している場合は、人物ごとに別レコードで出力する
- 個人名を特定できない場合のみ speaker.name / predictor_name に "不明" を許容し、source_note に要確認理由を記載する

# 厳守ルール（CHARTER準拠）
- 一次情報に辿れる実在URLのみ使用する（生URL。Markdownリンク禁止）
- 対象試合以外の情報を混ぜない
- 対象は「勝者方向の予測」（誰が勝つ/有利）
- 勝者方向が無い発言は出力しない
- 不明項目は推測で埋めず "不明" を使う
- method は次のいずれかのみ: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明"
- winner は target_bout の2選手名のどちらか（確定できない場合のみ "不明"）
- verification.status は結果が確定した場合のみ "resolved"。未確定は "unresolved"
- verification_date は原則 event_date（結果確定日が別日で確実な場合のみその日付）
- notes/source_note には「どのURLを根拠にしたか」を簡潔に残す

# 出力フォーマット（JSON配列のみ）
[
  {
    "statement_id": "AUTO_ASSIGN_BY_EDITOR",
    "statement_date": "YYYY-MM-DD または 不明",
    "speaker": {
      "name": "個人名（不明なら \"不明\"）",
      "role": "boxer|coach|commentator|youtuber|media|other|不明",
      "affiliation": "不明"
    },
    "content": {
      "raw_text": "短い引用（本人の言い回し優先）",
      "normalized_text": "短い要約（任意）"
    },
    "source": {
      "type": "video|article|sns",
      "url": "一次情報URL（必須）",
      "timestamp": "mm:ss または hh:mm:ss または 不明"
    },
    "prediction": {
      "exists": true,
      "predictor_name": "speaker.name と同一（個人名）",
      "source_url": "source.url と同一",
      "source_ref": "AUTO_ASSIGN_BY_EDITOR",
      "source_note": "Gemini補助で抽出（確認日：2026-03-19）。Tier A/B 判定メモ。要確認点があれば記載。",
      "expected_winner": "勝者（不明なら \"不明\"）",
      "expected_method": "判定|KO|TKO|不明",
      "target": "寺地拳四朗 vs 京口紘人",
      "expected_outcome": "例: 寺地拳四朗が勝利／寺地拳四朗がTKO勝ち／不明",
      "deadline": "2022-11-01"
    },
    "verification": {
      "status": "resolved または unresolved",
      "verification_date": "YYYY-MM-DD または 不明",
      "winner": "勝者名または不明",
      "method": "KO|TKO|判定|DQ|NC|不明",
      "actual_outcome": "事実のみを簡潔に記述",
      "notes": "一次情報URLに基づいて更新。必要なら要確認点を記載",
      "source_note": "根拠URL: <URL,...>"
    }
  }
]
```

---

## 実行版（event-02 / 影響力基準込み・最低件数指定）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: boxing-2022-12-13-event-02
- event_name: 世界バンタム級4団体王座統一戦 井上尚弥 vs ポール・バトラー
- event_date: 2022-12-13
- timezone: 不明
- target_bout: 井上尚弥 vs ポール・バトラー

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する（日本語記事/動画/SNS、日本国内メディア、日本で活動する発信者を優先）
- 同条件で比較できる場合は海外ソースより国内ソースを優先する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note にその旨を簡潔に残す

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- URLは生URLで出力する（Markdownリンク禁止）
- 対象試合と無関係なURLは採用しない

# 観測する予測者（CHARTER準拠・必須明記）
- Tier A（常に観測）:
  - 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B（常に観測）:
  - 格闘技を扱う有名YouTuber/配信者/解説系発信者（登録者10万人以上を原則。未満でも影響力が高ければ対象）
- 影響力の判断要素（いずれかを満たせば対象化を検討）:
  - 業界内での参照頻度が高い
  - 主要選手/主要媒体に継続的に引用される
  - 再生規模・反応規模が継続して大きい
  - 格闘技予測の継続発信実績がある
- predictor_name は必ず個人名で記録する（媒体名・編集部名・集合ラベルは禁止）
- 1本の動画で複数人が予測している場合は、人物ごとに別レコードで出力する
- 個人名を特定できない場合のみ speaker.name / predictor_name に "不明" を許容し、source_note に要確認理由を記載する

# 件数要件（重要）
- statements は **最低 15 件** を目標に抽出する
- ただし、一次情報で条件を満たす予測が 15 件未満の場合は、無理に捏造せず取得できた件数だけ返す
- 15 件未満の場合は、`charter_update_candidates` に不足理由（一次情報不足/対象者不足など）を記載する

# 抽出ルール（厳守）
- 対象は「勝者方向の予測」（誰が勝つ/有利）
- 勝者方向が無い発言は出力しない
- speaker.name / expected_winner / target が一意に確定できない場合は、推測で埋めない
- `prediction.target` は **`井上尚弥 vs ポール・バトラー` に完全一致**（記号・全角中点・空白まで一致）
- timestamp は分かる場合のみ（不明なら "不明"）
- method は次のいずれかのみ: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明"
- winner は target_bout の2選手名のどちらか（確定できない場合のみ "不明"）
- verification.status は結果が確定した場合のみ "resolved"。未確定は "unresolved"
- verification_date は原則 event_date（結果確定日が別日で確実な場合のみその日付）
- notes/source_note には「どのURLを根拠にしたか」を簡潔に残す
- 1件も無ければ statements は [] を返す
- `statement_id` は `stmt-<event_id>-###` 形式で採番して返す（001開始）
- `prediction.source_ref` は `statement_id=<statement_id>` 形式で返す
- 人名・肩書きの確度が低い場合は断定せず、`source_note` に「要確認（理由）」を明記
- `source.url` / `prediction.source_url` / `verification.source_note` / `charter_update_candidates.evidence_urls` はすべて生URLのみ（Markdown記法禁止）
- Markdownリンクで取得した場合は、生URLへ正規化してから返す
  - 例: `[https://example.com/x](https://example.com/x)` -> `https://example.com/x`
  - 例: `根拠URL: [https://example.com/x](https://example.com/x)` -> `根拠URL: https://example.com/x`
- 正規化後も URL 項目に `[` `]` `(` `)` が残る場合は、そのレコードを出力しない
- 同一人物が同一勝者方向を複数回述べている場合は、**最も明確な1件のみ**を残して重複を除外する

# CHARTER反映候補の収集ルール（Gemini向け）
- 収集対象は「運用ルール化すべき再発パターン」のみ（単発ミスは除く）
- 事実と根拠URLに紐づく候補のみ記載する（推測禁止）
- 候補は 0 件なら charter_update_candidates は [] を返す
- 候補には「問題」「提案ルール」「影響範囲」を短く入れる

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-boxing-2022-12-13-event-02-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": {
        "name": "個人名（不明なら \"不明\"）",
        "role": "boxer|coach|commentator|youtuber|media|other|不明",
        "affiliation": "不明"
      },
      "content": {
        "raw_text": "短い引用（本人の言い回し優先）",
        "normalized_text": "短い要約（任意）"
      },
      "source": {
        "type": "video|article|sns",
        "url": "一次情報URL（必須）",
        "timestamp": "mm:ss または hh:mm:ss または 不明"
      },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.name と同一（個人名）",
        "source_url": "source.url と同一",
        "source_ref": "statement_id=stmt-boxing-2022-12-13-event-02-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier A/B 判定メモ。要確認点があれば記載。",
        "expected_winner": "勝者（不明なら \"不明\"）",
        "expected_method": "判定|KO|TKO|不明",
        "target": "井上尚弥 vs ポール・バトラー",
        "expected_outcome": "例: 井上尚弥が勝利／井上尚弥がKO勝ち／不明",
        "deadline": "2022-12-13"
      },
      "verification": {
        "status": "resolved または unresolved",
        "verification_date": "YYYY-MM-DD または 不明",
        "winner": "勝者名または不明",
        "method": "KO|TKO|判定|DQ|NC|不明",
        "actual_outcome": "事実のみを簡潔に記述",
        "notes": "一次情報URLに基づいて更新。必要なら要確認点を記載",
        "source_note": "根拠URL: https://example.com/a, https://example.com/b"
      }
    }
  ],
  "charter_update_candidates": [
    {
      "title": "短い題名",
      "problem": "再発している運用上の問題を事実ベースで簡潔に記載",
      "proposed_rule": "CHARTERに追記するならこの1文、という形で記載",
      "scope": "prompts|events|verification|naming など",
      "evidence_urls": [
        "https://example.com/a"
      ]
    }
  ]
}
```

---

## 実行版（event-12 / 影響力基準込み・最低件数指定）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: boxing-2025-01-24-event-12
- event_name: 世界スーパーバンタム級4団体防衛戦 井上尚弥 vs サム・グッドマン
- event_date: 2025-01-24
- timezone: 不明
- target_bout: 井上尚弥 vs サム・グッドマン

# 確定結果（正本・編集者が指定した試合結果。verification はこれと矛盾させない）
- winner: 井上尚弥
- method: KO
- round / time: データ上は未確定の場合がある。一次情報（公式記録・主要メディアの試合レポート）で確認できた場合のみ notes / actual_outcome に書く。根拠URLが無い推測は書かない

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する（日本語記事/動画/SNS、日本国内メディア、日本で活動する発信者を優先）
- 同条件で比較できる場合は海外ソースより国内ソースを優先する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note にその旨を簡潔に残す

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- URLは生URLで出力する（Markdownリンク禁止）
- 対象試合と無関係なURLは採用しない

# 観測する予測者（CHARTER準拠・必須明記）
- Tier A（常に観測）:
  - 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B（常に観測）:
  - 格闘技を扱う有名YouTuber/配信者/解説系発信者（登録者10万人以上を原則。未満でも影響力が高ければ対象）
- 影響力の判断要素（いずれかを満たせば対象化を検討）:
  - 業界内での参照頻度が高い
  - 主要選手/主要媒体に継続的に引用される
  - 再生規模・反応規模が継続して大きい
  - 格闘技予測の継続発信実績がある
- predictor_name は必ず個人名で記録する（媒体名・編集部名・集合ラベルは禁止）
- 1本の動画で複数人が予測している場合は、人物ごとに別レコードで出力する
- 個人名を特定できない場合のみ speaker.name / predictor_name に "不明" を許容し、source_note に要確認理由を記載する

# 件数要件（重要）
- statements は **最低 15 件** を目標に抽出する
- ただし、一次情報で条件を満たす予測が 15 件未満の場合は、無理に捏造せず取得できた件数だけ返す
- 15 件未満の場合は、`charter_update_candidates` に不足理由（一次情報不足/対象者不足など）を記載する

# 抽出ルール（厳守）
- 対象は「勝者方向の予測」（誰が勝つ/有利）
- 勝者方向が無い発言は出力しない
- speaker.name / expected_winner / target が一意に確定できない場合は、推測で埋めない
- `prediction.target` は **`井上尚弥 vs サム・グッドマン` に完全一致**（記号・全角中点・空白まで一致）
- timestamp は分かる場合のみ（不明なら "不明"）
- method は次のいずれかのみ: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明"
- winner は target_bout の2選手名のどちらか（確定できない場合のみ "不明"）
- verification.status は結果が確定した場合のみ "resolved"。未確定は "unresolved"
- verification_date は原則 event_date（結果確定日が別日で確実な場合のみその日付）
- verification の winner は **井上尚弥**、method は **KO**（上記「確定結果」と一致）
- verification の `notes` / `actual_outcome` は **事実記述のみ**。「的中」「外れ」「圧勝」「善戦」など評価語・煽り表現は禁止
- ラウンド・スコア等の詳細は **根拠URLがある場合のみ** notes / actual_outcome に書く
- notes/source_note には「どのURLを根拠にしたか」を簡潔に残す
- 1件も無ければ statements は [] を返す
- `statement_id` は `stmt-<event_id>-###` 形式で採番して返す（001開始、欠番なし）
- `prediction.source_ref` は `statement_id=<statement_id>` 形式で返す
- 人名・肩書きの確度が低い場合は断定せず、`source_note` に「要確認（理由）」を明記
- `source.url` / `prediction.source_url` / `verification.source_note` / `charter_update_candidates.evidence_urls` はすべて生URLのみ（Markdown記法禁止）
- Markdownリンクで取得した場合は、生URLへ正規化してから返す
  - 例: `[https://example.com/x](https://example.com/x)` -> `https://example.com/x`
  - 例: `根拠URL: [https://example.com/x](https://example.com/x)` -> `根拠URL: https://example.com/x`
- 正規化後も URL 項目に `[` `]` `(` `)` が残る場合は、そのレコードを出力しない
- 同一人物が同一勝者方向を複数回述べている場合は、**最も明確な1件のみ**を残して重複を除外する

# CHARTER反映候補の収集ルール（Gemini向け）
- 収集対象は「運用ルール化すべき再発パターン」のみ（単発ミスは除く）
- 事実と根拠URLに紐づく候補のみ記載する（推測禁止）
- 候補は 0 件なら charter_update_candidates は [] を返す
- 候補には「問題」「提案ルール」「影響範囲」を短く入れる

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-boxing-2025-01-24-event-12-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": {
        "name": "個人名（不明なら \"不明\"）",
        "role": "boxer|coach|commentator|youtuber|media|other|不明",
        "affiliation": "不明"
      },
      "content": {
        "raw_text": "短い引用（本人の言い回し優先）",
        "normalized_text": "短い要約（任意）"
      },
      "source": {
        "type": "video|article|sns",
        "url": "一次情報URL（必須）",
        "timestamp": "mm:ss または hh:mm:ss または 不明"
      },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.name と同一（個人名）",
        "source_url": "source.url と同一",
        "source_ref": "statement_id=stmt-boxing-2025-01-24-event-12-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier A/B 判定メモ。要確認点があれば記載。",
        "expected_winner": "勝者（不明なら \"不明\"）",
        "expected_method": "判定|KO|TKO|不明",
        "target": "井上尚弥 vs サム・グッドマン",
        "expected_outcome": "例: 井上尚弥が勝利／井上尚弥がKO勝ち／不明",
        "deadline": "2025-01-24"
      },
      "verification": {
        "status": "resolved または unresolved",
        "verification_date": "YYYY-MM-DD または 不明",
        "winner": "井上尚弥",
        "method": "KO",
        "actual_outcome": "事実のみを簡潔に記述（評価語禁止）",
        "notes": "一次情報URLに基づく事実。ラウンド等は根拠URLがある場合のみ",
        "source_note": "根拠URL: https://example.com/a, https://example.com/b"
      }
    }
  ],
  "charter_update_candidates": [
    {
      "title": "短い題名",
      "problem": "再発している運用上の問題を事実ベースで簡潔に記載",
      "proposed_rule": "CHARTERに追記するならこの1文、という形で記載",
      "scope": "prompts|events|verification|naming など",
      "evidence_urls": [
        "https://example.com/a"
      ]
    }
  ]
}
```

---

## 実行版（event-13 / 影響力基準込み・最低件数指定）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: boxing-2025-03-13-event-13
- event_name: WBC世界フライ級 寺地拳四朗 vs ユーリ阿久井政悟
- event_date: 2025-03-13
- timezone: 不明
- target_bout: 寺地拳四朗 vs ユーリ阿久井政悟

# 確定結果（正本・編集者が指定した試合結果。verification はこれと矛盾させない）
- winner: 寺地拳四朗
- method: TKO
- round: 12（データ上の確定値。一次情報で異なる表記がある場合は source_note に根拠URLを添える）
- time: データ上は null の場合がある。一次情報で確認できた場合のみ notes / actual_outcome に書く。根拠URLが無い推測は書かない

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する（日本語記事/動画/SNS、日本国内メディア、日本で活動する発信者を優先）
- **予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する**（記事・テキストのみに偏らない）
- 同条件で比較できる場合は海外ソースより国内ソースを優先する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note にその旨を簡潔に残す

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- **YouTube（youtube.com）を検索対象に必ず含める**。対象試合名・両選手名・開催日のキーワードで動画を横断的に検索する
- URLは生URLで出力する（Markdownリンク禁止）
- 対象試合と無関係なURLは採用しない

# 観測する予測者（CHARTER準拠・必須明記）
- Tier A（常に観測）:
  - 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B（常に観測）:
  - 格闘技を扱う有名YouTuber/配信者/解説系発信者（登録者10万人以上を原則。未満でも影響力が高ければ対象）
- 影響力の判断要素（いずれかを満たせば対象化を検討）:
  - 業界内での参照頻度が高い
  - 主要選手/主要媒体に継続的に引用される
  - 再生規模・反応規模が継続して大きい
  - 格闘技予測の継続発信実績がある
- predictor_name は必ず個人名で記録する（媒体名・編集部名・集合ラベルは禁止）
- 1本の動画で複数人が予測している場合は、人物ごとに別レコードで出力する
- 個人名を特定できない場合のみ speaker.name / predictor_name に "不明" を許容し、source_note に要確認理由を記載する

# 件数要件（重要）
- statements は **最低 15 件** を目標に抽出する
- ただし、一次情報で条件を満たす予測が 15 件未満の場合は、無理に捏造せず取得できた件数だけ返す
- 15 件未満の場合は、`charter_update_candidates` に不足理由（一次情報不足/対象者不足など）を記載する

# 抽出ルール（厳守）
- 対象は「勝者方向の予測」（誰が勝つ/有利）
- 勝者方向が無い発言は出力しない
- speaker.name / expected_winner / target が一意に確定できない場合は、推測で埋めない
- `prediction.target` は **`寺地拳四朗 vs ユーリ阿久井政悟` に完全一致**（記号・全角中点・空白まで一致）
- timestamp は分かる場合のみ（不明なら "不明"）
- method は次のいずれかのみ: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明"
- winner は target_bout の2選手名のどちらか（確定できない場合のみ "不明"）
- verification.status は結果が確定した場合のみ "resolved"。未確定は "unresolved"
- verification_date は原則 event_date（結果確定日が別日で確実な場合のみその日付）
- verification の winner は **寺地拳四朗**、method は **TKO**（上記「確定結果」と一致）
- verification の `notes` / `actual_outcome` は **事実記述のみ**。「的中」「外れ」「圧勝」「善戦」など評価語・煽り表現は禁止
- ラウンド・スコア等の詳細は **根拠URLがある場合のみ** notes / actual_outcome に書く
- notes/source_note には「どのURLを根拠にしたか」を簡潔に残す
- 1件も無ければ statements は [] を返す
- `statement_id` は `stmt-<event_id>-###` 形式で採番して返す（001開始、欠番なし）
- `prediction.source_ref` は `statement_id=<statement_id>` 形式で返す
- 人名・肩書きの確度が低い場合は断定せず、`source_note` に「要確認（理由）」を明記
- `source.url` / `prediction.source_url` / `verification.source_note` / `charter_update_candidates.evidence_urls` はすべて生URLのみ（Markdown記法禁止）
- Markdownリンクで取得した場合は、生URLへ正規化してから返す
  - 例: `[https://example.com/x](https://example.com/x)` -> `https://example.com/x`
  - 例: `根拠URL: [https://example.com/x](https://example.com/x)` -> `根拠URL: https://example.com/x`
- 正規化後も URL 項目に `[` `]` `(` `)` が残る場合は、そのレコードを出力しない
- 同一人物が同一勝者方向を複数回述べている場合は、**最も明確な1件のみ**を残して重複を除外する

# CHARTER反映候補の収集ルール（Gemini向け）
- 収集対象は「運用ルール化すべき再発パターン」のみ（単発ミスは除く）
- 事実と根拠URLに紐づく候補のみ記載する（推測禁止）
- 候補は 0 件なら charter_update_candidates は [] を返す
- 候補には「問題」「提案ルール」「影響範囲」を短く入れる

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-boxing-2025-03-13-event-13-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": {
        "name": "個人名（不明なら \"不明\"）",
        "role": "boxer|coach|commentator|youtuber|media|other|不明",
        "affiliation": "不明"
      },
      "content": {
        "raw_text": "短い引用（本人の言い回し優先）",
        "normalized_text": "短い要約（任意）"
      },
      "source": {
        "type": "video|article|sns",
        "url": "一次情報URL（必須）",
        "timestamp": "mm:ss または hh:mm:ss または 不明"
      },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.name と同一（個人名）",
        "source_url": "source.url と同一",
        "source_ref": "statement_id=stmt-boxing-2025-03-13-event-13-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier A/B 判定メモ。要確認点があれば記載。",
        "expected_winner": "勝者（不明なら \"不明\"）",
        "expected_method": "判定|KO|TKO|不明",
        "target": "寺地拳四朗 vs ユーリ阿久井政悟",
        "expected_outcome": "例: 寺地拳四朗が勝利／寺地拳四朗がTKO勝ち／不明",
        "deadline": "2025-03-13"
      },
      "verification": {
        "status": "resolved または unresolved",
        "verification_date": "YYYY-MM-DD または 不明",
        "winner": "寺地拳四朗",
        "method": "TKO",
        "actual_outcome": "事実のみを簡潔に記述（評価語禁止）",
        "notes": "一次情報URLに基づく事実。ラウンド等は根拠URLがある場合のみ",
        "source_note": "根拠URL: https://example.com/a, https://example.com/b"
      }
    }
  ],
  "charter_update_candidates": [
    {
      "title": "短い題名",
      "problem": "再発している運用上の問題を事実ベースで簡潔に記載",
      "proposed_rule": "CHARTERに追記するならこの1文、という形で記載",
      "scope": "prompts|events|verification|naming など",
      "evidence_urls": [
        "https://example.com/a"
      ]
    }
  ]
}
```

---

## 実行版（event-14 / 影響力基準込み・最低件数指定）

```text
あなたは「予測→検証」ログのための抽出担当です。
推測で埋めないこと。一次情報に基づく内容だけを出力してください。
出力は必ず JSON オブジェクトのみ（説明文禁止）。

# 対象イベント
- event_id: boxing-2025-05-28-event-14
- event_name: WBO世界バンタム級 武居由樹 vs ユッタポン・トンディ
- event_date: 2025-05-28
- timezone: 不明
- target_bout: 武居由樹 vs ユッタポン・トンディ

# 確定結果（正本・編集者が指定した試合結果。verification はこれと矛盾させない）
- winner: 武居由樹
- method: TKO
- round: 1（データ上の確定値。一次情報で異なる表記がある場合は source_note に根拠URLを添える）
- time: データ上は null の場合がある。一次情報（例: 開始から約127秒・2分7秒など）で確認できた場合のみ notes / actual_outcome に書く。根拠URLが無い推測は書かない

# 収集の優先順位（重要）
- 日本国内の予測・一次情報を最優先で収集する（日本語記事/動画/SNS、日本国内メディア、日本で活動する発信者を優先）
- **予測の出所は YouTube・動画配信・解説チャンネル・ポッドキャストを含めて探索する**（記事・テキストのみに偏らない）
- 同条件で比較できる場合は海外ソースより国内ソースを優先する
- 国内だけで件数要件を満たせない場合のみ海外ソースで補完し、source_note にその旨を簡潔に残す

# 収集方針（URLはあなたが探索して特定）
- 一次情報URLを自分で探索し、実在するもののみ採用する
- **YouTube（youtube.com）を検索対象に必ず含める**。対象試合名・両選手名・開催日のキーワードで動画を横断的に検索する
- URLは生URLで出力する（Markdownリンク禁止）
- 対象試合と無関係なURLは採用しない

# 観測する予測者（CHARTER準拠・必須明記）
- Tier A（常に観測）:
  - 当事者性/専門性が高い人物（現役/元トップ選手、主要ジム指導者、著名解説者など）
- Tier B（常に観測）:
  - 格闘技を扱う有名YouTuber/配信者/解説系発信者（登録者10万人以上を原則。未満でも影響力が高ければ対象）
- 影響力の判断要素（いずれかを満たせば対象化を検討）:
  - 業界内での参照頻度が高い
  - 主要選手/主要媒体に継続的に引用される
  - 再生規模・反応規模が継続して大きい
  - 格闘技予測の継続発信実績がある
- predictor_name は必ず個人名で記録する（媒体名・編集部名・集合ラベルは禁止）
- 1本の動画で複数人が予測している場合は、人物ごとに別レコードで出力する
- 個人名を特定できない場合のみ speaker.name / predictor_name に "不明" を許容し、source_note に要確認理由を記載する

# 件数要件（重要）
- statements は **最低 15 件** を目標に抽出する
- ただし、一次情報で条件を満たす予測が 15 件未満の場合は、無理に捏造せず取得できた件数だけ返す
- 15 件未満の場合は、`charter_update_candidates` に不足理由（一次情報不足/対象者不足など）を記載する

# 抽出ルール（厳守）
- 対象は「勝者方向の予測」（誰が勝つ/有利）
- 勝者方向が無い発言は出力しない
- speaker.name / expected_winner / target が一意に確定できない場合は、推測で埋めない
- `prediction.target` は **`武居由樹 vs ユッタポン・トンディ` に完全一致**（記号・中黒・空白まで一致）
- timestamp は分かる場合のみ（不明なら "不明"）
- method は次のいずれかのみ: "KO" | "TKO" | "判定" | "DQ" | "NC" | "不明"
- winner は target_bout の2選手名のどちらか（確定できない場合のみ "不明"）
- verification.status は結果が確定した場合のみ "resolved"。未確定は "unresolved"
- verification_date は原則 event_date（結果確定日が別日で確実な場合のみその日付）
- verification の winner は **武居由樹**、method は **TKO**（上記「確定結果」と一致）
- verification の `notes` / `actual_outcome` は **事実記述のみ**。「的中」「外れ」「圧勝」「善戦」など評価語・煽り表現は禁止
- ラウンド・スコア等の詳細は **根拠URLがある場合のみ** notes / actual_outcome に書く
- notes/source_note には「どのURLを根拠にしたか」を簡潔に残す
- 1件も無ければ statements は [] を返す
- `statement_id` は `stmt-<event_id>-###` 形式で採番して返す（001開始、欠番なし）
- `prediction.source_ref` は `statement_id=<statement_id>` 形式で返す
- 人名・肩書きの確度が低い場合は断定せず、`source_note` に「要確認（理由）」を明記
- `source.url` / `prediction.source_url` / `verification.source_note` / `charter_update_candidates.evidence_urls` はすべて生URLのみ（Markdown記法禁止）
- Markdownリンクで取得した場合は、生URLへ正規化してから返す
  - 例: `[https://example.com/x](https://example.com/x)` -> `https://example.com/x`
  - 例: `根拠URL: [https://example.com/x](https://example.com/x)` -> `根拠URL: https://example.com/x`
- 正規化後も URL 項目に `[` `]` `(` `)` が残る場合は、そのレコードを出力しない
- 同一人物が同一勝者方向を複数回述べている場合は、**最も明確な1件のみ**を残して重複を除外する

# CHARTER反映候補の収集ルール（Gemini向け）
- 収集対象は「運用ルール化すべき再発パターン」のみ（単発ミスは除く）
- 事実と根拠URLに紐づく候補のみ記載する（推測禁止）
- 候補は 0 件なら charter_update_candidates は [] を返す
- 候補には「問題」「提案ルール」「影響範囲」を短く入れる

# 出力フォーマット（JSONオブジェクトのみ）
{
  "statements": [
    {
      "statement_id": "stmt-boxing-2025-05-28-event-14-001",
      "statement_date": "YYYY-MM-DD または 不明",
      "speaker": {
        "name": "個人名（不明なら \"不明\"）",
        "role": "boxer|coach|commentator|youtuber|media|other|不明",
        "affiliation": "不明"
      },
      "content": {
        "raw_text": "短い引用（本人の言い回し優先）",
        "normalized_text": "短い要約（任意）"
      },
      "source": {
        "type": "video|article|sns",
        "url": "一次情報URL（必須）",
        "timestamp": "mm:ss または hh:mm:ss または 不明"
      },
      "prediction": {
        "exists": true,
        "predictor_name": "speaker.name と同一（個人名）",
        "source_url": "source.url と同一",
        "source_ref": "statement_id=stmt-boxing-2025-05-28-event-14-001",
        "source_note": "Gemini補助で抽出（確認日：YYYY-MM-DD）。Tier A/B 判定メモ。要確認点があれば記載。",
        "expected_winner": "勝者（不明なら \"不明\"）",
        "expected_method": "判定|KO|TKO|不明",
        "target": "武居由樹 vs ユッタポン・トンディ",
        "expected_outcome": "例: 武居由樹が勝利／武居由樹がTKO勝ち／不明",
        "deadline": "2025-05-28"
      },
      "verification": {
        "status": "resolved または unresolved",
        "verification_date": "YYYY-MM-DD または 不明",
        "winner": "武居由樹",
        "method": "TKO",
        "actual_outcome": "事実のみを簡潔に記述（評価語禁止）",
        "notes": "一次情報URLに基づく事実。ラウンド等は根拠URLがある場合のみ",
        "source_note": "根拠URL: https://example.com/a, https://example.com/b"
      }
    }
  ],
  "charter_update_candidates": [
    {
      "title": "短い題名",
      "problem": "再発している運用上の問題を事実ベースで簡潔に記載",
      "proposed_rule": "CHARTERに追記するならこの1文、という形で記載",
      "scope": "prompts|events|verification|naming など",
      "evidence_urls": [
        "https://example.com/a"
      ]
    }
  ]
}
```
