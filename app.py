# import os
from flask import Flask, render_template, request
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

app = Flask(__name__)

joeydash_bot = ChatBot(
    'JoeydashBot',
    storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
    database = "joeydash",
    database_uri = "mongodb://joeydash:joeydash@ds135790.mlab.com:35790/joeydash",
    filters=["chatterbot.filters.RepetitiveResponseFilter"]
)

@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/train")
# def train():
    # joeydash_bot.set_trainer(ChatterBotCorpusTrainer)
    # joeydash_bot.train(
    #     "chatterbot.corpus.english.conversations"
    # )
    # joeydash_bot.set_trainer(chatterbot.trainers.ListTrainer)
    # for filename in os.listdir('static/sample'):
    #     chats = open('./static/sample/'+filename,'r').readlines()
    #     joeydash_bot.train(chats)
    # return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    try:
        return str(joeydash_bot.get_response(userText))
    except Exception:
        return str("I didn't get you")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
