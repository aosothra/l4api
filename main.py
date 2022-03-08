import os
import random
import time
from pathlib import Path

import telegram
from dotenv import load_dotenv

from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic_imgset
from fetch_spacex import fetch_spacex_last_launch


def get_random_img_name():
    files = os.listdir('./images/')
    return random.choice(files)


def is_imgset_empty():
    if Path('./images/').exists():
        return os.listdir('./images/')
    else:
        return False


def fetch_bulk(api_key):
    fetch_spacex_last_launch()
    fetch_nasa_apod(api_key)
    fetch_nasa_epic_imgset(api_key)


def main():
    load_dotenv()
    nasa_api_key = os.getenv('NASA_API_KEY')
    telegram_token = os.getenv('TELEGRAM_BOT_TOKEN')
    channel_id = os.getenv('TELEGRAM_CHANNEL_ID')
    time_delay = os.getenv('TIME_DELAY_SECONDS')
    if time_delay is None:
        time_delay = 86400
    bot = telegram.Bot(telegram_token)

    while True:
        if is_imgset_empty():
            fetch_bulk(nasa_api_key)

        img_path = f'./images/{get_random_img_name()}'
        bot.send_photo(chat_id=channel_id, photo=open(img_path, 'rb'))

        os.remove(img_path)

        time.sleep(int(time_delay))


if __name__ == '__main__':
    main()