from chatbot import get_chatbot_response
from AItranslater import *
from DialoGPT import *

def main(input):
    botreply = get_chatbot_response(input)
    print(botreply)
    if botreply == 'error'
        enInput = translateToEN(input)
        reply = dialoGPT(enInput)
        PtReply = translateFromEN(reply)
        return PtReply
    else:
        return botreply
        

if __name__ == "__main__":
    while 1:
        print(main(input('Usuário: ')))
        input('Pressione qualquer tecla pra continuar')