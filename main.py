from unicodedata import category
from generate_response import *
from generate_voice import *
from jokes import *
import json

def main(input):
  response = generate_response(input)
  speech = str(response.split('execute_action')[0])
  actions = []
  if speech != '':
    actions.append("print({})".format(speech))
    actions.append("speak({})".format(generate_voice(speech)))
  for action in response.split('execute_action')[1].replace('{','').replace('}','').split(','):
    actions.append(actions(action))
  return json.dumps(actions,ensure_ascii=False).encode('utf8')

def actions(action):
  if 'joke(' in action:
    category = action.replace('joke(','')[:-1]
    return "speak({})".format(generate_voice(jokes(category)))


if __name__ == "__main__":
    main(input("Digite o texto: "))
