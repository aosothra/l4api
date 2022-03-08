import os
from pathlib import Path

import requests

from fetch_image import fetch_image, save_image


def fetch_spacex_last_launch():
    spacex_api = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'

    response = requests.get(spacex_api)
    response.raise_for_status()

    img_urls = response.json()['links']['flickr']['original']

    for i, link in enumerate(img_urls):
        img_name = f'image_spacex_{i}.jpeg'
        img_data = fetch_image(link)
        save_image(img_name, img_data)