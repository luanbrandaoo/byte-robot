import unidecode

if __name__ == "__main__":
    from AItranslater import *
    from blenderbot import *
    from chatbot import get_response
    from calc import *
else:
    from modules.AItranslater import *
    from modules.blenderbot import *
    from modules.chatbot import get_response
    from modules.calc import *

calc_list = ['mais','menos','dividido','multiplicado','somado','diminuido','dividir','multiplica','com','sem','divisão','vezes','soma','tira','somado','subtraido','divisao','elevado','sobre','+','-','/','*','**']

def generate_response(input):
    input_rem = unidecode.unidecode(input).strip().lower()
    botreply = get_response(input_rem)
    #print(botreply)
    if botreply == 'error':
        if detect_calc(input) == True:
            botreply = 'execute_action{calculate()}'
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