import requests 
from json import load
from datetime import datetime

today_weather_list = ['Agora o tempo está {} em {}']
tomorrow_weather_list = ['Amanhã, o tempo estará {} em {}']
aftertm_weather_list = ['Depois de amanhã, o tempo estará {} em {}']
today_temp_list = ['Agora a temperatura é de {}°C em {}']
tomorrow_temp_list = ['Amanhã, a média de temperatura será de {}°C em {}']
aftertm_temp_list = ['Depois de amanhã, a média de temperatura será de {}°C em {}']

if __name__ == "__main__":
    credentials_file='credentials.json'
else:
    credentials_file='modules/credentials.json'

with open(credentials_file) as f:
   openweathermap = load(f)['openweathermap']

def weather(mode,location):
    if mode.endswith('today') == False:
        if 'tomorrow' in mode:
            day = 1
        elif 'aftertm' in mode:
            day = 2
        requisicao = requests.get("https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}".format(location,openweathermap))
        location = requisicao.json()['city']['name']
        weather_list = requisicao.json()['list']
        for x in weather_list:
            if x['dt_txt'].startswith(datetime.now().strftime("%Y-%m-{}".format(int(datetime.now().strftime("%d"))+day))) and '12:00:00' in x['dt_txt']:
                temp = x['main']['temp']
                weather = x['weather'][0]['id']
                break
        if mode.startswith('temperature'):
            celsius = int(temp)-273
            if day == 1:
                speakresponse = tomorrow_temp_list[0].format(celsius,location)
            else:
                speakresponse = aftertm_temp_list[0].format(celsius,location)
            return celsius,speakresponse
        else:
            if day == 1:
                speakresponse = tomorrow_weather_list[0].format(weather,location)
            else:
                speakresponse = aftertm_weather_list[0].format(weather,location)
            return weather,speakresponse
    else:
        requisicao = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location,openweathermap))
        location = requisicao.json()['name']
        if mode.startswith('forecast'):
            weather = int(requisicao.json()['weather'][0]['id'])
            speakresponse = today_weather_list[0].format(weather,location)
            return weather,speakresponse
        if mode.startswith('temperature'):
            celsius = (int(requisicao.json()['main']['temp']))-273
            speakresponse = today_temp_list[0].format(celsius,location)
            return celsius,speakresponse

if __name__ == "__main__":
    print(weather('temperature_aftertm',"vassouras"))