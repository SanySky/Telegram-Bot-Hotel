from telebot.types import Message
from loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.reply_to(message, f"Привет, {message.from_user.full_name}! Этот бот предназначен для поиска отелей в России."
                          f"Для более подробной информации введите команду help.")
