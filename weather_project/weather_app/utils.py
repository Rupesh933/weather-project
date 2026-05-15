import requests
from django.conf import settings

def get_weather(city_name):
    # Fetch current weather data from OpenWeatherMap API.
    # Returns parsed JSON on success, None on failure.

    api_key = settings.OPENWEATHER_API_KEY  # This comes from your .env via settings.py
    if not api_key:
        raise ValueError('OPENWEATHER_API_KEY is not set in environment')
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q' : city_name,
        'appid' : api_key,
        'units' : 'metric'
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json()
        else:
            # you have log the error: response.status_code, response.text
            return None
    except requests.exceptions.RequestException:
        return None
