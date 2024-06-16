from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

allow_usage = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="Our Channel", url="tg://resolve?domain=fgtn_tg")
        ],
        [
            InlineKeyboardButton(text="I subscribed ✅", callback_data="check_subscription")
        ]
    ]
)

start_clicking = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text="START CLICKING", web_app=WebAppInfo(url="https://google.com"))
        ],
    ]
)