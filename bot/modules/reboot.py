# Implement By https://github.com/jusidama18
# Based on this https://github.com/DevsExpo/FridayUserbot/blob/master/plugins/heroku_helpers.py

from pyrogram import filters
from bot import app, OWNER_ID, bot, REBOOT_BOT
from bot.helper import check_heroku

@app.on_message(filters.command([f'{REBOOT_BOT}', f'{REBOOT_BOT}@{bot.username}']) & filters.user(OWNER_ID))
@check_heroku
async def gib_restart(client, message, hap):
    msg_ = await message.reply_text("[HEROKU] - Restarting")
    hap.restart()


