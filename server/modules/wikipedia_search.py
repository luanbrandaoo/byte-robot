import wikipedia
from random import choice

wikipedia.set_lang("pt")

search_init_list = ['o que e','o que foi','quem foi','quem e','quando foi','quando e','como e','pesquise','como foi','como aconteceu','onde']
error_responses = ["Desculpe, não consegui encontrar"]


def detect_search(input):
    for init in search_init_list:
        if init in input:
            return True
    return False

def wikipedia_search(query):
    query = query.replace('o que e','').replace('que foi','').replace('quem','').replace('quando','').replace('como','').replace('pesquise','').replace('sobre','').replace('onde','').replace('foi','').replace('aconteceu','').replace('diga','').replace('fale','').replace('explique','').replace('me','').replace('quem','').strip()
    print('wikipedia_search: '+query)
    try:
        results = wikipedia.summary(query, sentences=1)
        results = results.replace('\n',' ').replace('  ',' ')
        return results
    except:
        return choice(error_responses)

if __name__ == "__main__":
    print(wikipedia_search(input('search: ')))