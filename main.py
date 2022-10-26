from modules.generate_response import *
from modules.generate_voice import *
from modules.music import *
from modules.jokes import *
from modules.wikipedia_search import *
from modules.get_time import *
from modules.weather import *
from modules.calc import *
import json

def main(input):
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
  elif 'music(' in action:
    action_text = 'Ainda não consigo reproduzir músicas, mas vou conseguir no próximo update.'
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound)
  elif 'get_time(' in action:
    category = action.replace('get_time(','')[:-1]
    action_text = get_time(category)
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound)
  elif 'weather(' in action:
    category = action.replace('weather(','')[:-1]
    action_data = weather(category,'vassouras')
    action_execute = action_data[0]
    action_text = action_data[-1]
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound), "weather({})".format(action_execute)
  elif 'recognition(' in action:
    action_text = 'Ainda não consigo reconhecer pessoas, mas vou conseguir nos próximos updates.'
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound)
  elif 'calculate(' in action:
    action_text = calc(input)
    action_sound = generate_voice(action_text)
    return "print({})".format(action_text), "speak({})".format(action_sound)
  else:
    return action

if __name__ == "__main__":
  while 1:
    main(input("Digite o texto: "))
