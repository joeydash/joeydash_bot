import os

from chatterbot import ChatBot
from app import joeydash_bot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


def train():
    trainer = ChatterBotCorpusTrainer(joeydash_bot)
    trainer.train(
        "sample/grow90/mp.yml"
    )
    # trainer.train(
    #     "chatterbot.corpus.english"
    # )
    # train basics
    # joeydash_bot.set_trainer(ChatterBotCorpusTrainer)
    # joeydash_bot.train(
    #     "sample/data/english/"
    # )
    # train my language
    # trainer = ListTrainer(joeydash_bot)
    # for filename in os.listdir('sample/un_trained/'):
    #     chats = open('./sample/un_trained/' + filename, 'r').readlines()
    #     trainer.train(chats)


if __name__ == '__main__':
    train()
