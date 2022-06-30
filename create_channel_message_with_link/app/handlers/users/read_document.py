import logging
import os
from pathlib import Path

from aiogram import types
import pandas as pd

from data.config import DEBUG, MessageText, Paths
from keyboards.inline.inline_keyboards import next_kbd
from loader import dp
from data import config


@dp.message_handler(content_types=types.ContentType.DOCUMENT)
async def save_document(message: types.Message):
    """
    Сохранение документа на диск
    :param message:
    :return:
    """
    raw_file_name = message.document.file_name
    file_name, file_extension = os.path.splitext(raw_file_name)
    if file_extension not in ['.xls', '.xlsx']:
        await message.answer(text=MessageText.save_document_error_extension)
        return

    # Сохранение файла на диск
    path_to_download = Path().joinpath(str(Paths.data_path), "posts")
    path_to_download.mkdir(parents=True, exist_ok=True)
    path_to_download = path_to_download.joinpath(message.document.file_name)
    await message.document.download(destination_file=path_to_download)
    if DEBUG:
        logging.info(f"Файл сохранён в: {path_to_download}")

    # Чтение данных
    if get_data_from_file(file_name=str(path_to_download)):
        await message.answer(text=MessageText.save_document_get_data,
                             reply_markup=next_kbd)
    else:
        await message.answer(text=MessageText.save_document_error_data)


def get_data_from_file(file_name: str) -> bool:
    """
    Получение данных из файла
    :param file_name:
    :return:
    """
    try:
        df = pd.read_excel(file_name)
        config.post['post_text'] = df.to_dict().get('Текст поста').get(0)
        config.post['urls'] = []
        for index in range(0, len(df.to_dict().get('Ссылка'))):
            config.post['urls'].append({
                'text': df.to_dict().get('Название ссылки').get(index),
                'url': df.to_dict().get('Ссылка').get(index),
            })
        return True
    except Exception as e:
        return False
