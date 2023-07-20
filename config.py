# Copyright (C) 2023 DX-MODS
#Licensed under the  AGPL-3.0 License;
#you may not use this file except in compliance with the License.
#Author ZIYAN
#if you use our codes try to donate here https://www.buymeacoffee.com/ziyankp

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyrogram client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config get this from mongodb
    DB_NAME = os.environ.get("DB_NAME","Dxbotz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    #start pic url this image will shown in start command get this from @DX_telegraphbot
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    #the channel which need to force subscribed, channel username without @
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    #the log channel id must start in -100 this channel will be were the bot send logs
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration
    #if your bot is web required give True or else False
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))
    #the interval time to ping server
    PING_INTERVAL = int(os.environ.get("PING_INTERVAL", "120"))
    #if your bot is running with web cmd pls copy the web link to ping server not down in 1 minutes
    PING_WEB = os.environ.get("PING_WEB", "") 
