import os

from flask import Flask, escape, request
from flask_cors import CORS
from telepot import Bot

# Load the file env from default location
from dotenv import load_dotenv
load_dotenv(verbose=True)

# Configure bot handler
TOKEN = os.environ['TELEGRAM_TOKEN']
bot = Bot(TOKEN)

app = Flask(__name__)

# This allow cors on all routes for all origin and methods. This should not be done in a production enviroment
CORS(app)


@app.route('/highscore/<int:from_id>/score/<int:score>')
def highscore(from_id: int, score: int):
    # Retrieve ids from query string
    message_id = request.args.get('message_id')
    chat_id = request.args.get('chat_id')
    bot.setGameScore(from_id, score, (chat_id, message_id))
    return 'ok'


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)