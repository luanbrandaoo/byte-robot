import unidecode

if __name__ == "__main__":
    from AItranslater import *
    from blenderbot import *
    from chatbot import get_response
    from calc import detect_calc
    from wikipedia_search import detect_search
else:
    from modules.AItranslater import *
    from modules.blenderbot import *
    from modules.chatbot import get_response
    from modules.calc import detect_calc
    from modules.wikipedia_search import detect_search


def generate_response(input):
    input_rem = unidecode.unidecode(input).strip().lower()
    botreply = get_response(input_rem)
    #print(botreply)
    if botreply == 'error':
        if detect_calc(input_rem) == True:
            botreply = 'execute_action{calculate()}'
        elif detect_search(input_rem) == True:
            botreply = 'execute_action{search()}'
        else:
            enInput = translateToEN(input)
            reply = blenderbot(enInput)
            PtReply = translateFromEN(reply)
            botreply = PtReply
            #print('English translation: '+enInput)
            #print('Generated response: '+reply)
            #print('Portuguese translation: '+PtReply)
    if 'execute_action' not in str(botreply):
        botreply=str(botreply)+" execute_action{emotion(neutral)}"
    botreply = str(botreply).replace('Sara','Byte').replace('byte','Byte').strip()
    return botreply

if __name__ == "__main__":
    while 1:
        print(generate_response(input('Usuário: ')))
        input('Pressione qualquer tecla pra continuar')