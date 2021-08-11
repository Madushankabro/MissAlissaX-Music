from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgIAAxkBAAEFirBhE1-v4LoR9Iw3WbcLZhDVdt6ucQACKwADTlzSKYG46jjQtpxnHgQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [ᴋᴀsᴜ ʙʀᴏ 🇱🇰](https://t.me/kasu_bro).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/MissAlissaMusicRoBot?startgroup=true"
                    )],[
                    InlineKeyboardButton(
                        "🛠 Original Source Code 🛠", url="https://github.com/Infinity-Bots/GroupMusicPlayerBot"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/epusthakalaya_bots"
                    )
                ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/epusthakalayabotsupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/epusthakalaya_bots"
                    )
                ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/epusthakalayabotsupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/epusthakalaya_bots"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🌟Review Us🌟", url="https://t.me/JEGroupMusicPlayerBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**AlissaX Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/epusthakalaya_bots")
                ]
            ]
        )
   )


