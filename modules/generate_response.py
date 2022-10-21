import unicodedata
import re

if __name__ == "__main__":
    from AItranslater import *
    from blenderbot import *
    from chatbot import get_response
else:
    from modules.AItranslater import *
    from modules.blenderbot import *
    from modules.chatbot import get_response

def generate_response(input):
    input_rem = re.sub('[^a-zA-Z0-9 \\\]', '', u"".join([c for c in unicodedata.normalize('NFKD', input) if not unicodedata.combining(c)])).strip().lower()
    botreply = get_response(input_rem)
    if botreply == 'error':
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