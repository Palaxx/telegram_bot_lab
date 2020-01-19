from flask import Flask, escape, request


app = Flask(__name__)

@app.route('/highscore/<int:chat_id>/score/<int:score>')
def hello(chat_id: int, score: int):
    return str(chat_id) + ' - '+str(score)