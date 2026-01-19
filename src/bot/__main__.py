from dotenv import load_dotenv
import os
import asyncio
from telebot.async_telebot import AsyncTeleBot


from .handlers import register_handlers


def main():
    # Создайте config.env
    # добавьте переменную TOKEN
    load_dotenv("config.env")

    BOT_TOKEN = os.getenv("TOKEN")
    if not BOT_TOKEN:
        raise ValueError("Переменная окружения TOKEN не установлена!")

    bot = AsyncTeleBot(BOT_TOKEN)

    register_handlers(bot)
    print("Бот запущен")
    asyncio.run(bot.polling())


if __name__ == "__main__":
    main()
