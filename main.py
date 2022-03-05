import datetime
import os
from pathlib import Path
from urllib.parse import urlsplit

import requests
import telegram
from dotenv import load_dotenv


def get_file_extension(url):
    path = urlsplit(url).path
    return os.path.splitext(path)[1]


def save_image(url, path, payload={}):
    dir = os.path.dirname(path)

    response = requests.get(url, params=payload)

    response.raise_for_status()


    Path(dir).mkdir(parents=True, exist_ok=True)
    with open(path, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch():
    spacex_api = 'https://api.spacexdata.com/v5/launches/5eb87d42ffd86e000604b384'
    base_path = './images/spacex/'

    response = requests.get(spacex_api)
    response.raise_for_status()

    img_urls = response.json()['links']['flickr']['original']

    for i, link in enumerate(img_urls):
        img_path = f'{base_path}image{i}.jpeg'
        save_image(link, img_path)


def fetch_nasa_apod(api_key, img_count=30):
    apod_api = 'https://api.nasa.gov/planetary/apod'
    base_path = './images/apod/'

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
            img_path = f'{base_path}image{i}{ext}'
            save_image(apod['url'], img_path)


def fetch_nasa_epic_image(api_key, img_name, date, index):
    formated_date = date.strftime('%Y/%m/%d') 
    url = f'https://api.nasa.gov/EPIC/archive/natural/{formated_date}/png/{img_name}.png'
    base_path = './images/epic/'

    payload = {
        'api_key':api_key
    }

    img_path = f'{base_path}image{index}.png'
    save_image(url, img_path, payload=payload)


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


def fetch_bulk(api_key):
    fetch_spacex_last_launch()
    fetch_nasa_apod(api_key)
    fetch_nasa_epic_imgset(api_key)

def publish_text(bot, channel, message):
    bot.send_message(chat_id=channel, text=message)


def main():
    load_dotenv()
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
    nasa_api_key = os.getenv('NASA_API_KEY')


    bot = telegram.Bot(telegram_token)
    publish_text(bot, channel_id, 'Hello Channel!')

if __name__ == '__main__':
    main()