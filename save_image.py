import os
from pathlib import Path

import requests


def save_image(url, path, payload={}):
    dir = os.path.dirname(path)

    response = requests.get(url, params=payload)
    response.raise_for_status()

    Path(dir).mkdir(parents=True, exist_ok=True)
    with open(path, 'wb') as file:
        file.write(response.content)