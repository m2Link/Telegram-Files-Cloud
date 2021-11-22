#!/usr/bin/env python3
# This is bot coded by Abhijith N T and used for educational purposes only
# https://github.com/AbhijithNT
# Copyright ABHIJITH N T
# Thank you https://github.com/pyrogram/pyrogram

import os
import logging

logging.basicConfig(level=logging.INFO,
                    handlers=[logging.FileHandler(
                        'log.txt'), logging.StreamHandler()],
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                    )
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

ENV = bool(os.environ.get('ENV', False))
try:
    if ENV:
        AUTH_USER = []
        BOT_TOKEN = os.environ.get('BOT_TOKEN')
        APP_ID = os.environ.get('APP_ID')
        API_HASH = os.environ.get('API_HASH')
        BOT_USE = bool(os.environ.get('BOT_USE', False))
        GET_AUTH_USER = os.environ.get('AUTH_USER')
        for i in GET_AUTH_USER.split(','):
            AUTH_USER.append(int(i))
    else:
        from sample_config import Config

        BOT_TOKEN = Config.BOT_TOKEN
        APP_ID = Config.APP_ID
        API_HASH = Config.API_HASH
        BOT_USE = Config.BOT_USE
        AUTH_USER = Config.AUTH_USERS
except KeyError:
    LOGGER.error('One or more configuration values are missing exiting now.')
    exit(1)


class Msg:
    source = "\nsource: https://github.com/AbhijithNT/TelegramFiletoCloud"
    start = "\n<b>This bot uploads telegram files to MixDrop.co,File.io.\n \nSend any file and the bot will upload it to MixDrop.co , File.io .</b>"
    error = "something is went wrong\n{error} \ncontact admin @M2botzSupport"
    help = "\n<b> HOW TO USE ME😎 \n \n🔽Send Me Telegram File \n🔽 To I Uploaded Some Other Website /n🔽 Choose Best Website For Upload  .</b>"
    about = "\n<b> ABOUT ME🌟 \n \n 🤖Name : <a href='https://t.me/M2_Telegram_Cloud_M2Bot'>Telegram File Cloud Bot</a> \n Support Group : <a href='https://t.me/m2botzsupport'>Click Here</a> </b>
