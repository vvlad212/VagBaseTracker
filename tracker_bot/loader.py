from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from config import config

bot = Bot(token=config.bot_token)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
