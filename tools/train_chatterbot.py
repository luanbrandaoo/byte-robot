from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import csv

bot = ChatBot('Byte',logic_adapters=['chatterbot.logic.BestMatch'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///chatterbot_database.sqlite3')
bot_en = ChatBot('Byte',logic_adapters=['chatterbot.logic.BestMatch','chatterbot.logic.MathematicalEvaluation'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///chatterbot_database_en.sqlite3')

corpus = ChatterBotCorpusTrainer(bot)
corpus_en = ChatterBotCorpusTrainer(bot_en)

corpus.train('chatterbot.corpus.portuguese')
#corpus_en.train('chatterbot.corpus.english')

conversa = ListTrainer(bot)

def trainbot(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for conversation in data:
        conversa.train(conversation)

trainbot('cumprimentos.csv')
trainbot('perguntas e respostas.csv')
trainbot('ativar comandos.csv')

print('treinamento realizado.')