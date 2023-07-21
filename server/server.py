from flask import Flask, request, send_file
import os
from main import *

app = Flask(__name__)

front_end_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'front_end'))

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return send_file(os.path.join(front_end_path, 'index.html'))

@app.route('/assets/<path:reqPath>')
def getImageFile(reqPath):
    return send_file(os.path.join(front_end_path, 'assets', reqPath))

@app.route('/scripts/<path:reqPath>')
def getScriptFile(reqPath):
    return send_file(os.path.join(front_end_path, 'scripts', reqPath))

@app.route('/styles/<path:reqPath>')
def getStyleFile(reqPath):
    return send_file(os.path.join(front_end_path, 'styles', reqPath))

@app.route("/response", methods=["GET"])
def response():
    input = request.args.get("input")
    return main(input)

app.run(port=8080, debug=False)
