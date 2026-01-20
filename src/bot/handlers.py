from telebot.async_telebot import AsyncTeleBot
from telebot import types

from .constants import FILES_URL, TEAM_INFO
from .create_qrcode import create_qrcode
from .download_file import download_file


FILES_WITH_DOCS = {
    "Презентация о проекте": "pptx",
    "Презентация о работе команды": "pptx",
    "Отчёт": "docx",
}

QR_TEXTS = {
    "Тест": "прохождения теста",
    "Курс": "прохождения курса",
    "Презентация о проекте": "скачивания презентации",
    "Презентация о работе команды": "скачивания презентации",
    "Отчёт": "скачивания отчёта",
}


def register_handlers(bot: AsyncTeleBot):

    @bot.message_handler(commands=["start"])
    async def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [
            "Тест",
            "Презентация о проекте",
            "Презентация о работе команды",
            "Курс",
            "Отчёт",
            "О команде",
        ]
        markup.add(*map(types.KeyboardButton, buttons))

        await bot.send_message(
            message.chat.id,
            f"Привет, {message.from_user.first_name}, чем могу быть полезен?",
            reply_markup=markup,
        )

    @bot.message_handler(content_types=["text"])
    async def buttons(message):
        text = message.text

        if text == "О команде":
            await bot.send_message(message.chat.id, TEAM_INFO)
            return

        if text not in FILES_URL:
            return

        qr_caption = (
            f"QR-код для {QR_TEXTS[text]}, также "
            f'<a href="{FILES_URL[text]}">прямая ссылка</a>'
        )

        await bot.send_photo(
            message.chat.id,
            create_qrcode(text),
            caption=qr_caption,
            parse_mode="HTML",
        )

        if text in FILES_WITH_DOCS:
            await bot.send_message(
                message.chat.id, "Подождите секунду, сейчас пришлю файл..."
            )
            await bot.send_document(
                message.chat.id,
                download_file(text, FILES_WITH_DOCS[text]),
                caption=text,
            )
