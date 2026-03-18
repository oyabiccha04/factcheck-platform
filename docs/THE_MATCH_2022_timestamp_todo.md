# THE MATCH 2022 — 一次情報URL＋タイムスタンプ埋め（作業用）

PROJECT_CHARTER.md 1.3.2 / 1.3.3 に従い、予測のソース（一次情報）に **URL＋必要ならタイムスタンプ** を記載する。  
ソース不明は推測で埋めず「不明」のまま。**一次情報に基づいて判明した場合のみ**ここで更新する。

---

## 現状：`source.timestamp` が「不明」の statement 一覧

取得したタイムスタンプを「取得値」列にメモし、確定したら `data/events/the-match-2022.json` の該当 `source.timestamp` と `prediction.source_note` を更新する。

### 記事（SPREAD）— 4件

| statement_id | 発言者 | URL | 取得値 |
|--------------|--------|-----|--------|
| stmt-the-match-2022-003 | 堀口恭司 | https://spread-sports.jp/archives/116734/5 | 不明（記事内に記載なし） |
| stmt-the-match-2022-004 | 青木真也 | https://spread-sports.jp/archives/116734/14 | 不明（記事内に記載なし） |
| stmt-the-match-2022-007 | 久保賢司 | https://spread-sports.jp/archives/116734/7 | 不明（記事内に記載なし） |
| stmt-the-match-2022-008 | 魔裟斗 | https://spread-sports.jp/archives/116734/12 | 不明（記事内に記載なし） |

### 動画（YouTube）— 9件（Gemini等で取得可）※2026-03-18 取得済み・JSON反映済み

| statement_id | 発言者 | 動画URL | 取得値（例: 12:34〜） |
|--------------|--------|---------|------------------------|
| stmt-the-match-2022-009 | 朝倉未来 | https://www.youtube.com/watch?v=mRSODsjDvc4 | 4:24〜 |
| stmt-the-match-2022-010 | 平本蓮 | https://www.youtube.com/watch?v=tPEfoTpKst8 | 4:18〜 |
| stmt-the-match-2022-011 | 堀口恭司 | https://www.youtube.com/watch?v=M7j6TkJhUr0 | 1:55〜 |
| stmt-the-match-2022-012 | 朝倉海 | https://www.youtube.com/watch?v=M7j6TkJhUr0 | 3:10〜 |
| stmt-the-match-2022-013 | 京口紘人 | https://www.youtube.com/watch?v=M7j6TkJhUr0 | 4:12〜 |
| stmt-the-match-2022-014 | 矢地祐介 | https://www.youtube.com/watch?v=M7j6TkJhUr0 | 7:45〜 |
| stmt-the-match-2022-015 | 小比類巻貴之 | https://www.youtube.com/watch?v=M7j6TkJhUr0 | 11:25〜 |
| stmt-the-match-2022-016 | 安保瑠輝也 | https://www.youtube.com/watch?v=QFrXrJ9_bNc | 4:58〜 |
| stmt-the-match-2022-017 | 青木真也 | https://www.youtube.com/watch?v=QFrXrJ9_bNc | 11:13〜 |

※ 011〜015 は同一動画（M7j6TkJhUr0）、016・017 は同一動画（QFrXrJ9_bNc）。発言者ごとの該当箇所タイムスタンプを分けて取得するとよい。

---

## 更新時のルール（DEVELOPMENT_GUIDELINES 厳守）

- **推測で補完しない**。一次情報（動画の該当箇所・記事の該当記述）で確認できた場合のみ記載。
- 更新するフィールド：
  - `statements[].source.timestamp` … 例: `"動画 12:34〜"` または `"7:21〜（記事内記載）"`
  - `statements[].prediction.source_note` … 既存メモにタイムスタンプを追記してよい（例: 「…。動画 12:34〜」）。
- 記事は「○分○秒〜」が記事内に書いてあればそれを、なければ「不明」のまま。
