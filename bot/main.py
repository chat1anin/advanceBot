from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import profile, documents
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

# Регистрируем роутеры
dp.include_router(profile.router)
dp.include_router(documents.router)

async def main():
    await bot.set_my_commands([
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="profile", description="Посмотреть / редактировать профиль")
    ])
    from aiogram import executor
    executor.start_polling(dp)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
