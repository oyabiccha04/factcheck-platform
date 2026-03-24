# エージェント／開発メモ

## Git に反映してリモートへ送る（デプロイ前の定番）

**`git push` だけではローカルの未コミット変更は送られません。**  
「Everything up-to-date」と出たら、`add` / `commit` がまだの可能性が高いです。

### 手順（この順で実行）

1. リポジトリのルートへ移動する（本リポジトリなら `factcheck-platform-main`）。
2. 変更をステージする。
3. コミットする。
4. リモートへプッシュする。

### コマンド例（変更をすべてコミットする場合）

```bash
git add -A

git commit -m "変更内容の一言（例: 予測ハブのUI調整）"

git push origin main
```

ブランチが `main` でない場合は、次で確認してから `main` を置き換える。

```bash
git branch
```

### コマンド例（特定ファイルだけコミットする場合）

```bash
git add path/to/file.html

git commit -m "メッセージ"

git push origin main
```

### PowerShell でも同じ

パスに日本語が含まれる場合は、リポジトリを `cd` してから上記と同様に実行できる。

---

運用ルールの正本は `PROJECT_CHARTER.md`、開発の細目は `docs/DEVELOPMENT_GUIDELINES.md` を参照。
