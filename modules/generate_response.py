import unidecode

if __name__ == "__main__":
    from AItranslater import *
    from dialoGPT import *
    from chatbot import get_chatterbot_response
    from calc import detect_calc
    from wikipedia_search import detect_search
    from get_time import detect_time
else:
    from modules.AItranslater import *
    from modules.dialoGPT import *
    from modules.chatbot import get_chatterbot_response
    from modules.calc import detect_calc
    from modules.wikipedia_search import detect_search
    from modules.get_time import detect_time


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

    # for blenderbot: botreply = str(botreply).replace('Sara','Byte').replace('byte','Byte').strip()
    #print(botreply)
    return botreply

if __name__ == "__main__":
    while 1:
        print(generate_response(input('Usuário: ')))
        input('Pressione qualquer tecla pra continuar')