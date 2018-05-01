import os
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

def train():
	joeydash_bot = ChatBot(
	    'JoeydashBot',
	    filters=["chatterbot.filters.RepetitiveResponseFilter"]
	)
	# train basics
    joeydash_bot.set_trainer(ChatterBotCorpusTrainer)
    joeydash_bot.train(
        "chatterbot.corpus.english"
    )
    # train my language
    # joeydash_bot.set_trainer(chatterbot.trainers.ListTrainer)
    # for filename in os.listdir('static/sample'):
    #     chats = open('./static/sample/'+filename,'r').readlines()
    #     joeydash_bot.train(chats)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=3000)