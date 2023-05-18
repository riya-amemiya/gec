# Guidance Extension for ChatGPT

Guidance Extension for ChatGPT(GEC)は、[ChatGPT](https://chat.openai.com/)をAPI経由で安全かつより高度に利用するための拡張アプリです。

(個人用に作ってるので、まだまだ未完成です。)

## 事前準備

`.env`ファイルを作成し、以下のように環境変数を設定してください。

```env
OPENAI_API_KEY=xxxxxxx
```

`OPENAI_API_KEY`は、[OpenAIのダッシュボード](https://platform.openai.com/account/api-keys)から取得できます。

### ローカルで実行する

```bash
python src/main.py
```

### 特殊コマンド

- exit: チャットを終了します。
- save: チャットのログを保存します。
- read: ask.txtに保存されたプロンプトを読み込みます。(長い時とかに便利)
- load: チャットのログを読み込みます。
- nowData: 現在のチャットのログを表示します。

## ライセンス

MIT
