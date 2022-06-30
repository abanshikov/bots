from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import ADD_POST, NEXT, CANCEL, CREATE_POST

btn_add_post = InlineKeyboardButton(text=ADD_POST, callback_data=ADD_POST)
btn_next = InlineKeyboardButton(text=NEXT, callback_data=NEXT)
btn_cancel = InlineKeyboardButton(text=CANCEL, callback_data=CANCEL)
btn_create_post = InlineKeyboardButton(text=CREATE_POST,
                                       callback_data=CREATE_POST)

start_kbd = InlineKeyboardMarkup(row_width=1).add(btn_add_post)
next_kbd = InlineKeyboardMarkup(row_width=2).add(btn_next, btn_cancel)
cancel_kbd = InlineKeyboardMarkup(row_width=1).add(btn_cancel)
create_kbd = InlineKeyboardMarkup(row_width=2).add(btn_create_post, btn_cancel)
