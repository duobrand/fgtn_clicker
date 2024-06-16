from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

allow_usage = InlineKeyboardMarkup(
    inline_keyboard =[
        [
            InlineKeyboardButton(text="Our Channel", url="tg://resolve?domain=fgtn_test")
        ],
        [
            InlineKeyboardButton(text="I subscribed ✅", callback_data="check_subscription")
        ]
    ]
)