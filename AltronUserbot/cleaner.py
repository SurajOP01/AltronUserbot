import os
from pyrogram import Client
from pyrogram.types import Message
from helpers.command import commandpro


@Client.on_message(commandpro(["/cl", "!cl", "Cl", "/clean", "Clean", "!clean"]))
async def cleanup(_, message: Message):
    pth = os.path.realpath(".")
    ls_dir = os.listdir(pth)
    if ls_dir:
        for dta in os.listdir(pth):
            os.system("rm -rf *.webm *.jpg")
        await message.reply_text("✅ **Ƈɭɘɑɳɘɗ**")
    else:
        await message.reply_text("✅ **Ʌɭɤɘɑɗy Ƈɭɘɑɳɘɗ**")
