import requests 
from json import load

with open('configurations.json') as f:
   credentialsfile = load(f)['openweathermap']

def weather(location):
    requisicao = requests.get("https://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&lang=pt_br")
    requisicao_dic = requisicao.json()
    print(requisicao_dic)

if __name__ == "__main__":
    print(weather("mendes"))