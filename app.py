from flask import Flask, render_template, request
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

app = Flask(__name__)

joeydash_bot = ChatBot(
        'JoeydashBot',
        filters=["chatterbot.filters.RepetitiveResponseFilter"]
    )

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    try:
        return str(joeydash_bot.get_response(userText))
    except Exception:
        return str("I didn't get you")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
