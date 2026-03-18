# 格闘技トップの課題点

入口「トップ → 格闘技ログ」は確定済み。本ドキュメントは **格闘技トップ**（`martial-arts/index.html`）およびその直下の団体ページの課題を、実ファイルを根拠に列挙する。PROJECT_CHARTER 9.5「格闘技のUI/UX最低限（event/logs/格闘技トップの見た目と導線を揃える）」の整理用。

---

## 1. データとの不整合（THE MATCH の欠落）

| 根拠 | 内容 |
|------|------|
| `data/index.json` | イベントの `organization` は **"RIZIN"** と **"THE MATCH"** の2種類が存在する（the-match-2022.json が THE MATCH）。 |
| `martial-arts/index.html` | クリック可能な団体は **RIZIN のみ**。「その他の団体（準備中）」は UFC / BOXING / ONE Championship / K-1 の4つのみ。**THE MATCH の入口がどこにもない。** |

- 格闘技トップからは「RIZIN」か「ログ一覧へ」でしかイベントに進めない。THE MATCH 2022 は `logs.html`（全件一覧）や `event.html?file=the-match-2022.json` の直接URLでは到達可能だが、**格闘技トップ上に「THE MATCH」としての導線がない**。

---

## 2. 団体ページの役割と RIZIN 特例

| 根拠 | 内容 |
|------|------|
| `martial-arts/rizin.html` | `data/index.json` を fetch し、`organization === "RIZIN"` でフィルタしてイベント一覧・最新1件を表示。event.html へのリンクを生成している。 |
| `martial-arts/` 配下 | 実ファイルは `index.html` / `rizin.html` / `README.md` のみ。**THE MATCH 用の団体ページ（例: the-match.html）は存在しない。** |

- 団体別「トップ」は現状 RIZIN 用のみ実装されている。THE MATCH を格闘技トップから選べるようにするには、格闘技トップに THE MATCH 用カードを追加するか、団体ページを追加する必要がある。

---

## 3. 導線の役割分担

| 経路 | 実装 | 備考 |
|------|------|------|
| 格闘技トップ → RIZIN | `martial-arts/index.html` のカード → `rizin.html` | RIZIN のみ団体別一覧あり。 |
| 格闘技トップ → ログ一覧 | 同「ログ一覧へ」→ `logs.html` | `logs.html` は `data/index.json` を**全件**表示するため、RIZIN も THE MATCH も出る。 |
| 格闘技トップ → THE MATCH | **なし** | 格闘技トップに THE MATCH のカード・リンクがない。 |

- 「全イベントを見る」は logs.html で可能。「団体ごとに見る」は RIZIN のみ可能で、THE MATCH は格闘技トップからは選べない。

---

## 4. 拡張性（静的と動的の差）

| 根拠 | 内容 |
|------|------|
| `martial-arts/index.html` | 団体カードは **静的HTML**（RIZIN + 準備中4団体）。`data/index.json` の `organization` を読んで団体一覧を動的生成していない。 |
| `data/index.json` | 団体は `events[].organization` で持っている。ここに新団体を足しても、格闘技トップの表示は自動では変わらない。 |

- 新団体（例: UFC）を index.json に追加しても、格闘技トップにカードを**手動で**追加する必要がある。index.json を正本として「団体一覧を動的に出す」仕組みは格闘技トップにはない。

---

## 5. 見た目・文言の揃え

| 箇所 | 現状（実ファイル上の表記） |
|------|----------------------------|
| 格闘技トップ | タイトル「格闘技ログ」、説明「団体ごとのイベントログを参照できます」。セクション「主要団体」「その他の団体（準備中）」「ナビゲーション」。 |
| RIZIN ページ | タイトル「RIZINログ」、説明「RIZINのイベントログ一覧」。セクション「概要」「イベント数」「最新イベント」「イベント一覧」「ナビゲーション」。 |
| ログ一覧 | タイトル「ログ一覧」、説明「すべてのイベントログ」。的中率ランキング + イベント一覧。 |
| event.html | タイトル「イベント詳細」、説明「イベントの試合カード / 発言・予測と検証」。 |

- ナビは「トップ」「格闘技ログ」「ログ一覧」で共通。ページごとの説明文・セクション名は統一されていない（「ログ」「イベントログ」の混在など）。

---

## 6. まとめ：後続で決めるとよいこと

1. **THE MATCH の扱い**  
   data/index.json に THE MATCH が存在するため、格闘技トップに「THE MATCH」の入口を設けるか（カード追加 or 団体ページ追加）、または「ログ一覧で全団体見せる」方針で格闘技トップは RIZIN のみにしておくかを決める。

2. **団体一覧のデータ駆動化**  
   index.json の `organization` のユニーク一覧を元に、格闘技トップの団体カードを動的生成するか。すると新団体追加時は index.json のみ更新すればよくなる。

3. **「準備中」団体の扱い**  
   UFC / BOXING / ONE / K-1 は現状データにない。格闘技トップに表示し続けるか、データに存在する団体だけ表示するか。

4. **見た目・文言の統一**  
   「ログ」「イベントログ」「イベント一覧」などの用語と、各ページの説明文・セクション構成を、event / logs / 格闘技トップで揃えるか。

---

*出典：martial-arts/index.html, martial-arts/rizin.html, data/index.json, logs.html, event.html を実ファイルとして参照。*
