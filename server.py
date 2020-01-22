import os

from flask import Flask, escape, request
from telepot import Bot

# Load the file env from default location
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Configure bot handler
TOKEN = os.environ['TELEGRAM_TOKEN']
bot = Bot(TOKEN)

app = Flask(__name__)

@app.route('/highscore/<int:from_id>/score/<int:score>')
def highscore(from_id: int, score: int):
    print(request, request.args)
    message_id = request.args.get('message_id')
    chat_id = request.args.get('chat_id')
    print(chat_id, from_id, message_id)
    bot.setGameScore(from_id, score, (chat_id, message_id))
    return 'ok'