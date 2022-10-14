import requests 
from json import load

if __name__ == "__main__":
    credentials_file='credentials.json'
else:
    credentials_file='modules/credentials.json'

with open(credentials_file) as f:
   openweathermap = load(f)['openweathermap']

def weather(location):
    try:
        requisicao = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location,openweathermap))
        requisicao_dic = requisicao.json()['weather'][0]['main']
        return requisicao_dic
    except:
        return 'error'

if __name__ == "__main__":
    print(weather("mendes"))