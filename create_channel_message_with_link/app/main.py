import logging

from aiogram import executor

from loader import dp
import middlewares
import filters
import handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Установка дефолтных команд
    await set_default_commands(dispatcher)

    # Уведомление про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
