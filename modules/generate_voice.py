from os import system
from pydub import AudioSegment
import base64

if __name__ == "__main__":
    cache_voice_file='.cache/.byte_voice.wav'
else:
    cache_voice_file='modules/.cache/.byte_voice.wav'

def generate_voice(input):
    #print('voice generator input: '+input)
    input = input.replace("'",'').replace('"','')
    print(input)
    system('espeak -vpt-brm2 -s130 "{}" -w {}'.format(input,cache_voice_file))
    sound = AudioSegment.from_file(cache_voice_file, format="wav")
    new_sample_rate = int(sound.frame_rate * (1.3))
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    hipitch_sound.export(cache_voice_file, format="wav")
    with open(cache_voice_file, 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        return str(base64_encoded_data)

if __name__ == "__main__":
    generate_voice(input("Digite o texto: "))