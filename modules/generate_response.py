from ast import Return
import unidecode
from random import choice

if __name__ == "__main__":
    from AItranslater import *
    from blenderbot import *
    from chatbot import get_response
    from calc import detect_calc
    from wikipedia_search import detect_search
    from get_time import detect_time
else:
    from modules.AItranslater import *
    from modules.blenderbot import *
    from modules.chatbot import get_response
    from modules.calc import detect_calc
    from modules.wikipedia_search import detect_search
    from modules.get_time import detect_time

def detect_name(input):
    for x in ['seu nome','voce se chama','quem e voce']:
        if x in input:
            return True
    return False

def generate_response(input):
    input_rem = unidecode.unidecode(input).strip().lower()
    if detect_name(input_rem) == True:
        botreply = choice(['Meu nome é Byte.','Me chamo Byte.','Sou o Byte.'])
    elif detect_time(input_rem) == True:
        print("get time")
        botreply = 'execute_action{get_time(time)}'
    else:
        botreply = get_response(input_rem)
    #print(botreply)
    if botreply == 'error':
        enInput = translateToEN(input)
        reply = blenderbot(enInput)
        PtReply = translateFromEN(reply)
        botreply = PtReply
        #print('English translation: '+enInput)
        #print('Generated response: '+reply)
        #print('Portuguese translation: '+PtReply)
    botreply = str(botreply).replace('Sara','Byte').replace('byte','Byte').strip()
    #print(botreply)
    return botreply

if __name__ == "__main__":
    while 1:
        print(generate_response(input('Usuário: ')))
        input('Pressione qualquer tecla pra continuar')