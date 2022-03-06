import os
from pathlib import Path

import requests

def save_image(url, path):
    dir = os.path.dirname(path)

    response = requests.get(url)
    response.raise_for_status()

    Path(dir).mkdir(parents=True, exist_ok=True)
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    spacex_api = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    base_path = './images/'

    response = requests.get(spacex_api)
    response.raise_for_status()

    img_urls = response.json()['links']['flickr']['original']

    for i, link in enumerate(img_urls):
        img_path = f'{base_path}image_spacex_{i}.jpeg'
        save_image(link, img_path)