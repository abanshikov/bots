import logging

from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.exceptions import TelegramAPIError

from data.config import ADMINS_ID, NEXT, CANCEL, ADD_POST, CHANNELS_ID, \
    CREATE_POST, MessageText, Paths
from keyboards.inline import start_kbd
from keyboards.inline.inline_keyboards import cancel_kbd, create_kbd
from loader import dp, bot
from data import config


async def send_post(call: types.CallbackQuery, chat_id: str):
    """
    Формирование и отправка поста.
    :param call:
    :param chat_id:
    :return:
    """
    text = config.post.get('post_text')
    keyboard_links = InlineKeyboardMarkup()
    for item in config.post.get('urls'):
        keyboard_links.add(InlineKeyboardButton(
            text=item.get('text'),
            url=item.get('url'),
        ))

    # Выбор вида отправки в зависимости от прикреплённых медиафайлов
    if config.media_ids:
        # Добавлен один медиафайл
        current_id, type_media = config.media_ids[0].split(':::')
        if type_media == 'photo':
            await bot.send_photo(chat_id=chat_id,
                                 photo=current_id,
                                 caption=text,
                                 reply_markup=keyboard_links)
        elif type_media == 'video':
            await bot.send_video(chat_id=chat_id,
                                 video=current_id,
                                 caption=text,
                                 reply_markup=keyboard_links)
    else:
        # Медиафайлы не были добавлены
        await call.message.answer(text=text, reply_markup=keyboard_links)


@dp.callback_query_handler(text=CANCEL)
async def cancel(call: types.CallbackQuery):
    """
    Отмена ввода данных
    """
    await call.answer(cache_time=5)

    config.media_ids = []
    config.post = {}
    await call.message.answer(text=MessageText.cancel, reply_markup=start_kbd)


@dp.callback_query_handler(text=ADD_POST)
async def begin_create_post(call: types.CallbackQuery):
    """
    Начало создания поста. Проверка, что сообщение послал администратор.
    """
    await call.answer(cache_time=5)

    if str(call.from_user.id) not in ADMINS_ID:
        await call.message.answer(text=MessageText.no_admin)
        return

    example_document = open(str(Paths.example_file), 'rb')
    await call.message.answer_document(document=example_document,
                                       caption=MessageText.begin_create_post,
                                       reply_markup=cancel_kbd)


@dp.callback_query_handler(text=NEXT)
async def demonstrate_post(call: types.CallbackQuery):
    """
    Формирование поста
    """
    await call.answer(cache_time=5)
    await send_post(call, call.from_user.id)
    await call.message.answer(text=MessageText.demonstrate_post,
                              reply_markup=create_kbd)


@dp.callback_query_handler(text=CREATE_POST)
async def send_post_to_channel(call: types.CallbackQuery):
    """
    Отправка сформированного поста в канал
    """
    await call.answer(cache_time=5)
    for channel_id in CHANNELS_ID:
        try:
            await send_post(call, channel_id)
        except TelegramAPIError:
            logging.error(f'Ошибка отправки поста в канал {channel_id}')

    config.media_ids = []
    config.post = {}
    await call.message.answer(text=MessageText.send_post_to_channel,
                              reply_markup=start_kbd)

