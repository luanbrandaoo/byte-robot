from chatterbot import ChatBot

if __name__ == "__main__":
    from AItranslater import *
    from DialoGPT import *
    database_uri = 'sqlite:///chatterbot_database.sqlite3'
else:
    from modules.AItranslater import *
    from modules.DialoGPT import *
    database_uri = 'sqlite:///modules/chatterbot_database.sqlite3'

chatbot = ChatBot('Byte',logic_adapters=['chatterbot.logic.BestMatch','chatterbot.logic.MathematicalEvaluation','chatterbot.logic.TimeLogicAdapter'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri=database_uri)

def generate_response(input):
    botreply = chatbot.get_response(input)
    if float(botreply.confidence) < 0.6:
        enInput = translateToEN(input)
        reply = chatbot.get_response(enInput)
        if float(reply.confidence) < 0.6:
            reply = dialoGPT(enInput)
            reply = translateFromEN(reply)
            print('English translation: '+enInput)
            print('Generated response: '+reply)
            print('Portuguese translation: '+PtReply)
        else:
            print('Chatbot americano: '+reply)
    if 'execute_action' not in str(botreply):
        botreply=str(botreply)+" execute_action{emotion(neutral)}"
    return str(botreply)

if __name__ == "__main__":
    while 1:
        print(generate_response(input('Usuário: ')))
        input('Pressione qualquer tecla pra continuar')