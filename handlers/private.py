from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIEpWE1ztNddQZpLk7hxK7Kim3j-yt5AALCAwACXXSxVarEpVwH_WhOIAQ")
    await message.reply_text(
        f"""**Hey, I'm {bn} π΅

I can play music in your group's voice chat.
Developed by [π ππππππππππππ ππππ¬ β’ π±π°](https://t.me/epusthakalaya_bots).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(
                        "βοΈ Add Me To Your Group βοΈ", url="https://t.me/MissAlissaMusicRoBot?startgroup=true"
                    )],[
                    InlineKeyboardButton(
                        "π  Original Source Code π ", url="https://github.com/Infinity-Bots/GroupMusicPlayerBot"
                    ),
                    InlineKeyboardButton(
                        "πReview Usπ", url="https://t.me/tlgrmcbot?start=missalissamusicrobot"
                    )
                ],[
                    InlineKeyboardButton(
                        "π₯ Main Group π₯", url="https://t.me/epusthakalayabotsupport"
                    ),
                    InlineKeyboardButton(
                        "π Bots Channel π", url="https://t.me/epusthakalaya_bots"
                    )
                ],[
                InlineKeyboardButton(
                        "β»οΈ My Assistant β»οΈ", url="https://t.me/AlissaXPlayer"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**AlissaX Music Player Online β**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π Channel", url="https://t.me/epusthakalaya_bots")
                ]
            ]
        )
   )


