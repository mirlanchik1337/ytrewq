from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from keyboards.client_kb import start_markup


async def start_handler(message: types.Message):
    await bot.send_message(message.from_user.id, f'привет {message.from_user.first_name}',
                           reply_markup=start_markup)
    # await message.answer('это ансфер')
    # await message.reply(message.from_user.first_name)


# опросник\викторина
async def quiz_1(message: types.Message):
    # создание кнопок
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton('next1', callback_data='button1')
    markup.add(button)
    # привязать кнопки к опроснику

    # создание опросника
    ques = 'кто ты воин?'
    answer = [
        'Бетмен-"рыцарь ночи"',
        'Томас Шелби из семьи "Острые козырьки"',
        'Спанч Боб: "квадратные штаны"',
        'Ахилес! "Сын пелея"',
        'Диктор канала "Мастерская настроения"',
        'Оптимус Прайм "Последний прайм"'
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='ты ахилесс',
        open_period=15,
        reply_markup=markup
    )

def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start', 'hello'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
