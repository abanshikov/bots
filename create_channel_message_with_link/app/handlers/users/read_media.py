import logging

from aiogram import types
from aiogram.types import ContentType

from loader import dp

from data import config
from data.config import DEBUG


@dp.message_handler(content_types=(ContentType.PHOTO, ContentType.VIDEO))
async def add_video(message: types.Message):
    """
    Запись id переданных в бот медиафайлов.
    К каждому id медиафайла добавляется запись ":::photo" или ":::video" для
    дальнейшей идентификации типа медиафайла.
    :param message:
    :return:
    """
    match message.content_type:
        case 'photo':
            current_id = message.photo[-1].file_id + ':::photo'
        case 'video':
            current_id = message.video.file_id + ':::video'
        case _:
            logging.error(f"Ошибка добавления медиафайла. Тип фала: "
                          f"{message.content_type}")
            return

    if current_id not in config.media_ids:
        config.media_ids.append(current_id)

    if DEBUG:
        logging.info(config.media_ids)
