print('Carregando...')

from AItranslater import *
from DialoGPT import *

print('Carregado!')

while 1:
    print(translateFromEN(dialoGPT(translateToEN(input('Usuário: ')))))
    input('Pressione qualquer tecla pra continuar')