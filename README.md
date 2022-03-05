# Telegram Astro BOT 

**This project is under development!** Current functionality is limited to image fetching from avaliable API sources.

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

In order to access NASA API endpoints, you'll need an `api_key` ([get it here](https://api.nasa.gov/))

This script uses `.env` file in root folder to store the `api_key`. So, do not forget to create one!

Here is how contents of your `.env` file should look like:
```
NASA_API_KEY='putyourapikeyhere'
```


### Basic usage (for the lack of any other...)

```
py main.py 
```

You can find fetched images in `./images/` folder

### Project goals

This project was created for educational purposes as part of [dvmn.org](https://dvmn.org/) Backend Developer course.