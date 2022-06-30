from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import MessageText
from keyboards.inline import start_kbd
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text=MessageText.start, reply_markup=start_kbd)

