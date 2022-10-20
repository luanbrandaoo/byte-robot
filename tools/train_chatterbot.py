from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import csv
import unicodedata
import re

bot = ChatBot('Byte',logic_adapters=['chatterbot.logic.BestMatch'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///chatterbot_database.sqlite3')

#bot_en = ChatBot('Byte',logic_adapters=['chatterbot.logic.BestMatch','chatterbot.logic.MathematicalEvaluation'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///chatterbot_database_en.sqlite3')

corpus = ChatterBotCorpusTrainer(bot)
#corpus_en = ChatterBotCorpusTrainer(bot_en)

corpus.train('chatterbot.corpus.portuguese')
#corpus_en.train('chatterbot.corpus.english')

conversa = ListTrainer(bot)

def trainbot(file):
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    for conversation in data:
        conversation_formatted = []
        conversation_formatted.append(re.sub('[^a-zA-Z0-9 \\\]', '', u"".join([c for c in unicodedata.normalize('NFKD',conversation[0]) if not unicodedata.combining(c)])).strip().lower())
        conversation_formatted.append(conversation[1].lower().strip())
        print(conversation_formatted)
        conversa.train(conversation_formatted)

trainbot('cumprimentos.csv')
trainbot('perguntaserespostas.csv')
trainbot('ativarcomandos.csv')

print('treinamento realizado.')