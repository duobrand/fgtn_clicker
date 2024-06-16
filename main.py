from Token import TOKEN

from keyboards import allow_usage

import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}! \nSubscribe to the channel to use the bot", reply_markup=allow_usage)


@dp.callback_query()
async def check_subscription(query: CallbackQuery):
    user_id = query.from_user.id
    try:
        member = await bot.get_chat_member(chat_id=-1002242286490, user_id=user_id)
        if member.status in ["member", "administrator", "creator"]:
            await query.answer("You are subscribed to the channel!")
        else:
            await query.answer("You are not subscribed to the channel. Please subscribe to access this feature.")
    except Exception as e:
        await query.answer("An error occurred. Please try again later.")
        print(e)


@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    global bot
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())