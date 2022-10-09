from os import system
from pydub import AudioSegment
import base64

def generate_voice(input):
    print('voice generator input: '+input)
    system('espeak -vpt-brm2 -s130 "{}" -w .byte_voice.wav'.format(input))
    sound = AudioSegment.from_file('.byte_voice.wav', format="wav")
    new_sample_rate = int(sound.frame_rate * (1.3))
    hipitch_sound = sound._spawn(sound.raw_data, overrides={'frame_rate': new_sample_rate})
    hipitch_sound.export(".byte_voice.wav", format="wav")
    with open('.byte_voice.wav', 'rb') as binary_file:
        binary_file_data = binary_file.read()
        base64_encoded_data = base64.b64encode(binary_file_data)
        return str(base64_encoded_data)

if __name__ == "__main__":
    generate_voice(input("Digite o texto: "))