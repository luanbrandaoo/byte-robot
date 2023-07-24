import unidecode
from random import choice

from AItranslater import *
from dialoGPT import *
from chatbot import get_chatterbot_response
from calc import detect_calc
from wikipedia_search import detect_search
from get_time import detect_time

error_responses = ["Desculpe, não entendi"]

def generate_response(input):
    input_rem = unidecode.unidecode(input).strip().lower()
    input_rem2 = input_rem.replace('?','').replace('.','').replace(',','').replace('!','')

    botreply = get_chatterbot_response(input_rem)
    print(botreply)

    if botreply == 'error':
        if detect_calc(input_rem2) == True:
            botreply = 'execute_action{calculate()}'
        elif detect_search(input_rem2) == True:
            botreply = 'execute_action{search()}'
        elif detect_time(input_rem2) == True:
            botreply = 'execute_action{get_time(time)}'
        else:
            enInput = translateToEN(input)
            reply = dialoGPT(enInput)
            PtReply = translateFromEN(reply)
            botreply = PtReply
            #print('English translation: '+enInput)
            #print('Generated response: '+reply)
            #print('Portuguese translation: '+PtReply)
        
        if botreply.strip() == '':
            botreply = choice(error_responses)
    return botreply

if __name__ == "__main__":
    while 1:
        print(generate_response(input('Usuário: ')))
        input('Pressione qualquer tecla pra continuar')