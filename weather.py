import requests

def get_weather_info(key, location):
    req = requests.get('http://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=2'.format(key, location))

    return req.json()
