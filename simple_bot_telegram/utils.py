import shlex
import subprocess

import telegram

from config import TOKEN, SCRIPTS_DIR


def check_token():
    """
    Function to validate the token from config.py
    """
    bot = telegram.Bot(token=TOKEN)
    print(bot.get_me())


def run_command(command: str = None, file_name: str = None) -> str:
    """
    A function to run a script or command from the console.
    :return console output
    """
    if file_name:
        process = subprocess.Popen(f'{SCRIPTS_DIR}/{file_name}', shell=True, stdout=subprocess.PIPE)
    else:
        process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)

    text_output = ''
    while True:
        output = process.stdout.readline()
        output = output.decode('utf8')
        if output == '' and process.poll() is not None:
            break
        text_output = text_output + '\n' + output.strip()
    return text_output


def main():
    run_command(file_name='cpu_used.sh')


if __name__ == '__main__':
    main()
