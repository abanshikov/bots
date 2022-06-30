import logging
from data.config import SAVE_FILE


FILE_NAME = "history.log"
CONSOLE_LEVEL = logging.INFO
FILE_LEVEL = logging.INFO


if SAVE_FILE:
    logging.basicConfig(
        filename=FILE_NAME,
        format=u'%(levelname)s:\t[%(filename)s] [LINE:%(lineno)s] [%(asctime)s]:\t%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=FILE_LEVEL,
    )
else:
    logging.basicConfig(
        format=u'%(levelname)s:\t[%(filename)s] [LINE:%(lineno)s] [%(asctime)s]:\t%(message)s',
        datefmt='%H:%M',
        level=CONSOLE_LEVEL,
    )
