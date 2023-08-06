import sys
from random import choice
sys.path.append("modules")

from generate_response import *
from generate_voice import *
from music import *
from jokes import *
from wikipedia_search import *
from get_time import *
from weather import *
from calc import *
import json

log_file = open('log.csv','a')
def log(input,actions):
  log_file.write(input+','+actions)
  log_file.write('\n')


def main(input):
  input = input.strip().lower()
  response = generate_response(input)
  #print(response)
  speech = response.split('execute_action')[0].strip().capitalize()
  if len(speech) > 1:
    if speech[-1] not in ['.','!', '?']:
      #print(speech)
      #print(speech[-1])
      speech = speech+'.'
  actions = []
  if speech != '':
    actions.append("print({})".format(speech))
    actions.append("speak({})".format(generate_voice(speech)))
  if 'execute_action' not in response:
    response=response+" execute_action{emotion(neutral)}"
  actionlist = response.split("execute_action")[1].replace('{','').replace('}','').split(',')
  for action in actionlist:
    actions.append(action_processor(action,input))
  actions = str(actions)
  if actions.startswith('[('):
    actions = actions[2:-2]
  else:
    actions = actions[1:-1]
  actions = '"'+actions.replace(", '(",', "(').replace("), '",'), "').replace(")', ",')", ').replace(")\", '",')", "')[1:-1]+'"'
  log(input,actions)
  return actions

def action_processor(action,input):
  if 'joke(' in action:
    category = action.replace('joke(','')[:-1]
    action_text = jokes(category)
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound),"emotion(happy)"
  elif 'search(' in action:
    action_text, action_image = wikipedia_search(input)
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound), "search()" ,"image({})".format(action_image)
  elif 'music(' in action:
    action_text = 'Ainda não consigo reproduzir músicas, mas vou conseguir nos próximos updates.'
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound),"emotion(sad)"
  elif 'get_time(' in action:
    category = action.replace('get_time(','')[:-1]
    action_text = get_time(category)
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound),"emotion(neutral)"
  elif 'weather(' in action:
    category = action.replace('weather(','')[:-1]
    if 'aftertm' in category:
      if 'depois' not in input or ' pós' not in input:
        category = 'tomorrow'
    action_data = weather(category,'vassouras')
    action_execute = action_data[0]
    action_text = action_data[1]
    action_mode = action_data[2]
    if action_mode == 'weather':
      action_execute = "weather({})".format(action_data[0])
    else:
      action_execute = "temperature({})".format(action_data[0])
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound), action_execute
  elif 'recognition(' in action:
    action_text = 'Ainda não consigo reconhecer pessoas, mas vou conseguir nos próximos updates.'
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound),"emotion(sad)"
  elif 'calculate(' in action:
    action_text = calc(input)
    action_sound = generate_voice(calc_voice(action_text))
    return "print({})".format(action_text), "speak({})".format(action_sound),"emotion(neutral)"
  elif 'move(' in action:
    action_text = 'Claro!'
    action_sound = generate_voice(action_text)
    action_mode = action[5:-1]
    if action_mode == 'side':
      action_mode = choice(['right','left'])
    return "print({})".format(action_text), "speak({})".format(action_sound),"emotion(happy)",f"move({action_mode})"
  else:
    return action

if __name__ == "__main__":
  while 1:
    main(input("Digite o texto: "))
