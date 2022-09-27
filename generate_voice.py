from os import system
from pydub import AudioSegment

def generate_voice(input):
    system('espeak -vpt-brm2 -s130 "{}" -w byte_voice.wav'.format(input))
    sound = AudioSegment.from_file('byte_voice.wav', format="wav")
    new_sample_rate = int(sound.frame_rate * (1.3))
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    hipitch_sound.export("byte_voice.wav", format="wav")

if __name__ == "__main__":
    generate_voice(input("Digite o texto: "))