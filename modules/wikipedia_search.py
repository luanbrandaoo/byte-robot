import wikipedia
wikipedia.set_lang("pt")

def wikipedia_search(query):
    query.replace('que foi','').replace('quem','').replace('quando','').replace('como','').replace('pesquise','').replace('sobre','')
    try:
        results = wikipedia.summary(query, sentences=2)
        return "Encontrei na internet: "+results
    except:
        return 'error'

if __name__ == "__main__":
    print(wikipedia_search(input('search: ')))