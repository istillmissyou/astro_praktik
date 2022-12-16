from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)

START = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    *[KeyboardButton(name) for name in [
        'Натальная карта', 'Прогнозирование', 'Детский гороскоп', 'Гороскоп',
        'Синастрия', 'Электив',
    ]]
)

APPOINTMENT = InlineKeyboardMarkup().add(InlineKeyboardButton(
    text='Записаться', callback_data='Записаться'
))