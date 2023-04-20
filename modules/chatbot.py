from chatterbot import ChatBot
import unicodedata
import re

from chatterbot import languages
languages.ENG.ISO_639_1 = "pt_core_news_lg"

if __name__ == "__main__":
	database_uri = 'sqlite:///chatterbot_database.sqlite3'
else:
	database_uri = 'sqlite:///modules/chatterbot_database.sqlite3'

chatbot = ChatBot('Byte',storage_adapter='chatterbot.storage.SQLStorageAdapter',read_only=True ,database_uri=database_uri)

def get_chatterbot_response(input):
	input_rem = re.sub('[^a-zA-Z0-9 \\\]', '', u"".join([c for c in unicodedata.normalize('NFKD', input) if not unicodedata.combining(c)])).strip().lower()
	botreply = chatbot.get_response(input_rem)
	print(botreply.confidence)
	if float(botreply.confidence) < 0.8:
		return "error"
	if 'execute_action' not in str(botreply):
		botreply=str(botreply)+" execute_action{emotion(neutral)}"
	return str(botreply)

if __name__ == "__main__":
	while 1:
		print(get_chatterbot_response(input('Usuário: ')))
		input('Pressione qualquer tecla pra continuar')