import os
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

def train():
	joeydash_bot = ChatBot(
		'JoeydashBot',
		filters=["chatterbot.filters.RepetitiveResponseFilter"]
	)
	# train basics
	joeydash_bot.set_trainer(ChatterBotCorpusTrainer)
	joeydash_bot.train(
		"./sample/corpus_recomended/"
		)
	# train my language
	joeydash_bot.set_trainer(ListTrainer)
	for filename in os.listdir('sample/un_trained/'):
		chats = open('./sample/un_trained/'+filename,'r').readlines()
		joeydash_bot.train(chats)

if __name__ == '__main__':
	train()
