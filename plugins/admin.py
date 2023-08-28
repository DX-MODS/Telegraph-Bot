from config import Config
from helper.database import db
from pyrogram.types import Message
from pyrogram import Client, filters

@Client.on_message(filters.command("users") & filters.user(Config.ADMIN))
async def get_stats(bot :Client, message: Message):
    mr = await message.reply('**𝙰𝙲𝙲𝙴𝚂𝚂𝙸𝙽𝙶 𝙳𝙴𝚃𝙰𝙸𝙻𝚂.....**')
    total_users = await db.total_users_count()
    await mr.edit( text=f"𝚝𝚘𝚝𝚊𝚕 𝚞𝚜𝚎𝚛𝚜 `{total_users}`")
