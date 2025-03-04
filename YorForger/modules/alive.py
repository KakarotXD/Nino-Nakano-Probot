from YorForger import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/cfef463ba4303cf731fa0.jpg"

def alive(update: Update, context: CallbackContext):
    TEXT = f"I am Nino Nakano!\n\nI Work Under - **[【V๏ɪ፝֟𝔡】 ✧Network✧](https://t.me/voidxnetwork)** \n\n◈ I will love to be in your group chat ◈"
    

    update.effective_message.reply_photo(
        PHOTO, caption= TEXT,
        parse_mode=ParseMode.MARKDOWN,

            reply_markup=InlineKeyboardMarkup(
            [
                [
                InlineKeyboardButton(text="【Support】", url="https://t.me/NinoxSupport"),
                InlineKeyboardButton(text="【Updates】", url="https://t.me/NinoXupdates")
                ],
                [InlineKeyboardButton(text="【V๏ɪ፝֟𝔡】Network", url="https://t.me/voidxnetwork")]
            ]
        ),
    )

void_handler = CommandHandler("alive", alive, run_async = True)
dispatcher.add_handler(void_handler)


__help__ = """ 
❂ /alive: To check if bot is alive or not."""
   
__mod_name__ = "Alive"
