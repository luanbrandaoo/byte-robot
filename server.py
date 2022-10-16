from flask import Flask, request, send_file
from main import *

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
  return send_file('front-end/index.html')

@app.route('/images/<path:reqPath>')
def getImageFile(reqPath):
    return send_file('front-end/images/'+reqPath)

@app.route('/scripts/<path:reqPath>')
def getScriptFile(reqPath):
    return send_file('front-end/scripts/'+reqPath)

@app.route('/styles/<path:reqPath>')
def getStyleFile(reqPath):
    return send_file('front-end/styles/'+reqPath)

@app.route("/response", methods=["GET"])
def response():
  input = request.args.get("input")
  return main(input)

app.run(port=5000, debug=False)
