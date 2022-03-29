import os
import re
from youtube_dl import YoutubeDL

import datetime
import motor.motor_asyncio
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

class Config:
    APP_ID = int(os.environ.get("APP_ID", ""))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    START_MSG = os.environ.get("START_MSG", "<b>Hi {},\nIam A Simple Youtube to Mp3 Downloader Bot,</b>\n\nSend me Any Songs name with /song command")
    OWNER = os.environ.get("OWNER", "shamilhabeeb")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    BOT_USERNAME = os.environ.get("BOT_USERNAME")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    GROUP_SUPPORT = os.environ.get("GROUP_SUPPORT", "Repo")
    GONDERME_TURU = os.environ.get("GONDERME_TURU", False)
    OWNER_ID = int(os.environ.get("OWNER_ID"))
    LANGAUGE = os.environ.get("LANGAUGE", "AZ")
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/")
    msg = {}
