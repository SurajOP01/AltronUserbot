from pyrogram import filters, Client
from config import SUDO_USERS
from pyrogram.types import Message


@client.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
@client2.on_message(filters.command(["help"], ["/", "!", "."]) & filters.user(SUDO_USERS))
async def start(Client, message: Message):
    await message.reply_text(
    "**🤖 ʜᴇʏᴀ..!!**\n\n»__ ғᴏʀ ʜᴇʟᴘ ᴍᴇɴᴜ ɢᴏ ᴛᴏ ʏᴏᴜʀ ᴄʀᴇᴀᴛᴇᴅ ʙᴏᴛ's ᴅᴍ » @BOT_USERNAME\n\nsᴏᴏɴ ᴀᴅᴅɪɴɢ ɪɴʟɪɴᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ʙᴜᴛᴛᴏɴs ɪɴ ᴜsᴇʀʙᴏᴛ\nᴊᴏɪɴ » @Altron_X__"
    )
    
    

