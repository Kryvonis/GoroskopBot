import requests

from app.settings import Config


def get_weather(city, country):
    params = f'?lat={city}&lon={country}&APPID={Config.WEATHER_APP_ID}'
    request_url = f'{Config.WEATHER_URL}{params}'
    response = requests.get(request_url)
    return response


def get_city(lat, lng):
    params = f'json?latlng={lat},{lng}&key={Config.GOOGLE_API_KEY}'
    request_url = f'{Config.GOOGLE_URL}{params}'
    return requests.get(request_url)


def convert_weather(weather_dict):
    return {
        "main": weather_dict['weather'][0]['main'],
        "description": weather_dict['weather'][0]['description'],
    }
