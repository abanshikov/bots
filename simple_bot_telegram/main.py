import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TOKEN
from utils import run_command

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


class Handlers:
    """
    All handlers must be registered with registration_handlers() in dictionary command_handlers.
    """

    def __init__(self):
        self.handlers = {
            'cpu': {
                'name': self.cpu,
                'description': "processor load %"
            },
            'df': {
                'name': self.df,
                'description': "disk space info (df -h)"
            },
            'free': {
                'name': self.free,
                'description': 'memori information (free -h)'
            },
            'help': {
                'name': self.help,
                'description': "command description",
            },
            'nginx_logs': {
                'name': self.nginx_logs,
                'description': 'get nginx logs'
            },
            'random': {
                'name': self.random,
                'description': "random number from 0 to 10",
            },
            'start': {
                'name': self.start,
                'description': "welcome command"
            },
        }

    def help(self, update, context):
        text = ''
        for item in self.handlers:
            text += f'/{item} - {self.handlers[item]["description"]}\n'
        context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    @staticmethod
    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Hello, I'm server bot, please enter the command!\n" +
                                      "/help - to view all commands.")

    @staticmethod
    def df(update, context):
        text_output = run_command(command="df -h")
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_output)

    @staticmethod
    def free(update, context):
        text_output = run_command(command="free -h")
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_output)

    @staticmethod
    def cpu(update, context):
        text_output = "CPU load: " + run_command(file_name='cpu_used.sh')
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_output)

    @staticmethod
    def random(update, context):
        text_output = "Random number from 0 to 10: " + run_command(file_name='rand_int.py')
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_output)

    @staticmethod
    def nginx_logs(update, context):
        text_output = "Nginx logs" + run_command(file_name='parser_logs.py')
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_output)

    @staticmethod
    def echo(update, context):
        """
        Method for entering plain text, not a command.
        :return None
        """
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Sorry, I understand only commands.\n" +
                                      "/help - to view all commands.")

    @staticmethod
    def unknown(update, context):
        """
        Method for handling unregistered command.
        :return None
        """
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Sorry, I didn't understand that command.\n" +
                                      "/help - to view all commands.")


def registration_handlers(dispatcher):
    """
    Registration of handlers. It is necessary to list all command handlers that are needed in the bot.
    :param: dispatcher - object for registration handlers
    :param: handlers - dictionary with all commands handlers for registration
    :return None
    """
    handlers = Handlers().handlers

    for handler in handlers:
        command_handler = CommandHandler(handler, handlers[handler]['name'])
        dispatcher.add_handler(command_handler)

    echo_handler = MessageHandler(Filters.text & (~Filters.command), Handlers().echo)
    unknown_handler = MessageHandler(Filters.command, Handlers().unknown)
    dispatcher.add_handler(echo_handler)
    dispatcher.add_handler(unknown_handler)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    registration_handlers(dispatcher=dispatcher)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
