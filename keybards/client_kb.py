from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

start_markup = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width = 3
)

start_button = KeyboardButton("/start")
end_button = KeyboardButton("/end")
quiz_button = KeyboardButton("/quiz")


start_markup.add(start_button, end_button, quiz_button)


