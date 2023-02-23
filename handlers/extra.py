from aiogram import types, Dispatcher
from config import bot


async def bad_word(message: types.Message):
    if message.chat.type != 'private':
        bad_words = ['балбес', 'урод', 'дурак']
        username = f'{message.from_user.username}' \
            if message.from_user.username is not None else message.from_user.full_name

        for word in bad_words:
            if word in message.text.lower().replace(' ', ''):
                await bot.delete_message(message.chat.id, message.message_id)
                await message.answer(f'Не матерись {username}')

        if message.text == 'python':
            text = f'У тебя все получиться {message.from_user.full_name}'
            await bot.send_message(message.chat.id, text)
            await bot.send_dice(message.chat.id, emoji='🎰')

        if message.text.startswith('.') and message.reply_to_message:
            await bot.pin_chat_message(message.chat.id, message.message_id)

    else:
        await message.answer("Пиши в группе")

def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(bad_word)
