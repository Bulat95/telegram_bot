import telebot
import UserService

API_TOKEN = '6496268341:AAHiLUnZq4wJVh1y4n2ZBbLqkjFIPqnwuM8'

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['/help', '/start'])
def welcome(message):
    bot.send_message(message.chat.id, "Сейчас всего лишь две команды доступны")


@bot.message_handler(commands=['info'])
def send_welcome(message):
    name = bot.get_me()
    print(name)
    bot.reply_to(message, "Welcome, " + name)

@bot.message_handler(content_types=['text'])
def lalalla(message):
    bot.send_message(message.chat.id, message.text)

@bot.message_handler(commands=["register"])
def register(message):
    # Запрашиваем данные пользователя
    bot.reply_to(message, "Введите ваш логин:")
    bot.register_next_step_handler(message, process_login)


def process_login(message):
    login = message.text
    bot.reply_to(message, "Введите ваше имя:")
    bot.register_next_step_handler(message, process_name, login)


def process_name(message, login):
    name = message.text
    bot.reply_to(message, "Введите вашу фамилию:")
    bot.register_next_step_handler(message, process_surname, login, name)


def process_surname(message, login, name):
    surname = message.text
    bot.reply_to(message, "Введите ваш аккаунт:")
    bot.register_next_step_handler(message, process_account, login, name, surname)


def process_account(message, login, name, surname):
    try:
        account = float(message.text)
        bot.reply_to(message, "Введите ваш статус (Активный/Неактивный):")
        bot.register_next_step_handler(message, save_user, login, name, surname, account)
    except ValueError:
        bot.reply_to(message, "Ошибка! Введите числовое значение для аккаунта.")
        bot.register_next_step_handler(message, process_account, login, name, surname)


def save_user(message, login, name, surname, account):
    status = False
    if message.text.lower() == "активный":
        status = True
    # Сохраняем данные пользователя в базе данных
    bot.send_message(message.chat.id, "Вы успешно зарегистрированы!")

bot.polling(none_stop=True)


