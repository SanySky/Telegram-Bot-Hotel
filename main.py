from telebot.custom_filters import StateFilter
from loader import bot
import handlers
from database.core import crud
from utils.set_bot_commands import set_default_commands

db_write = crud.create()
db_read = crud.retrieve()

if __name__ == "__main__":
    bot.add_custom_filter(StateFilter(bot))
    set_default_commands(bot)
    bot.infinity_polling()
