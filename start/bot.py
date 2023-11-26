import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

import UserService

API_TOKEN = '6496268341:AAHiLUnZq4wJVh1y4n2ZBbLqkjFIPqnwuM8'

bot = telebot.TeleBot(API_TOKEN)

userService = UserService

@bot.message_handler(commands=['start'])
def send_initial_message(message):
    user = message.from_user
    userService.register_user(user.username, user.first_name, user.last_name, 0, "true")
    bot.send_message(message.chat.id,"Добро пожаловать, вы зарегистрировались и можете отправлять сообщения!")


def send_menu(chat_id):
    message = "Выберите одну из команд:"

    # Создаем кнопки меню
    menu_buttons = [
        [InlineKeyboardButton('Команда 1', callback_data='command1')],
        [InlineKeyboardButton('Команда 2', callback_data='command2')],
        [InlineKeyboardButton('Команда 3', callback_data='command3')]
    ]

    # Создаем разметку меню
    menu_markup = InlineKeyboardMarkup(menu_buttons)

    # Отправляем сообщение с меню
    bot.send_message(chat_id=chat_id, text=message, reply_markup=menu_markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    # Обработка выбора пользователем команды из меню
    if call.data == 'command1':
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали Команду 1")
    elif call.data == 'command2':
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали Команду 2")
    elif call.data == 'command3':
        bot.send_message(chat_id=call.message.chat.id, text="Вы выбрали Команду 3")


@bot.message_handler(commands=['starts'])
def start_command_handler(message):
    send_menu(message.chat.id)

bot.polling(none_stop=True)


