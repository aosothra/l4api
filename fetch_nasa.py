import datetime
import os
from urllib.parse import urlsplit

import requests

from fetch_image import fetch_image


def get_file_extension(url):
    path = urlsplit(url).path
    return os.path.splitext(path)[1]


def fetch_nasa_apod(api_key, img_count=30):
    apod_api = 'https://api.nasa.gov/planetary/apod'
    base_path = './images/'

    payload = {
        'count':img_count,
        'api_key':api_key
    }

    response = requests.get(apod_api, params=payload)
    response.raise_for_status()

    apod_list = response.json()
    for i, apod in enumerate(apod_list):
        if apod['media_type']=='image':
            ext = get_file_extension(apod['url'])
            img_name = f'image_apod_{i}{ext}'
            fetch_image(apod['url'], img_name)


def fetch_nasa_epic_image(api_key, img_name, date, index):
    formated_date = date.strftime('%Y/%m/%d') 
    url = f'https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{img_name}.png'
    base_path = './images/'

    payload = {
        'api_key':api_key
    }

    img_name = f'image_epic_{index}.png'
    fetch_image(url, img_name, payload=payload)


def fetch_nasa_epic_imgset(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'

    payload = {
        'api_key':api_key
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    epic_list = response.json()
    for i, epic in enumerate(epic_list):
        img_name = epic['image']
        img_date = datetime.datetime.fromisoformat(epic['date'])
        fetch_nasa_epic_image(api_key, img_name, img_date, i)