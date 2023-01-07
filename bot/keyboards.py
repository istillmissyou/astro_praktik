from aiogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,
                           KeyboardButton, ReplyKeyboardMarkup)

START = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2).add(
    *[KeyboardButton(name) for name in [
        '💫 Консультации 💫', '📝 Записаться 📝', '🧮 Цены 🧮', '📌 Акции 📌',
    ]]
)

CONSULTATIONS = InlineKeyboardMarkup(row_width=2).add(*[InlineKeyboardButton(
    text=name, callback_data=name
)for name in [
    'Натальная карта', 'Дет. натальная карта', 'Прогнозирование',
    'Детский гороскоп', 'Синастрия', 'Электив',
]])

APPOINTMENT = InlineKeyboardMarkup().add(
    InlineKeyboardButton(
        text='📲 WhatsApp 📲',
        url='wa.me/77011551177',
        callback_data='📲 WhatsApp 📲'
    ),
    InlineKeyboardButton(
        text='💭 Telegram 💭',
        url='t.me/nataliapractice',
        callback_data='💭 Telegram 💭'
    )
)
