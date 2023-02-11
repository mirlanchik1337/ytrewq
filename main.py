from aiogram import Bot, Dispatcher, executor, types
import logging
from decouple import config
import decouple

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=["start"])
async def cd_start(message: types.Message):
    await message.answer(
        f"Hello {message.from_user.full_name}\n"
        f"Пока что всё"
)


@dp.message_handler()
async def echo(message: types.Message):
    print(message)
    await message.answer(message.text)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
