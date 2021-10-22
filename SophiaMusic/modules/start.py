from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""Yoo,👋 {message.from_user.first_name}!
\nThis is psy music bot.
I play music on Telegram's VC.
\nFor More Help Use Buttons Below:
 """,
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/PSYR3X/Psymusic")
                  ],[
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/thepsyrex"
                    ),
                    InlineKeyboardButton(
                        "💻 Support Group", url="https://t.me/incOfficials"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add Me To Your Group ➕", url="https://t.me/psymusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""*My psy Music Bot is alive.*""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/thepsyrex")
                ]
            ]
        )
   )


