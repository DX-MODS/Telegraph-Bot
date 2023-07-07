from pyrogram import Client
import pyromod.listen
from config import Config
from os import getcwd

DxTelegraphBot = Client(
    name='TelegraphBot',
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    sleep_threshold=Config.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)

multi_clients = {}
work_loads = {}
