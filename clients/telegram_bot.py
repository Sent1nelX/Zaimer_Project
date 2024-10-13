import os
import time
import logging
from pytz import UTC
from dateutil import tz
from datetime import datetime
from pyrogram import Client, filters
from django.utils.timezone import now
from clients.models import TelegramUser, TelegramUserLog
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton

app = Client("bot", api_id=27446844, api_hash="21ec39462f4585e95d48ab4fa647e436", bot_token="7651580994:AAGCkmgD--P0xWNX6joNN_bzNVzV36dE1rA")

# Команда для регистрации пользователей
@app.on_message(filters.command('start') & filters.private)
def start(client, message):
    user, created = TelegramUser.objects.get_or_create(
        telegram_id=message.from_user.id,
        defaults={
            'first_name': message.from_user.first_name,
            'last_name': message.from_user.last_name,
            'username': message.from_user.username,
        }
    )

    if user.approved:
        message.reply_text("Вы уже зарегистрированы.")
    else:
        # Отправляем кнопку для запроса номера телефона
        message.reply_text(
            "Пожалуйста, отправьте свой номер телефона для завершения регистрации.",
            reply_markup=ReplyKeyboardMarkup(
                [[KeyboardButton("Отправить номер телефона", request_contact=True)]],
                resize_keyboard=True,
                one_time_keyboard=True
            )
        )

# Обработка контакта с номером телефона
@app.on_message(filters.contact)
def handle_contact(client, message):
    # Обновляем номер телефона в базе данных
    user = TelegramUser.objects.get(telegram_id=message.from_user.id)
    user.phone_number = message.contact.phone_number
    user.save()

    # Уведомляем администратора
    admin_id = 5792605910
    client.send_message(
        admin_id, 
        f"Новый пользователь {user.first_name} прислал номер телефона: {user.phone_number}.",
        reply_markup=approval_keyboard(user.telegram_id)
    )

    message.reply_text("Ваш запрос на регистрацию отправлен на рассмотрение администратору.")

# Функция для создания клавиатуры одобрения/блокировки
def approval_keyboard(telegram_id):
    from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Одобрить", callback_data=f"approve_{telegram_id}"), 
         InlineKeyboardButton("Отклонить", callback_data=f"block_{telegram_id}")]
    ])

# Обработка кнопок одобрения регистрации
@app.on_callback_query(filters.regex(r"approve_\d+"))
def approve_user(client, callback_query):
    telegram_id = callback_query.data.split('_')[1]
    user = TelegramUser.objects.get(telegram_id=telegram_id)
    user.approved = True
    user.save()
    client.send_message(telegram_id, "Вы были одобрены для использования бота!")
    callback_query.answer("Пользователь одобрен.")

# Обработка кнопок блокировки
@app.on_callback_query(filters.regex(r"block_\d+"))
def block_user(client, callback_query):
    telegram_id = callback_query.data.split('_')[1]
    TelegramUser.objects.filter(telegram_id=telegram_id).delete()
    callback_query.answer("Пользователь заблокирован.")

# # Логирование действий пользователя
# def log_action(user, action):
#     TelegramUserLog.objects.create(user=user, action=action, timestamp=now())

# @app.on_message(filters.private & filters.text)
# def log_user_action(client, message):
#     user = TelegramUser.objects.get(telegram_id=message.from_user.id)
#     if user.approved:
#         log_action(user, f"Сообщение: {message.text}")


# Определяем строку формата
format_str = "%S:%M:%H %d-%m-%Y"

# Логирование действий пользователя
def log_action(user, action, timestamp):
    # Форматируем временную метку
    formatted_time = timestamp.strftime(format_str)
    TelegramUserLog.objects.create(user=user, action=action, timestamp=formatted_time)

@app.on_message(filters.private & filters.text)
def log_user_action(client, message):
    user = TelegramUser.objects.get(telegram_id=message.from_user.id)
    if user.approved:
        # Получаем время отправки сообщения и преобразуем в UTC
        message_time = message.date.replace(tzinfo=UTC)  # Привязываем временную зону
        log_action(user, f"Сообщение: {message.text}", message_time)

@app.on_callback_query()
def log_button_action(client, callback_query):
    user = TelegramUser.objects.get(telegram_id=callback_query.from_user.id)
    if user.approved:
        # Получаем время нажатия кнопки и преобразуем в UTC
        button_time = callback_query.date.replace(tzinfo=UTC)  # Привязываем временную зону
        log_action(user, f"Нажата кнопка: {callback_query.data}", button_time)

@app.on_message(filters.private & filters.command("start"))
def log_start_command(client, message):
    user = TelegramUser.objects.get(telegram_id=message.from_user.id)
    if user.approved:
        start_time = message.date.replace(tzinfo=UTC)  # Привязываем временную зону
        log_action(user, "Команда /start", start_time)

def RunBot():
    try:
        logger = logging.getLogger("RunBot")
        logger.info("Запуск бота!")
        app.run()
    except KeyboardInterrupt:
        logger.error("Бот остановлен принудительно!")
    except Exception as e:
        logger.error(f"Ошибка при запуске бота: {e}!")

if __name__ == "__main__":
    RunBot()
