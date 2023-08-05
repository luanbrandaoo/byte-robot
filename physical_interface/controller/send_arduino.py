from send_images import send_image
import os

weather_icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), './', 'weather_icons'))

def send_emotion(s,emotion):
    if emotion == 'happy':
        send = 'emotionhap'
    elif emotion == 'sad':
        send = 'emotionsad'
    elif emotion == 'neutral':
        send = 'emotionneu'
    
    while 1:
        s.write(send.encode())
        if str(s.readline().decode()).strip() == 'emotion':
            print("Emoção enviada")
            break 

def loading_icon(s):
    while 1:
        s.write('loadingico'.encode())
        if str(s.readline().decode()).strip() == 'loading':
            print("Carregando...")
            break 

def black_screen(s):
    while 1:
        s.write('blackscree'.encode())
        if str(s.readline().decode()).strip() == 'black':
            print("tela preta")
            break 

def send_actions(s,input):
    #create action list
    inputs_raw = input.split('", ')
    actions = []
    for x in inputs_raw:
        if x.startswith('"'):
            x = x[1:]
        if x.endswith('"'):
            x = x[:-1] 
        actions.append(x)
    
    for action in actions:
        if action.startswith('emotion'):
            emotion = action[8:-1]
            send_emotion(s,emotion)
        
        if action.startswith('speak(') == False:
            print(action)

        if action.startswith('weather('):
            emotion = action[8:-1]
            send_weather(s,emotion)
        
        if action.startswith('move('):
            emotion = action[5:-1]
            move(s,emotion)

def send_weather(s,weather):
    black_screen(s)
    
    if weather == 'chovendo_dia' or weather == 'chovendo_noite' or weather == 'chuviscando' or weather == 'chovendo':
        icon = 'chuviscando'
    elif weather == 'nublado' or weather == 'parcialmente nublado' or weather == 'nevando' or weather == 'neblinado':
        icon = 'nublado'
    else:
        icon = weather
    
    icon = icon+'.png'
    
    print(os.path.join(weather_icon_path, icon))
    send_image(s,os.path.join(weather_icon_path, icon))

def move(s,side):
    global send
    if side == 'front':
        send = 'movefrontt'
    elif side == 'back':
        send = 'movebackkk'
    elif side == 'right':
        send = 'moverightt'
    elif side == 'left':
        send = 'movelefttt'
    
    while 1:
        s.write(send.encode())
        if str(s.readline().decode()).strip() == 'move':
            print("Movimento enviado")
            break 