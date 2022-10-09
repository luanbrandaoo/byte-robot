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
    print(action)
    actions.append(action_processor(action,input))
  return json.dumps(actions,ensure_ascii=False).encode('utf8')

def action_processor(action,input):
  if 'joke(' in action:
    category = action.replace('joke(','')[:-1]
    action_text = jokes(category)
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound)
  elif 'search(' in action:
    search = input.replace('que foi','').replace('quem','').replace('quando','').replace('como','').replace('pesquise','').replace('sobre','')
    action_text = wikipedia_search(search)
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound)
  else:
    return action


if __name__ == "__main__":
    main(input("Digite o texto: "))
