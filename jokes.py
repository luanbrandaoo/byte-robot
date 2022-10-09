import json
from random import choice

with open('jokes.json', encoding='utf-8') as json_file:
	jokes_dict = json.load(json_file)

def jokes(category):
    if category == 'random':
        return choice(jokes_dict['geral'])
    else:
        return choice(jokes_dict[category])

if __name__ == "__main__":
    print(jokes(input('digite a categoria: ').lower().strip()))