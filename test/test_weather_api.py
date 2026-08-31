from fastapi.testclient import TestClient

from weather_api import app


def test_get_weather_returns_forecast_for_region(monkeypatch) -> None:
    choices = iter(("晴れ", 25))
    monkeypatch.setattr("weather_api.random.choice", lambda _: next(choices))

    response = TestClient(app).get("/weather/東京")

    assert response.status_code == 200
    assert response.headers["content-type"] == "text/plain; charset=utf-8"
    assert response.text == "東京: 晴れ、最高気温25℃"

