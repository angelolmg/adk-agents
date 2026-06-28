def get_weather(city: str) -> str:
    """
    Returns the weather for a city.
    """

    fake_weather = {
        "Natal": "29°C and sunny",
        "São Paulo": "18°C and cloudy",
        "Rio de Janeiro": "31°C and partly cloudy",
    }

    return fake_weather.get(city, "Weather data unavailable.")