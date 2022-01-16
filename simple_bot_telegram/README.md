# Simple telegram bot
Telegram bot based on [python-telegram-bot](https://pypi.org/project/python-telegram-bot/). Convenient for running commands on the server or running scripts.
Before starting work:
1. Register a telegram bot via @BotFather
2. Write the received token into the file **config.py**
3. Clone this repository to your server.
4. Install the required dependencies from **requirements.txt**. It is recommended to use a virtual environment.
5. Enter and register the necessary commands or scripts bash or python in the directory **./scripts**
6. After creating scripts in the folder **./scripts** they need to be given execution rights:
```
$ chmod +x ./scripts/my_script.py
```
7. Run the application in the background, for example via [screen](https://en.wikipedia.org/wiki/GNU_Screen)