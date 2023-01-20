import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message, InputFile

from config import TOKEN, ADMIN, ADMIN2
import keyboards
import messages

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

num_start = 0

@dp.message_handler(CommandStart())
async def start(message: Message):
    global num_start
    await message.answer_photo(
        photo=InputFile('../media/start.jpeg'),
        caption=messages.START.format(message.chat.first_name),
        parse_mode='HTML',
        reply_markup=keyboards.START,
    )
    await message.delete()
    num_start += 1
    await bot.send_message(
        chat_id=ADMIN,
        text=messages.ADMIN_REPLY.format(
            message.from_user.full_name,
            message.from_user.username,
            num_start,
        )
    )
    await bot.send_message(
        chat_id=ADMIN2,
        text=messages.ADMIN_REPLY.format(
            message.from_user.full_name,
            message.from_user.username,
            num_start,
        )
    )


@dp.message_handler(content_types=['text'])
async def key(message: Message):
    if message.text == '💫 Консультации 💫':
        await message.delete()
        await message.answer(
            text=messages.CONSULTATIONS,
            parse_mode='HTML',
            reply_markup=keyboards.CONSULTATIONS,
        )
    elif message.text == '📝 Записаться 📝':
        await message.delete()
        await message.answer(
            text=messages.APPOINTMENT,
            parse_mode='HTML',
            reply_markup=keyboards.APPOINTMENT,
        )
    elif message.text == '🧮 Цены 🧮':
        await message.delete()
        await message.answer(
            text=messages.PRICES,
            parse_mode='HTML',
        )
    elif message.text == '📌 Акции 📌':
        await message.delete()
        await message.answer(
            text=messages.PROMO,
            parse_mode='HTML',
        )
    else:
        await message.answer(
            text=messages.ECHO,
            parse_mode='HTML',
        )


@dp.callback_query_handler(lambda callback_query: True)
async def inline(callback_query):
    if callback_query.data == 'Натальная карта':
        await callback_query.message.delete()
        await callback_query.message.answer(
            text=messages.NATAL_CHART,
            reply_markup=keyboards.CONSULTATIONS,
            parse_mode="HTML",
        )
    elif callback_query.data == 'Синастрия':
        await callback_query.message.delete()
        await callback_query.message.answer(
            text=messages.SYNASTRY,
            parse_mode='HTML',
            reply_markup=keyboards.CONSULTATIONS,
        )
    elif callback_query.data == 'Электив':
        await callback_query.message.delete()
        await callback_query.message.answer(
            text=messages.ELECTIVE,
            parse_mode='HTML',
            reply_markup=keyboards.CONSULTATIONS,
        )
    elif callback_query.data == 'Детский гороскоп':
        await callback_query.message.delete()
        await callback_query.message.answer(
            text=messages.CHILDREN_HOROSCOPE,
            parse_mode='HTML',
            reply_markup=keyboards.CONSULTATIONS,
        )
    elif callback_query.data == 'Дет. натальная карта':
        await callback_query.message.delete()
        await callback_query.message.answer(
            text=messages.CHILDREN_NATAL_CHART,
            parse_mode='HTML',
            reply_markup=keyboards.CONSULTATIONS,
        )
    elif callback_query.data == 'Прогнозирование':
        await callback_query.message.delete()
        await callback_query.message.answer(
            text=messages.PROGNOSTIC,
            parse_mode='HTML',
            reply_markup=keyboards.CONSULTATIONS,
        )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
