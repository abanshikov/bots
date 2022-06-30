import logging
from aiogram.utils.exceptions import (TelegramAPIError,
                                      MessageNotModified,
                                      CantParseEntities)

from loader import dp


@dp.errors_handler()
async def errors_handler(update, exception):
    """
    Exceptions handler. Catches all exceptions within task factory tasks.
    :param update:
    :param exception:
    :return: stdout logging
    """

    if isinstance(exception, MessageNotModified):
        # do something here?
        logging.error('Message is not modified')
        return True

    if isinstance(exception, CantParseEntities):
        # or here
        logging.error(f'CantParseEntities: {exception} \nUpdate: {update}')
        return True

    #  MUST BE THE  LAST CONDITION (ЭТО УСЛОВИЕ ВСЕГДА ДОЛЖНО БЫТЬ В КОНЦЕ)
    if isinstance(exception, TelegramAPIError):
        logging.error(f'TelegramAPIError: {exception} \nUpdate: {update}')
        return True

    # At least you have tried.
    logging.error(f'Update: {update} \n{exception}')
