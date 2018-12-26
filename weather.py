import os
import pytz
import math
import requests

from datetime import datetime

API_KEY = os.environ.get('API_KEY')
API_URL = (
    'http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}'
)


def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None

    return data
