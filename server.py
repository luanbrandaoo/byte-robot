from flask import Flask, request, send_file
from generate_response import *
from generate_voice import *
import json

def main(input):
  response = generate_response(input)
  if 'execute_action' not in response:
    response=response+" execute_action{emotion(neutral)}"
  speech = str(response.split('execute_action')[0])
  actions = []
  actions.append("print({})".format(speech))
  actions.append("speak({})".format(generate_voice(speech)))
  for x in response.split('execute_action')[1].replace('{','').replace('}','').split(','):
    actions.append(str(x))
  return json.dumps(actions,ensure_ascii=False).encode('utf8')


app = Flask(__name__)

@app.route("/response", methods=["GET"])
def response():
  input = request.args.get("input")
  return main(input)
  #return send_file("voz.wav", mimetype="audio/wav", as_attachment=True, attachment_filename="voz.wav")
	
app.run(debug=True)