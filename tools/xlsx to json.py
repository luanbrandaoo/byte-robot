import pandas as pd
import simplejson

filename = 'piadas byte.xlsx'

all = pd.ExcelFile(filename)
pages = all.sheet_names
dict = {}

for category in pages:
    lines = []
    file = pd.read_excel(filename, sheet_name=category)
    lines = file.values.tolist()
    liness = []
    for x in lines:
        x = str(x)
        if x.lower() != 'null' and x.lower() != '[nan]':
            liness.append(x.replace("['",'').replace("']",''))
    dict[category] = liness

with open('jokes.json', 'w', encoding='utf-8') as fp:
    dictt = simplejson.dumps(dict, ignore_nan=True, ensure_ascii=False)
    dictt = dictt.replace(r'[\"','').replace(r'\"]','')
    fp.write(dictt)