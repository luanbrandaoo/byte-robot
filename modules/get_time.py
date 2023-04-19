from datetime import datetime
from random import choice, getrandbits
from num2words import num2words

month_name = ["janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro"]
weekday_name = ["domingo","segunda","terça","quarta","quinta","sexta","sábado"]
weekday_complete_name = ["domingo","segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sábado"]

time_response_list = ["Agora são %H horas e %M minutos.","São %H horas e %M minutos.","Agora são *%Hhour**%Mminutes*.","São *%Hhour**%Mminutes*.","Agora são %H:%M. Tenha *greeting*.","Agora são %H horas e %M minutos. Tenha *greeting*.","Agora são *%Hhour**%Mminutes*. Tenha *greeting*."]
date_response_list = ["Hoje é dia %d de *%mmonth*.","Hoje é dia *%dday* de *%mmonth*.","Estamos no dia %d de *%mmonth*.","Estamos no dia *%dday* de *%mmonth*.","Hoje é *%wweekdayy*, dia %d de *%mmonth*.","Hoje é *%wweekdayy*, *%dday* de *%mmonth*."]
weekday_response_list = ["Hoje é *%wweekdayy*.", "*%wweekdayy*.", "Hoje é *%wweekdayy*, dia *%dday*.", "*%wweekdayy*, dia *%dday*."]
year_response_list = ["Estamos no ano de %Y.","Estamos no ano %Y.","Estamos no ano de *%Yyear*.","Estamos em %Y.","%Y.","Estamos em *%Yyear*."]

time_command_list = ['horas sao','quantas horas','horas agora','que horas sao']

def detect_time(input):
  for x in time_command_list:
    if input in x:
      return True
  return False

def get_time(response):
    if response == 'time':
      response = choice(time_response_list)
    elif response == 'date':
      response = choice(date_response_list)
    elif response == 'weekday':
      response = choice(weekday_response_list)
    elif response == 'year':
      response = choice(year_response_list)
    response = datetime.now().strftime(str(response))
    if "*greeting*" in response:
        number = int(datetime.now().strftime("%H"))
        if 0<=number<6:
            greeting = "uma boa madrugada"
        elif 6<=number<12:
            greeting = "uma bom dia"
        elif 12<=number<18:
            greeting = "uma boa tarde"
        elif 18<=number:
            greeting = "uma boa noite"
        response = response.replace("*greeting*",greeting)
    if "weekdayy*" in response:
        index = response.index('weekdayy*')
        number = int(response[index-1:index])
        if bool(getrandbits(1)) == True:
          weekday = weekday_complete_name[number-1]
        else:
          weekday = weekday_name[number-1]
        response = response[:index-2]+weekday+response[index+9:]
    if "day*" in response:
        index = response.index('day*')
        number = response[index-2:index]
        if number == '01': 
          days = 'primeiro'
        else:
          days = num2words(number,lang='pt-br')
        response = response[:index-3]+days+response[index+4:]
    if "year*" in response:
        index = response.index('year*')
        number = response[index-4:index]
        years = num2words(number,lang='pt-br')
        response = response[:index-5]+years+response[index+5:]
    if "hour*" in response:
        index = response.index('hour*')
        number = response[index-2:index]
        if number == '00': 
          hours = 'meia-noite'
        elif number == '01':
          hours = 'uma hora'
        elif number == '02':
          hours = 'duas horas'
        elif number == '21':
          hours = 'vinte e uma horas'
        elif number == '22':
          hours = 'vinte e duas horas'
        else:
          hours = num2words(number,lang='pt-br')+' horas'
        response = response[:index-3]+hours+response[index+5:]
    if "minutes*" in response:
        index = response.index('minutes*')
        number = response[index-2:index]
        if number == '00':
          minutes = ''
        elif number == '01':
          minutes = ' e um minuto'
        else:
          minutes = ' e '+num2words(number,lang='pt-br')+' minutos'
        response = response[:index-3]+minutes+response[index+8:]
    if "month*" in response:
        index = response.index('month*')
        number = int(response[index-2:index])
        month = month_name[number-1]
        response = response[:index-3]+month+response[index+6:]
    
    response.replace('dezasseis','dezesseis')
    return response.capitalize()

if __name__ == '__main__':
  print(get_time('time'))
  print(get_time('date'))
  print(get_time('weekday'))
  print(get_time('year'))