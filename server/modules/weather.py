import requests 
from json import load
from datetime import datetime

today_weather_list = ['Agora está {} em {}']
tomorrow_weather_list = ['Amanhã, estará {} em {}']
aftertm_weather_list = ['Depois de amanhã, estará {} em {}']
today_temp_list = ['Agora a temperatura é de {}°C em {}']
tomorrow_temp_list = ['Amanhã, a média de temperatura será de {}°C em {}']
aftertm_temp_list = ['Depois de amanhã, a média de temperatura será de {}°C em {}']

if __name__ == "__main__":
    credentials_file='credentials.json'
else:
    credentials_file='modules/credentials.json'

with open(credentials_file) as f:
   openweathermap = load(f)['openweathermap']

def format_weather(weather):
    if 200 <= weather < 300:
        weather_name = 'trovejando'
    elif 300 <= weather < 500:
        weather_name = 'chuviscando'
    elif 500 <= weather < 519:
        weather_name = 'chovendo'
    elif 519 <= weather < 600:
        weather_name = 'chovendo forte'
    elif 600 <= weather < 700:
        weather_name = 'nevando'
    elif 700 <= weather < 800:
        weather_name = 'neblinado'
    elif weather == 800:
        weather_name = 'limpo'
    elif 801 <= weather < 803:
        weather_name = 'parcialmente nublado'
    elif 803 <= weather < 805:
        weather_name = 'nublado'
    return weather_name

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
                weather = int(x['weather'][0]['id'])
                weather_name = format_weather(weather)
                '''if weather_name == 'chovendo':
                    weather_name = weather_name+'_dia'''
                break
        if mode.startswith('temperature'):
            celsius = int(temp)-273
            if day == 1:
                speakresponse = tomorrow_temp_list[0].format(celsius,location)
            else:
                speakresponse = aftertm_temp_list[0].format(celsius,location)
            return celsius,speakresponse,'temperature'
        else:
            if day == 1:
                speakresponse = tomorrow_weather_list[0].format(weather_name,location)
            else:
                speakresponse = aftertm_weather_list[0].format(weather_name,location)
            return weather_name,speakresponse,'weather'
    else:
        requisicao = requests.get("https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(location,openweathermap))
        location = requisicao.json()['name']
        if mode.startswith('forecast'):
            weather = int(requisicao.json()['weather'][0]['id'])
            weather_name = format_weather(weather)
            speakresponse = today_weather_list[0].format(weather_name,location)
            '''if weather_name == 'chovendo':
                if 6 < int(datetime.now().strftime("%H")) < 18:
                    weather_name = weather_name+'_dia'
                else:
                    weather_name = weather_name+'_noite'''
            return weather_name,speakresponse,'weather'
        if mode.startswith('temperature'):
            celsius = (int(requisicao.json()['main']['temp']))-273
            speakresponse = today_temp_list[0].format(celsius,location)
            return celsius,speakresponse,'temperature'

if __name__ == "__main__":
    print(weather('forecast_today',"vassouras"))