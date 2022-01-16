from flask import Flask, request, Response
import requests
try:
    from config import Configuration, TOKEN, GITHUB_PAGE
except:
    from .config import Configuration, TOKEN, GITHUB_PAGE

app = Flask(__name__)
app.config.from_object(Configuration)
URL = f'https://api.telegram.org/bot{TOKEN}/'


def send_message(chat_id, text='Wait a second, please...'):
    url = URL + 'sendmessage'
    answer = {'chat_id': chat_id, 'text': text, }
    requests.get(url, params=answer)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        response = request.get_json()
        message = response['message']
        chat_id = message['chat']['id']
        message_text = message['text']

        if '/help' in message_text:
            text_weather = 'Hello! This is bot for testing webhooks telegram!\n' + \
                           f'See details {GITHUB_PAGE}'
            send_message(chat_id, text=text_weather)

        return Response('Ok', status=200)
    return '<h1>Bot welcomes you!</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
