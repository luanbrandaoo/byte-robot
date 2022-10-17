#from unicodedata import category
from modules.generate_response import *
from modules.generate_voice import *
from modules.music import *
from modules.jokes import *
from modules.wikipedia_search import *
import json

def main(input):
  response = generate_response(input)
  print(response)
  speech = str(response.split('execute_action')[0])
  actions = []
  if speech != '':
    actions.append("print({})".format(speech))
    actions.append("speak({})".format(generate_voice(speech)))
  for action in response.split('execute_action')[1].replace('{','').replace('}','').split(','):
    actions.append(action_processor(action,input))
  actions = str(actions)
  if actions.startswith('[('):
    actions = actions[2:-2]
  else:
    actions = actions[1:-1]
  actions = '"'+actions.replace(", '(",', "(').replace("), '",'), "').replace(")', ",')", ').replace(")\", '",')", "')[1:-1]+'"'
  return actions

def action_processor(action,input):
  if 'joke(' in action:
    category = action.replace('joke(','')[:-1]
    action_text = jokes(category)
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound)
  elif 'search(' in action:
    action_text = wikipedia_search(input)
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound)
  else:
    return action

if __name__ == "__main__":
  while 1:
    main(input("Digite o texto: "))
