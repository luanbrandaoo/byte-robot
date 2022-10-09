import json
from random import choice, randint

with open('jokes.json', encoding='utf-8') as json_file:
	jokes_dict = json.load(json_file)

def jokes(category):
    if category == 'random':
        if randint(0, 10) > 7:
            category, joke = choice(list(jokes_dict.items()))
            print(category)
        else:
            category = "geral"
    return choice(jokes_dict[category])

if __name__ == "__main__":
    while 1:
        print(jokes(input('digite a categoria: ').lower().strip()))