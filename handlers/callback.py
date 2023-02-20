from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot, dp

# перехватчик нажатия кнопки
async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton('next', callback_data='button2')
    markup.add(button2)
    ques = 'кто это?'
    answer = [
        'Бетмен-рыцарь ночи',
        'томас шелби из семьи острые козырьки',
        'спанч боб:квадратные штаны',
        'Ахилес! Сын пелея ',
        'диктор канала "Мастерская настроения"',
        'оптимус прайм последний прайм'
    ]
    # photo = open('media/img.png', 'rb')
    # await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='это бетмен ты угадал',
        open_period=15,
        reply_markup=markup
    )


async def quiz_3(call: types.CallbackQuery):
    ques = 'откуда мем?'
    answer = [
        'Нелепо фотогеничный парень',
        'Угрюмый кот',
        'Филосораптор',
        'Доге',
    ]
    # photo = open('large_p18e64la397s51qt3prjdhbbal3.jpg', 'rb')
    # await bot.send_photo(call.from_user.id, photo=photo)
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=ques,
        options=answer,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="it's Доге, you win!",
        open_period=15
    )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text='button1')
    dp.register_callback_query_handler(quiz_3, text='button2')
