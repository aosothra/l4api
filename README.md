# Telegram Astro BOT 

This script utilizes avaliable free sources of space photography and uses Telegram Bot to post these images randomly on the specified channel.

Currently used API sources:

[{Nasa APIs}](https://api.nasa.gov/)

[SpaceX-API](https://github.com/r-spacex/SpaceX-API)

### Installation guidelines


You must have Python3 installed on your system.
You may use `pip` (or `pip3` to avoid conflict with Python2) to install dependencies.
```
pip install -r requirements.txt
```
It is strongly advised to use [virtualenv/venv](https://docs.python.org/3/library/venv.html) for project isolation.

This script uses `.env` file in root folder to store variables neccessary for operation. So, do not forget to create one!

Below you can find how contents of your `.env` file should look like, and 

```
NASA_API_KEY = 'yourapikeyhere'
TELEGRAM_BOT_TOKEN = '1234567890:yourbotauthtokenhere'
TELEGRAM_CHANNEL_ID = '@your_channel_name'
TIME_DELAY_SECONDS = 86400
```

`NASA_API_KEY` is required for fetching from NASA Api endpoints ([get it here](https://api.nasa.gov/)).

`TELEGRAM_BOT_TOKEN` is your Telegram Bot authentication token. If you do not have one already, you need to crate a bot and acquire the auth token. (Find more about it on [Bots: An introduction for developers](https://core.telegram.org/bots))

`TELEGRAM_CHANNEL_ID` refers to identifier of your telegram channel, where bot is supposed to post the images. Make sure that your bot is invited to your channel and has admin rights neccessary for posting messages.

`TIME_DELAY_SECONDS` controls the time frame between each single post. Keep in mind that value is specified in seconds.


### Basic usage (for the lack of any other...)

```
py main.py 
```

You can find fetched images in `./images/` folder. Images are fetched in bulk and deleted after posting. Once the script runs out of images to post, bulk fetch happens again. 

### Project goals

This project was created for educational purposes as part of [dvmn.org](https://dvmn.org/) Backend Developer course.