from flask import Flask, request, send_file
import main

app = Flask(__name__)

@app.route("/oi", methods=["GET"])
def oi():
  input = request.args.get("input")
  main(input)

  #return send_file("voz.wav", mimetype="audio/wav", as_attachment=True, attachment_filename="voz.wav")
	
app.run(debug=True)