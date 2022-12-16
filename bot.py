import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery, Message

import keyboards
import messages
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(CommandStart())
async def start(message: Message):
    await message.answer(
        text=messages.START.format(message.chat.first_name),
        parse_mode='HTML',
        reply_markup=keyboards.START,
    )
    await message.delete()


@dp.message_handler(content_types=['text'])
async def key(message: Message):
    if message.text == 'Натальная карта':
        await message.answer(
            text=messages.NATAL_CHART,
            parse_mode='HTML',
            reply_markup=keyboards.APPOINTMENT,
        )
    elif message.text == 'Синастрия':
        await message.answer(
            text=messages.SYNASTRY,
            parse_mode='HTML',
            reply_markup=keyboards.APPOINTMENT,
        )
    else:
        await message.answer(
        text=messages.ECHO,
        parse_mode='HTML',
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
