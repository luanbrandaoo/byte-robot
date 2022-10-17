from chatterbot import ChatBot

if __name__ == "__main__":
    from AItranslater import *
    from DialoGPT import *
    database_uri = 'sqlite:///chatterbot_database.sqlite3'
else:
    from modules.AItranslater import *
    from modules.DialoGPT import *
    database_uri = 'sqlite:///modules/chatterbot_database.sqlite3'

chatbot = ChatBot('Byte',logic_adapters=['chatterbot.logic.BestMatch'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri=database_uri,read_only=True)

def generate_response(input):
    #print(input)
    botreply = chatbot.get_response(input)
    #print(botreply)
    #print(float(botreply.confidence))
    if float(botreply.confidence) < 0.7:
        enInput = translateToEN(input)
        reply = dialoGPT(enInput)
        PtReply = translateFromEN(reply)
        print('English translation: '+enInput)
        print('Generated response: '+reply)
        print('Portuguese translation: '+PtReply)
        return PtReply+" execute_action{emotion(neutral)}"
    else:
        if 'execute_action' not in str(botreply):
            botreply=str(botreply)+" execute_action{emotion(neutral)}"
        return str(botreply)

if __name__ == "__main__":
    while 1:
        print(generate_response(input('Usuário: ')))
        input('Pressione qualquer tecla pra continuar')