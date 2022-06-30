import logging

from aiogram import Dispatcher

from data.config import ADMINS_ID


async def on_startup_notify(dp: Dispatcher):
    try:
        await dp.bot.send_message(ADMINS_ID[0], "Бот Запущен")
    except Exception as err:
        logging.exception(err)
