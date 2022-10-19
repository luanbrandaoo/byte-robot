from chatterbot import ChatBot

if __name__ == "__main__":
    from AItranslater import *
    from blenderbot import *
    database_uri = 'sqlite:///chatterbot_database.sqlite3'
else:
    from modules.AItranslater import *
    from modules.blenderbot import *
    database_uri = 'sqlite:///modules/chatterbot_database.sqlite3'

chatbot = ChatBot('Byte',logic_adapters=['chatterbot.logic.BestMatch'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri=database_uri)

def generate_response(input):
    botreply = chatbot.get_response(input)
    print(botreply.confidence)
    if float(botreply.confidence) < 0.6:
        enInput = translateToEN(input)
        reply = blenderbot(enInput)
        PtReply = translateFromEN(reply)
        botreply = PtReply
        print('English translation: '+enInput)
        print('Generated response: '+reply)
        print('Portuguese translation: '+PtReply)
    if 'execute_action' not in str(botreply):
        botreply=str(botreply)+" execute_action{emotion(neutral)}"
    return str(botreply)

if __name__ == "__main__":
    while 1:
        print(generate_response(input('Usuário: ')))
        input('Pressione qualquer tecla pra continuar')