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
