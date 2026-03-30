# Factcheck Platform
### 検証可能な「発言ログ」を残すためのアーカイブ

---

## このサイトは何か

このサイトは、  
**誰かの発言・予測・主張を「評価せずに記録する」ためのログアーカイブ**です。

政治家、評論家、YouTuber、格闘技関係者などが  
「いつ・何を言ったか」  
そして  
「その後、何が起きたか」

を、**後から検証可能な形で保存すること**だけを目的としています。

意見・賛否・当たり外れ・評価は一切行いません。

---

## 基本思想（Principles）

- 人ではなく **発言（statement）** を主語とする
- 発言時点の内容と、後から判明した結果を分離する
- 後出し修正が分かる構造を保つ
- GitHub の commit 履歴も検証対象とする
- 「正しい／間違い」ではなく  
  **「何が言われ、何が起きたか」だけを残す**

---

## このサイトが「しないこと」

- 発言の評価・採点・ランキング
- 意見・批評・感想の掲載
- 当たり外れの断定
- 編集者による解釈の付加

このサイトは「答え」を出しません。  
**判断は常に閲覧者に委ねられます。**

---

## 技術的な前提（最小限）

- GitHub Pages による静的サイト
- 1イベント = 1 JSON ファイル
- JSON は差分更新せず、必ず全文更新
- 構造変更は commit 履歴で追跡可能
- 表示ロジックとデータ構造を分離

---

## 開発ドキュメント・サイト構造（運用者向け）

- **前提・憲法**：リポジトリ直下の [PROJECT_CHARTER.md](PROJECT_CHARTER.md)（インデックス正本、種目別ランキングの扱い、ナビ方針など）
- **開発判断**： [docs/DEVELOPMENT_GUIDELINES.md](docs/DEVELOPMENT_GUIDELINES.md)

**予測者ハブ（グローバルナビの「MMA予測 / ボクシング予測 / キック予測」先）**

| 表示名 | ファイル |
|--------|-----------|
| MMA予測 | `martial-arts/predictors.html` |
| ボクシング予測 | `predictors.html` |
| キック予測 | `kick-predictors.html` |

ログ一覧（`logs.html` / `martial-arts/logs.html`）はナビの直接項目ではなく、各ページ内の導線から遷移する。

生JSON・GitHub 等の**検証用リンク**はトップからは外し、[`verify.html`](verify.html) にまとめています。

**閲覧者向けの説明・利用条件**

| ファイル | 内容 |
|----------|------|
| [`about.html`](about.html) | サイトのねらい・記録のルール・方針（平易な説明） |
| [`policy.html`](policy.html) | 編集の独立性、データの第三者利用（クレジット等）、免責 |

---

## なぜ GitHub を使うのか

GitHub は単なるホスティングではありません。

- **いつ、誰が、何を変更したか**が残る
- データの**改変経路を追いやすく**し、公開ログの**検証可能性を高める**助けになる（外部出典 URL の恒久的な有効性や「絶対の真実」を保証するものではない）
- 不当な「消し去り」に対して、履歴を通じた説明責任を高められる

このサイトでは  
**GitHub の履歴自体が検証性の一部**です（出典リンクの枯れについては <a href="./PROJECT_CHARTER.md">PROJECT_CHARTER.md</a> の「出典の検証可能性とリンク枯れ」を参照）。

---

## ステータス

- このサイトは発展途上です
- 表示やUIは今後変更される可能性があります
- ただし、**過去ログの意味や文脈が壊れる変更は行いません**

---

## GitHub に公開する

### 1. Git の準備

- [Git for Windows](https://git-scm.com/download/win) などで Git をインストールし、ターミナルで `git --version` が動くことを確認する。

### 2. GitHub でリポジトリを作る

1. [GitHub](https://github.com) にログインし、**New repository** で新規リポジトリを作成する。
2. リポジトリ名は任意（例: `factcheck-platform`）。**Public** を選ぶ。
3. **Initialize this repository with a README** は**チェックしない**（既にローカルに README があるため）。

### 3. ローカルで Git を初期化してプッシュする

プロジェクトのフォルダで、次のコマンドを順に実行する。

```bash
cd "プロジェクトのパス（factcheck-platform-main があるフォルダ）"

git init
git add .
git commit -m "Initial commit: factcheck platform with martial-arts logs"
git branch -M main
git remote add origin https://github.com/あなたのユーザー名/リポジトリ名.git
git push -u origin main
```

`あなたのユーザー名` と `リポジトリ名` は、手順 2 で作ったリポジトリの URL に合わせて書き換える。

### 4. GitHub Pages で公開する（任意）

- リポジトリの **Settings** → **Pages** を開く。
- **Source** で **Deploy from a branch** を選び、**Branch** を `main`、**Folder** を `/ (root)` にし、**Save** する。
- 数分後、`https://あなたのユーザー名.github.io/リポジトリ名/` でサイトが表示される。  
  （トップは `index.html` がルートにあるので、リポジトリ名が付く場合は `https://あなたのユーザー名.github.io/リポジトリ名/index.html` や `../index.html` のリンクが正しく動くか確認する。）

### 既にリポジトリがある場合：変更を Git に反映してプッシュする

初回セットアップではなく、**日々の修正を GitHub に載せる**ときの手順は、リポジトリ直下の [**AGENTS.md**](AGENTS.md) にまとめてある（`git add` → `commit` → `push`）。

---

## 最後に

このプロジェクトは  
「正しさ」を主張するためのものではありません。

**記録が残ること**  
**検証できること**  
それ自体に価値があると考えています。
