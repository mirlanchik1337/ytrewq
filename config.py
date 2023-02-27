from aiogram import Dispatcher, Bot
from aiogram.dispatcher import storage
from dotenv import load_dotenv
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

load_dotenv()
bot = Bot(token=os.getenv('BOT_TOKEN'))
db = Dispatcher(bot=bot, storage=storage)
ADMIN = [5416111170, 5416111170]
