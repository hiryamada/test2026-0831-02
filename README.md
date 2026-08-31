# 天気予報API

地域名を受け取り、ランダムに生成したサンプル天気予報を返す FastAPI アプリケーションです。

## 必要条件

- Python 3.12 以上
- [uv](https://docs.astral.sh/uv/)

## セットアップ

```bash
uv sync
```

## 起動

```bash
uv run weather-api
```

起動後、例えば東京の予報は次の URL で取得できます。

```text
http://127.0.0.1:8000/weather/東京
```

レスポンス例:

```text
東京: 晴れ、最高気温25℃
```

天気と最高気温はアクセスのたびにランダムに生成されます。

## テスト

```bash
uv run pytest
```