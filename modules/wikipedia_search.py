import wikipedia
wikipedia.set_lang("pt")

search_init_list = ['o que e','o que foi','quem foi','quem e','quando foi','quando e','como e','pesquise','como foi','como aconteceu','onde']

def detect_search(input):
    for init in search_init_list:
        if input.startswith(init):
            return True
    return False

def wikipedia_search(query):
    query.replace('o que e','').replace('que foi','').replace('quem','').replace('quando','').replace('como','').replace('pesquise','').replace('sobre','').replace('onde','').replace('foi','').replace('aconteceu','')
    try:
        results = wikipedia.summary(query, sentences=1)
        results = results.replace('\n',' ').replace('  ',' ')
        return results
    except:
        return 'error'

if __name__ == "__main__":
    print(wikipedia_search(input('search: ')))