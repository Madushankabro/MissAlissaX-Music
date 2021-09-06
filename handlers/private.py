from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker(" CAACAgUAAxkBAAIEpWE1ztNddQZpLk7hxK7Kim3j-yt5AALCAwACXXSxVarEpVwH_WhOIAQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice chat.
Developed by [𝐄 𝐏𝐔𝐒𝐓𝐇𝐀𝐊𝐀𝐋𝐀𝐘𝐀 𝐁𝐎𝐓𝐬 ™ 🇱🇰](https://t.me/epusthakalaya_bots).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                        "⚜️ Add Me To Your Group ⚜️", url="https://t.me/MissAlissaMusicRoBot?startgroup=true"
                    )],[
                    InlineKeyboardButton(
                        "🛠 Original Source Code 🛠", url="https://github.com/Infinity-Bots/GroupMusicPlayerBot"
                    ),
                    InlineKeyboardButton(
                        "🌟Review Us🌟", url="https://t.me/tlgrmcbot?start=missalissamusicrobot"
                    )
                ],[
                    InlineKeyboardButton(
                        "👥 Main Group 👥", url="https://t.me/epusthakalayabotsupport"
                    ),
                    InlineKeyboardButton(
                        "🔊 Bots Channel 🔊", url="https://t.me/epusthakalaya_bots"
                    )
                ],[
                InlineKeyboardButton(
                        "♻️ My Assistant ♻️", url="https://t.me/AlissaXPlayer"
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


