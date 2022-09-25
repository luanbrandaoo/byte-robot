from chatterbot import ChatBot
bot = ChatBot('Bit',logic_adapters=['chatterbot.logic.BestMatch'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///database.sqlite3', read_only=True)
from AItranslater import *
from DialoGPT import *

def main(input):
    botreply = bot.get_response(input)
    print(botreply)
    print(botreply.confidence)
    if float(botreply.confidence) > 0.5:
        return botreply
    else:
        enInput = translateToEN(input)
        reply = dialoGPT(enInput)
        PtReply = translateFromEN(reply)
        return PtReply

if __name__ == "__main__":
    while 1:
        print(main(input('Usuário: ')))
        input('Pressione qualquer tecla pra continuar')