
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
        