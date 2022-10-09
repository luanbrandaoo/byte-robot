#from unicodedata import category
from generate_response import *
from generate_voice import *
from music import *
from jokes import *
from wikipedia_search import *
import json

def main(input):
  response = generate_response(input)
  speech = str(response.split('execute_action')[0])
  actions = []
  if speech != '':
    actions.append("print({})".format(speech))
    actions.append("speak({})".format(generate_voice(speech)))
  for action in response.split('execute_action')[1].replace('{','').replace('}','').split(','):
    actions.append(actions(action,input))
  return json.dumps(actions,ensure_ascii=False).encode('utf8')

def actions(action,input):
  if 'joke(' in action:
    category = action.replace('joke(','')[:-1]
    return "speak({})".format(generate_voice(jokes(category)))
  if 'search(' in action:
    search = input.replace('que foi','').replace('quem','').replace('quando','').replace('como','').replace('pesquise','').replace('sobre','')
    return "speak({})".format(generate_voice(wikipedia_search(search)))


if __name__ == "__main__":
    main(input("Digite o texto: "))
