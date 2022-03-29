import os
import re
from youtube_dl import YoutubeDL

class Config:
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Simple Youtube to Mp3 Downloader Bot,</b>\n\nSend me Any Songs name with /song command")
    OWNER = os.environ.get("OWNER", "shamilhabeeb")
    PLAYLIST_ID = int(os.environ.get("PLAYLIST_ID"))
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
