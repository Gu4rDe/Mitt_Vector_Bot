import telebot
from telebot import types
from dotenv import load_dotenv
import os

from consts import FILES_URL, TEAM_INFO
from create_qrcode import create_qr
from googleDiskDownload import download_file

# Создайте config.env
# добавьте переменную TOKEN
load_dotenv("config.env")


BOT_TOKEN = os.getenv("TOKEN")
if not BOT_TOKEN:
    raise ValueError("Переменная окружения TOKEN не установлена!")


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def test(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('тест')
    item2 = types.KeyboardButton('презентация')
    item3 = types.KeyboardButton('курс')
    item4 = types.KeyboardButton('отчёт')
    item5 = types.KeyboardButton('О команде')

    markup.add(item1, item2).add(item3, item4).add(item5)

    bot.send_message(message.chat.id, 'Привет, я - {1.first_name}, чем могу быть полезен?'
                     .format(
                         message.from_user,
                         bot.get_me()),
                     reply_markup=markup,
                     )


@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.text == 'тест':
        qr_caption = f'QR-код для прохождения теста, также <a href="{FILES_URL[message.text]}">прямая ссылка</a> на него'
        bot.send_photo(
            message.chat.id,
            create_qr(message.text),
            caption=qr_caption,
            parse_mode='HTML'
        )

    if message.text == 'презентация':
        qr_caption = f'QR-код для скачивания презентации, также <a href="{FILES_URL[message.text]}">прямая ссылка</a> на неё'
        bot.send_photo(
            message.chat.id,
            create_qr(message.text),
            caption=qr_caption,
            parse_mode='HTML'
        )
        bot.send_message(
            message.chat.id, "Подождите секунду, сейчас пришлю файл...")

        bot.send_document(message.chat.id,
                          download_file(
                              message.text),
                          caption='Презентация'
                          )

    if message.text == 'курс':
        bot.send_message(message.chat.id, 'тут пока ничего нет')

    if message.text == 'отчёт':
        bot.send_message(message.chat.id, 'тут пока ничего нет')

    if message.text == 'О команде':

        bot.send_message(message.chat.id, TEAM_INFO)


bot.polling(none_stop=True)
