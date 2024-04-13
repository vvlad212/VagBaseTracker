import asyncio

from loguru import logger

from handlers.state_handler import state_router
from loader import dp, bot
from handlers.message_handler import message_router
from handlers.callback_handler import callback_router


async def main():
    logger.info("Bot started")
    dp.include_router(state_router)
    dp.include_router(message_router)
    dp.include_router(callback_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
