# -*- coding: utf-8 -*-

import asyncio
import sqlite3
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import TOKEN
# Импорт функции из message_generator.py
from message_generator import generate_motivation

bot = Bot(token=TOKEN)
dp = Dispatcher()
scheduler = AsyncIOScheduler()

# Создание БД для хранения настроек пользователей
conn = sqlite3.connect("users.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        interval INTEGER DEFAULT 1,
        start_hour INTEGER DEFAULT 9,
        active INTEGER DEFAULT 1
    )
""")
conn.commit()

def get_random_message():
    return generate_motivation()

async def send_scheduled_message(user_id):
    cursor.execute("SELECT active FROM users WHERE user_id = ?", (user_id,))
    active = cursor.fetchone()
    if active and active[0] == 1:
        message = get_random_message()
        await bot.send_message(user_id, message)

def schedule_messages():
    cursor.execute("SELECT user_id, interval, active FROM users")
    users = cursor.fetchall()
    for user_id, interval, active in users:
        if active == 1:
            # Удаляем старые задания для пользователя
            for job in scheduler.get_jobs():
                if job.args == (user_id,):
                    scheduler.remove_job(job.id)

            # Добавляем новое задание с нужным интервалом
            if interval == 0:
                scheduler.add_job(
                    send_scheduled_message, "interval", minutes=1, args=[user_id]
                )
            else:
                scheduler.add_job(
                    send_scheduled_message, "interval", hours=interval, args=[user_id]
                )


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    cursor.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (message.from_user.id,))
    conn.commit()
    await message.answer("Привет! Выберите интервал отправки сообщений с помощью команды /settings")

@dp.message(Command("settings"))
async def settings_handler(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="1 минута")],
            [types.KeyboardButton(text="1 час")],
            [types.KeyboardButton(text="3 часа")],
            [types.KeyboardButton(text="6 часов")],
            [types.KeyboardButton(text="12 часов")],
            [types.KeyboardButton(text="24 часа")],
            [types.KeyboardButton(text="Остановить отправку сообщений")],
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите интервал отправки сообщений:", reply_markup=keyboard)

@dp.message()
async def interval_selection_handler(message: types.Message):
    intervals = {"1 минута": 0, "1 час": 1, "3 часа": 3, "6 часов": 6, "12 часов": 12, "24 часа": 24}
    if message.text in intervals:
        cursor.execute("UPDATE users SET interval = ?, active = 1 WHERE user_id = ?", (intervals[message.text], message.from_user.id))
        conn.commit()
        await message.answer(f"Интервал установлен: {message.text}")
        schedule_messages()
    elif message.text == "Остановить отправку сообщений":
        cursor.execute("UPDATE users SET active = 0 WHERE user_id = ?", (message.from_user.id,))
        conn.commit()
        await message.answer("Отправка сообщений остановлена.")

async def main():
    scheduler.start()
    schedule_messages()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
