from flask import Flask, request, send_file
from main import *

app = Flask(__name__)

@app.route("/response", methods=["GET"])
def response():
  input = request.args.get("input")
  return main(input)
  #return send_file("voz.wav", mimetype="audio/wav", as_attachment=True, attachment_filename="voz.wav")
	
app.run(debug=True)