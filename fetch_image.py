import requests


def fetch_image(url, payload={}):
    response = requests.get(url, params=payload)
    response.raise_for_status()

    return response.content


def save_image(img_name, bytes):
    with open(f'./images/{img_name}', 'wb') as file:
        file.write(bytes)
