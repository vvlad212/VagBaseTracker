from aiogram.types import Message
from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from keyboards import reply_keyboard as rp_kb
from keyboards import inline_keyboard as in_kb
from loguru import logger

message_router = Router()


@message_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет это бот VagBase через меня можно записаться на ремонт или узнать статус..",
                         reply_markup=rp_kb.menu_keyboard)
    logger.info(f'User {message.from_user.full_name} chat_id {message.chat.id} connected.')


@message_router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("Помощь пока не активна")


@message_router.message(F.text == 'Записаться')
async def repair_task(message: Message):
    await message.answer("Что вы хотите?", reply_markup=in_kb.sign_up_keyboard)
    logger.info(f'User {message.from_user.full_name} chat_id {message.chat.id} repair.')


@message_router.message(F.text == 'лох')
async def filter_message(message: Message):
    await message.reply("ругательства запрещены")
