from chatterbot import ChatBot
from AItranslater import *
from DialoGPT import *
chatbot = ChatBot('Byte',logic_adapters=['chatterbot.logic.BestMatch'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///database.sqlite3',read_only=True)

def generate_response(input):
    print(input)
    botreply = chatbot.get_response(input)
    print(botreply)
    print(float(botreply.confidence))
    if float(botreply.confidence) < 0.7:
        enInput = translateToEN(input)
        reply = dialoGPT(enInput)
        PtReply = translateFromEN(reply)
        return PtReply
    else:
        return str(botreply)
        

if __name__ == "__main__":
    while 1:
        print(generate_response(input('Usuário: ')))
        input('Pressione qualquer tecla pra continuar')