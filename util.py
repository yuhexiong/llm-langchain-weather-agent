import requests


def get_weather(city: str) -> str:
    """
    查詢指定城市的天氣資訊
    """

    response = requests.get(f"https://wttr.in/{city}?format=%C+%t")
    return response.text
