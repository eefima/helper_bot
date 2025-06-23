import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from config import BOT_TOKEN

from handlers import start
from handlers import my_disciplines
from handlers import discipline_actions
from handlers import add_homework
from handlers import add_lecture
logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()

# Регистрируем роутеры один раз, до запуска polling
dp.include_router(start.router)
dp.include_router(my_disciplines.router)
dp.include_router(discipline_actions.router)
dp.include_router(add_homework.router)
dp.include_router(add_lecture.router)
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())