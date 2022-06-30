import os
from dataclasses import dataclass
from pathlib import Path

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS_ID = env.list("ADMINS_ID")
CHANNELS_ID = env.list("CHANNELS_ID")
IP = env.str("IP")

# Основные настройки
DEBUG = False
SAVE_FILE = True

# Текст кнопок
NEXT = 'Продолжить🪄️'
CREATE_POST = 'Опубликовать пост➡'
CANCEL = 'Начать заново'
ADD_POST = 'Добавить пост 📘'


@dataclass
class MessageText:
    """
    Тексты сообщений
    """
    begin_create_post: str = f'Отлично, приступаем к созданию поста! Для ' \
        f'начала отправьте мне фотографию 📷 или видео 🎥 для создания поста, ' \
        f'либо отправьте мне файл с шаблоном поста (как в файле примера⬆️).'

    cancel: str = f'Хорошо, введите данные сначала!\nЧто бы приступить к ' \
                  f'созданию поста нажмите кнопку ниже.'

    demonstrate_post: str = f'Отлично👍 всё получилось!\nЕсли в получившемся ' \
        f'⬆️ посте всё устраивает, то можно отправить его в канал, нажав ' \
        f'кнопку {CREATE_POST}!'

    no_admin: str = f"Простите, но у Вас нет доступа к отправке постов."

    save_document_get_data: str = f'Файл получен! Если все данные (фото, ' \
        f'видео, шаблон поста) добавлены, нажмите кнопку {NEXT}'

    save_document_error_data: str = f'Простите, но Вы добавили файл с ' \
        f'данными отличающимися от шаблона🥺 \nВажно, что бы названия ' \
        f'столбцов были как в шаблоне, соблюдался порядок столбцов и т.д.\n' \
        f'Попробуйте отправить ещё один файл!'

    save_document_error_extension: str = f'Простите, но вы добавили файл в ' \
        f'не верном формате🥺 \nДолжен быть добавлен <b>excel</b> файл, т.е. ' \
        f'в формате <code>xls</code> или <code>xlsx</code>\nПопробуйте ' \
        f'отправить ещё один файл!'

    send_post_to_channel: str = f'Пост успешно отправлен в канал!\n' \
                                f'Создать ещё один пост?'

    start: str = f'Привет!\nВы запустили бота 🤖 для добавления поста 📘 ' \
        f'в канал, что бы приступить к созданию поста нажмите кнопку ' \
        f'{ADD_POST}.'


@dataclass
class Paths:
    __current_file = os.path.abspath(__file__)
    __current_path = "/".join(__current_file.split('/')[:-1])
    data_path = str(Path(__current_path))
    example_file = Path().joinpath(data_path, "posts", "Пример поста.xlsx")


# Хранение данных
media_ids: list = []
post = {}


if __name__ == '__main__':
    print(Paths.data_path)
