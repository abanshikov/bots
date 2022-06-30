from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    """
    Эхо хендлер, куда летят текстовые сообщения без указанного состояния.
    :param message:
    :return:
    """
    await message.answer(f"Простите, но я не знаю как обработать команду: \n"
                         f"{message.text}")

