from telebot.async_telebot import AsyncTeleBot
from telebot import types

from .constants import FILES_URL, TEAM_INFO
from .create_qrcode import create_qrcode
from .download_file import download_file


def register_handlers(bot: AsyncTeleBot):
    @bot.message_handler(commands=['start'])
    async def test(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Тест')
        item2 = types.KeyboardButton('Презентация о проекте')
        item3 = types.KeyboardButton('Презентация о работе команды')
        item4 = types.KeyboardButton('Курс')
        item5 = types.KeyboardButton('Отчёт')
        item6 = types.KeyboardButton('О команде')

        markup.add(item1, item2).add(item3, item4).add(item5, item6)

        await bot.send_message(message.chat.id, 'Привет, я - {1.first_name}, чем могу быть полезен?'
                               .format(
                                   message.from_user,
                                   bot.get_me()),
                               reply_markup=markup,
                               )

    @bot.message_handler(content_types=['text'])
    async def buttons(message):
        if message.text == 'Тест':
            qr_caption = f'QR-код для прохождения теста, также <a href="{FILES_URL[message.text]}">прямая ссылка</a> на него'
            await bot.send_photo(
                message.chat.id,
                create_qrcode(message.text),
                caption=qr_caption,
                parse_mode='HTML'
            )

        if message.text == 'Презентация о проекте':
            qr_caption = f'QR-код для скачивания презентации, также <a href="{FILES_URL[message.text]}">прямая ссылка</a> на неё'
            await bot.send_photo(
                message.chat.id,
                create_qrcode(message.text),
                caption=qr_caption,
                parse_mode='HTML'
            )
            await bot.send_message(
                message.chat.id, "Подождите секунду, сейчас пришлю файл...")

            await bot.send_document(
                message.chat.id,
                download_file(
                    message.text, 'pptx'),
                caption=f'{message.text}'
            )
        if message.text == 'Презентация о работе команды':
            qr_caption = f'QR-код для скачивания презентации, также <a href="{FILES_URL[message.text]}">прямая ссылка</a> на неё'
            await bot.send_photo(
                message.chat.id,
                create_qrcode(message.text),
                caption=qr_caption,
                parse_mode='HTML'
            )
            await bot.send_message(
                message.chat.id, "Подождите секунду, сейчас пришлю файл...")

            await bot.send_document(
                message.chat.id,
                download_file(
                    message.text, 'pptx'),
                caption=f'{message.text}'
            )

        if message.text == 'Курс':
            qr_caption = f'QR-код для прохождения курса, также <a href="{FILES_URL[message.text]}">прямая ссылка</a> на него'
            await bot.send_photo(
                message.chat.id,
                create_qrcode(message.text),
                caption=qr_caption,
                parse_mode='HTML'
            )

        if message.text == 'Отчёт':
            qr_caption = f'QR-код для скачивания отчёта, также <a href="{FILES_URL[message.text]}">прямая ссылка</a> на него'
            await bot.send_photo(
                message.chat.id,
                create_qrcode(message.text),
                caption=qr_caption,
                parse_mode='HTML'
            )
            await bot.send_message(
                message.chat.id, "Подождите секунду, сейчас пришлю файл...")

            await bot.send_document(
                message.chat.id,
                download_file(
                    message.text, 'docx'),
                caption=f'{message.text}'
            )

        if message.text == 'О команде':
            await bot.send_message(
                message.chat.id,
                TEAM_INFO
            )
