from pynput import keyboard
import speech_recognition as sr  

def mic():
        microfone = sr.Recognizer()
        with sr.Microphone() as source:
                microfone.adjust_for_ambient_noise(source)
                print("Diga alguma coisa: ")
                audio = microfone.listen(source)
                try:
                        frase = microfone.recognize_google(audio,language='pt-BR')
                        print("Você disse: " + frase)
                except:
                        print("Não entendi")
        return frase

def main():
        mic()

def on_release(key):
        if key == keyboard.Key.enter:
                print('enter')
                main()

def movefront():
        keyboard.press('w')

def moveback():
        keyboard.press('s')

def turnright():
        keyboard.press('d')

def turnleft():
        keyboard.press('a')

listener = keyboard.Listener(on_release = on_release)
listener.start()
listener.join()

