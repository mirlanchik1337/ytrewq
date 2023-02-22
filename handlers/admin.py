from aiogram import types, Dispatcher
from config import bot
from config import ADMINS

async def ban(message: types.Message):
    if message.chat.type != 'private':
        if message.from_user.id not in ADMINS:
            await message.answer('Ты не мой босс')
        elif not message.reply_to_message:
            await message.answer('Команда должна быть ответом на смс!')
        else:
            await bot.kick_chat_member(message.chat.id,
                                       message.reply_to_message.from_user.id)
            text = f'{message.reply_to_message.from_user.username} вышел сам'
            pinned_message = await bot.send_message(message.chat.id, text)
            await bot.pin_chat_message(message.chat.id, pinned_message.message_id)
    else:
        await message.answer('Пиши в группе')

async def cheers_up(message: types.Message):
    if message.text == 'python':
        text = f'У тебя все получиться {message.from_user.full_name}'
        await bot.send_message(message.chat.id, text)
        await bot.send_dice(message.chat.id, emoji='🎰')

def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix ='!/')
    dp.register_message_handler(cheers_up)