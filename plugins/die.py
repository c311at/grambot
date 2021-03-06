from random import choice
from userbot import bot, logger
from telethon import TelegramClient, events
from config import die

@bot.on(events.NewMessage(**die))
async def insult(event):
    logger.info("insults plugin called")
    file = open("./plugins/data/insults").readlines()
    insult = choice(file)
    logger.info(f"chosen insult - {insult}")
    await event.respond(insult, reply_to=event.reply_to_msg_id)