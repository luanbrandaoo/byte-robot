from generate_response import *
from generate_voice import *
import json

def main(input):
  response = generate_response(input)
  speech = str(response.split('execute_action')[0])
  actions = []
  actions.append("print({})".format(speech))
  actions.append("speak({})".format(generate_voice(speech)))
  for x in response.split('execute_action')[1].replace('{','').replace('}','').split(','):
    actions.append(str(x))
  return json.dumps(actions,ensure_ascii=False).encode('utf8')

if __name__ == "__main__":
    main(input("Digite o texto: "))
