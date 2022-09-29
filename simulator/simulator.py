from pynput import keyboard
from vosk import Model, KaldiRecognizer
import pyaudio

model = Model('pt')
recognizer = KaldiRecognizer(model, 16000)
cap = pyaudio.PyAudio()

def main():
        stream = cap.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
        stream.start_stream()
        data = stream.read(4096)
        print(recognizer.Result())

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

