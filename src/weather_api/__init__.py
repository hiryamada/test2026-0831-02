import random

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(title="天気予報API")

WEATHERS = ("晴れ", "曇り", "雨")
TEMPERATURES = tuple(range(15, 31))


@app.get("/weather/{region}", response_class=PlainTextResponse)
def get_weather(region: str) -> str:
    """指定地域のサンプル天気予報を返す。"""
    weather = random.choice(WEATHERS)
    temperature = random.choice(TEMPERATURES)
    return f"{region}: {weather}、最高気温{temperature}℃"


def main() -> None:
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)

# 入力された整数が素数か
