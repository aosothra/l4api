import datetime
import os
from urllib.parse import urlsplit

import requests

from fetch_image import fetch_image, save_image


def get_file_extension(url):
    path = urlsplit(url).path
    return os.path.splitext(path)[1]


def fetch_nasa_apod(api_key, img_count=30):
    apod_api = 'https://api.nasa.gov/planetary/apod'

    payload = {
        'count': img_count,
        'api_key': api_key
    }

    response = requests.get(apod_api, params=payload)
    response.raise_for_status()

    apods = response.json()
    for i, apod in enumerate(apods):
        if apod['media_type'] == 'image':
            ext = get_file_extension(apod['url'])
            img_name = f'image_apod_{i}{ext}'
            img_data = fetch_image(apod['url'])
            save_image(img_name, img_data)


def fetch_nasa_epic_image(api_key, img_name, date, index):
    formated_date = date.strftime('%Y/%m/%d')

    url = (
        f'https://api.nasa.gov/EPIC/archive/natural/'
        f'{formated_date}/png/{img_name}.png'
        )

    payload = {
        'api_key': api_key
    }

    img_name = f'image_epic_{index}.png'
    img_data = fetch_image(url, payload=payload)
    save_image(img_name, img_data)


def fetch_nasa_epic_imgset(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'

    payload = {
        'api_key': api_key
    }

    response = requests.get(url, params=payload)
    response.raise_for_status()

    epics = response.json()
    for i, epic in enumerate(epics):
        img_name = epic['image']
        img_date = datetime.datetime.fromisoformat(epic['date'])
        fetch_nasa_epic_image(api_key, img_name, img_date, i)
