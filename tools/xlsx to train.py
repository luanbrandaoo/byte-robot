import pandas as pd
import json

filename = 'falas byte.xlsx'

all = pd.ExcelFile(filename)
pages = all.sheet_names
list = []
dict = {}

for category in pages:
    lines = []
    file = pd.read_excel(filename, sheet_name=category)
    lines = file.values.tolist()
    a = 0

    for x in lines:
        if a==0:
            dict['patterns'] = []
            dict['responses'] = []
            dict['tag'] = category+str(a)
            dict['patterns'].append(x[0])
            dict['responses'].append(x[1])
        else:
            if x[1] == previous[1]:
                dict['patterns'].append(x[0])
            else:
                list.append(dict)
                dict = {}
                dict['patterns'] = []
                dict['responses'] = []
                dict['tag'] = 'cumprimentos'+str(a)
                dict['patterns'].append(x[0])
                dict['responses'].append(x[1])
            if a == len(lines)-1:
                list.append(dict)
        a = a + 1
        previous = x

final_dict = {}
final_dict['intents'] = list

with open('intends.json', 'w', encoding='utf8') as file:
     file.write(json.dumps(final_dict, ensure_ascii=False))