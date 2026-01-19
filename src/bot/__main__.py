import telebot
from dotenv import load_dotenv
import os

from .handlers import register_handlers

def main():
    # Создайте config.env
    # добавьте переменную TOKEN
    load_dotenv("config.env")


    BOT_TOKEN = os.getenv("TOKEN")
    if not BOT_TOKEN:
        raise ValueError("Переменная окружения TOKEN не установлена!")


    bot = telebot.TeleBot(BOT_TOKEN)
    register_handlers(bot)


    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()