import logging

from aiogram import Bot, Dispatcher, executor
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message

from config import TOKEN
import keyboards
import messages

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
            text=messages.CONSULTATIONS,
            parse_mode='HTML',
            reply_markup=keyboards.APPOINTMENT,
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


# @dp.message_handler(content_types=['text'])
# async def key(message: Message):
#     if message.text == 'Натальная карта':
#         await message.answer(
#             text=messages.NATAL_CHART,
#             parse_mode='HTML',
#             reply_markup=keyboards.APPOINTMENT,
#         )
#     elif message.text == 'Синастрия':
#         await message.answer(
#             text=messages.SYNASTRY,
#             parse_mode='HTML',
#             reply_markup=keyboards.APPOINTMENT,
#         )
#     elif message.text == 'Электив':
#         await message.answer(
#             text=messages.ELECTIVE,
#             parse_mode='HTML',
#             reply_markup=keyboards.APPOINTMENT,
#         )
#     elif message.text == 'Детский гороскоп':
#         await message.answer(
#             text=messages.CHILDREN_HOROSCOPE,
#             parse_mode='HTML',
#             reply_markup=keyboards.APPOINTMENT,
#         )
#     elif message.text == 'Дет. натальная карта':
#         await message.answer(
#             text=messages.CHILDREN_NATAL_CHART,
#             parse_mode='HTML',
#             reply_markup=keyboards.APPOINTMENT,
#         )
#     elif message.text == 'Прогнозирование':
#         await message.answer(
#             text=messages.PROGNOSTIC,
#             parse_mode='HTML',
#             reply_markup=keyboards.APPOINTMENT,
#         )
#     else:
#         await message.answer(
#             text=messages.ECHO,
#             parse_mode='HTML',
#         )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
