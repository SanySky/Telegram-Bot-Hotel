from keyboards.reply.contact import request_contact
from loader import bot
from states.contact_information import UserInfoState
from telebot.types import Message


@bot.message_handler(commands=["survey"])
def survey(message: Message) -> None:
    bot.set_state(message.from_user.id, UserInfoState.name, message.chat.id)
    bot.send_message(message.from_user.id, f'Привет, {message.from_user.username} введи свое имя')


@bot.message_handler(state=UserInfoState.name)
def get_name(message: Message) -> None:
    if message.text.isalpha():
        bot.send_message(message.from_user.id, f'Спасибо записал, теперь введи свой возраст.')
        bot.set_state(message.from_user.id, UserInfoState.age, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["name"] = message.text
    else:
        bot.send_message(message.from_user.id, f'Имя может содержать только буквы')


@bot.message_handler(state=UserInfoState.age)
def get_age(message: Message) -> None:
    if message.text.isdigit():
        bot.send_message(message.from_user.id, f'Спасибо записал, теперь введи страну проживания.')
        bot.set_state(message.from_user.id, UserInfoState.country, message.chat.id)

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data["age"] = message.text
    else:
        bot.send_message(message.from_user.id, f'Возраст может содержать только цифры')


@bot.message_handler(state=UserInfoState.country)
def get_country(message: Message) -> None:
    bot.send_message(message.from_user.id, f'Спасибо записал, теперь введи город проживания.')
    bot.set_state(message.from_user.id, UserInfoState.city, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["country"] = message.text


@bot.message_handler(state=UserInfoState.city)
def get_city(message: Message) -> None:
    bot.send_message(message.from_user.id, f'Спасибо записал, теперь отправь свой номер, для этого нажми на кнопку.',
                     reply_markup=request_contact())
    bot.set_state(message.from_user.id, UserInfoState.number_telephone, message.chat.id)

    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data["city"] = message.text


@bot.message_handler(content_types=['text', 'contact'], state=UserInfoState.number_telephone)
def get_number_telephone(message: Message) -> None:
    if message.content_type == 'contact':
        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['number_telephone'] = message.contact.phone_number

        text = f'Спасибо, что предоставили нам информацию, ваши данные\n ' \
               f'Имя - {data["name"]}\n Возраст - {data["age"]}\n Страна - {data["country"]}\n ' \
               f'Город - {data["city"]}\n Телефон - {data["number_telephone"]}'
        bot.send_message(message.from_user.id, f'{text}')
    else:
        bot.send_message(message.from_user.id, f'Чтобы отправить информацию, нажми на кнопку')
