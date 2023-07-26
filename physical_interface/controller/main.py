from flask import Flask, request, send_file
import os
from ports import serial_ports
import serial
from time import sleep
from send_images import send_image
from send_arduino import send_actions, loading_icon, send_emotion
import requests
import webbrowser

available_ports = serial_ports()
print('Portas disponíveis:')
print(available_ports)

while 1:
    com_port = str(input('Digite a porta conectada ao Byte: ').strip().upper())
    if com_port in available_ports:
        break
    else:
        print('Porta inválida. Tente novamente.')

s = serial.Serial(com_port, 150000, timeout=5)

main_server = input('Digite a URL e porta do servidor: ').strip()

app = Flask(__name__)

front_end_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..', 'front_end'))

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
    loading_icon(s)
    input_request = request.args.get("input")
    output_request = requests.get(f'{main_server}/response?input={input_request}').content
    send_actions(s,output_request.decode())
    return output_request

webbrowser.open('http://127.0.0.1:5000')
send_emotion(s,'neutral')
app.run(host="127.0.0.1", port=5000, debug=False)