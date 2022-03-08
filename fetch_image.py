from pathlib import Path

import requests


def fetch_image(url, payload={}):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.content


def save_image(img_name, bytes):
    base_path = './images/'
    Path(base_path).mkdir(parents=True, exist_ok=True)
    with open(f'{base_path}{img_name}', 'wb') as file:
        file.write(bytes)
