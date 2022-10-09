from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Byte',logic_adapters=['chatterbot.logic.BestMatch'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///chatterbot_database.sqlite3')

conversa = ListTrainer(bot)

#greetings
conversa.train(["Bom dia","Bom dia!"])
conversa.train(["Bom tarde","Boa tarde!"])
conversa.train(["Boa noite","Boa noite!"])
conversa.train(["Eai?","Eai, como vai?"])
conversa.train(["Eai?","O que deseja?"])
conversa.train(["Eai?","O que você quer?"])
conversa.train(["Olá","Oi"])
conversa.train(["Oi","Olá"])
conversa.train(["Opa","Olá"])
conversa.train(["Saudações!","Olá"])
conversa.train(["Olá","Saudações!"])
conversa.train(["Salve","Salve!"])
conversa.train(["E ai como vai?","Bem"])
conversa.train(["E ai como vai?","Bem"])
conversa.train(["E ai como vai?","Ótimo"])
conversa.train(["E ai como vai?","Bem, e você?"])
conversa.train(["Como vai você?","Bem"])
conversa.train(["Como vai você?","Bem, e você?"])
conversa.train(["Como vai você?","Muito bem, obrigado"])
conversa.train(["Prazer em conhecê-lo","Obrigado, digo o mesmo"])
conversa.train(["Como vai?","Eu estou bem"])
conversa.train(["Como vai?","Eu estou bem. Como você está?"])
conversa.train(["É um prazer te conhecer","Obrigado. Você também"])
conversa.train(["E aí beleza?","Beleza"])
conversa.train(["E aí brother?","E aí bro!"])
conversa.train(["Tudo bom?","Melhor agora"])
conversa.train(["Tudo bom?","Tudo, e você?"])
conversa.train(["E aí cara?","Tudo bom?","Tudo de bom e você?","Tudo bem"])
conversa.train(["E aí mano?","Tudo bom?"])
conversa.train(["Quanto tempo!","Como vai?","Vou bem","Que ótimo!"])
conversa.train(["E ai mano","E ai, como vai você?"])
conversa.train(["E ai brother","E ai, como vai você?"])
conversa.train(["E ai irmão","E ai, como vai você?"])
conversa.train(["E ai amigo","E ai, como vai você?"])
#replies
conversa.train(["quem é você?","Sou o Byte, um robô criado para te ajudar"])
conversa.train(["qual é seu nome?","Meu nome é Byte"])
conversa.train(["qual seu nome?","Meu nome é Byte"])
#jokes
conversa.train(["conte uma piada","execute_action{joke(random)}"])
conversa.train(["me conte uma piada","execute_action{joke(random)}"])
conversa.train(["conte uma coisa engraçada","execute_action{joke(random)}"])
conversa.train(["fale uma piada","execute_action{joke(random)}"])
conversa.train(["fale uma coisa engraçada","execute_action{joke(random)}"])
conversa.train(["conte uma piada de plantas","execute_action{joke(plantas)}"])
conversa.train(["me conte uma piada sobre plantas","execute_action{joke(plantas)}"])
conversa.train(["conte uma piada de animais","execute_action{joke(animais)}"])
conversa.train(["me conte uma piada sobre animais","execute_action{joke(animais)}"])
conversa.train(["conte uma piada de games","execute_action{joke(games)}"])
conversa.train(["me conte uma piada sobre games","execute_action{joke(games)}"])
conversa.train(["conte uma piada de jogos","execute_action{joke(games)}"])
conversa.train(["me conte uma piada sobre jogos","execute_action{joke(games)}"])
conversa.train(["conte uma piada de informatica","execute_action{joke(informatica)}"])
conversa.train(["me conte uma piada sobre informatica","execute_action{joke(informatica)}"])
conversa.train(["conte uma piada de computadores","execute_action{joke(informatica)}"])
conversa.train(["me conte uma piada sobre computadores","execute_action{joke(informatica)}"])
conversa.train(["conte uma piada de computação","execute_action{joke(informatica)}"])
conversa.train(["me conte uma piada sobre computação","execute_action{joke(informatica)}"])
conversa.train(["conte uma piada de carros","execute_action{joke(carros)}"])
conversa.train(["me conte uma piada sobre carros","execute_action{joke(carros)}"])
conversa.train(["conte uma piada de veículos","execute_action{joke(carros)}"])
conversa.train(["me conte uma piada sobre veículos","execute_action{joke(carros)}"])
conversa.train(["conte uma piada de automóveis","execute_action{joke(carros)}"])
conversa.train(["me conte uma piada sobre automóveis","execute_action{joke(carros)}"])
conversa.train(["conte uma piada de filmes","execute_action{joke(filmes)}"])
conversa.train(["me conte uma piada sobre filmes","execute_action{joke(filmes)}"])
conversa.train(["conte uma piada de cinema","execute_action{joke(filmes)}"])
conversa.train(["me conte uma piada sobre cinema","execute_action{joke(filmes)}"])
conversa.train(["conte uma piada de comida","execute_action{joke(comida)}"])
conversa.train(["me conte uma piada sobre comida","execute_action{joke(comida)}"])
conversa.train(["conte uma piada de alimentos","execute_action{joke(comida)}"])
conversa.train(["me conte uma piada sobre alimentos","execute_action{joke(comida)}"])
conversa.train(["conte uma piada de pontinho","execute_action{joke(pontinho)}"])
conversa.train(["me conte uma piada sobre pontinhos","execute_action{joke(pontinho)}"])
conversa.train(["conte uma piada de biologia","execute_action{joke(biologia)}"])
conversa.train(["me conte uma piada sobre biologia","execute_action{joke(biologia)}"])
conversa.train(["conte uma piada de medicina","execute_action{joke(biologia)}"])
conversa.train(["me conte uma piada sobre medicina","execute_action{joke(biologia)}"])
conversa.train(["conte uma piada de remédio","execute_action{joke(remedio)}"])
conversa.train(["me conte uma piada sobre remédios","execute_action{joke(remedio)}"])
conversa.train(["conte uma piada de farmácia","execute_action{joke(remedio)}"])
conversa.train(["me conte uma piada sobre farmácia","execute_action{joke(remedio)}"])
conversa.train(["conte uma piada de filosofia","execute_action{joke(filosofia)}"])
conversa.train(["me conte uma piada sobre filosofia","execute_action{joke(filosofia)}"])
conversa.train(["conte uma piada de filósofos","execute_action{joke(filosofia)}"])
conversa.train(["me conte uma piada sobre filósofos","execute_action{joke(filosofia)}"])
conversa.train(["conte uma piada de história","execute_action{joke(historia)}"])
conversa.train(["me conte uma piada sobre história","execute_action{joke(historia)}"])
conversa.train(["conte uma piada histórica","execute_action{joke(historia)}"])
conversa.train(["conte uma piada de português","execute_action{joke(portugues)}"])
conversa.train(["me conte uma piada sobre português","execute_action{joke(portugues)}"])
conversa.train(["conte uma piada de língua portuguesa","execute_action{joke(portugues)}"])
conversa.train(["me conte uma piada sobre língua portuguesa","execute_action{joke(portugues)}"])
conversa.train(["conte uma piada de geografia","execute_action{joke(geografia)}"])
conversa.train(["me conte uma piada sobre geografia","execute_action{joke(geografia)}"])
conversa.train(["conte uma piada geografica","execute_action{joke(geografia)}"])
conversa.train(["conte uma piada de astronomia","execute_action{joke(astronomia)}"])
conversa.train(["me conte uma piada sobre astronomia","execute_action{joke(astronomia)}"])
conversa.train(["conte uma piada astronomica","execute_action{joke(astronomia)}"])
conversa.train(["conte uma piada de espaço","execute_action{joke(astronomia)}"])
conversa.train(["me conte uma piada sobre espaço","execute_action{joke(astronomia)}"])
conversa.train(["conte uma piada de física","execute_action{joke(fisica)}"])
conversa.train(["me conte uma piada sobre física","execute_action{joke(fisica)}"])
conversa.train(["conte uma piada de química","execute_action{joke(quimica)}"])
conversa.train(["me conte uma piada sobre química","execute_action{joke(quimica)}"])
conversa.train(["conte uma piada de matemática","execute_action{joke(matematica)}"])
conversa.train(["me conte uma piada sobre matemática","execute_action{joke(matematica)}"])
conversa.train(["conte uma piada de álgebra","execute_action{joke(matematica)}"])
conversa.train(["me conte uma piada sobre álgebra","execute_action{joke(matematica)}"])
conversa.train(["conte uma piada de música","execute_action{joke(musica)}"])
conversa.train(["me conte uma piada sobre música","execute_action{joke(musica)}"])
conversa.train(["conte uma piada de musical","execute_action{joke(musica)}"])
conversa.train(["conte uma piada de cúmulo","execute_action{joke(cumulo)}"])
conversa.train(["me conte uma piada sobre cúmulo","execute_action{joke(cumulo)}"])
#actions
conversa.train(["ande para o lado esquerdo","ok execute_action{move(left)}"])
conversa.train(["ande para o lado direito","ok execute_action{move(right)}"])
conversa.train(["ande para a frente","ok execute_action{move(front)}"])
conversa.train(["ande para trás","ok execute_action{move(back)}"])
conversa.train(["fique feliz","estou feliz execute_action{emotion(happy)}"])
conversa.train(["fique triste","por que tenho que ficar triste? execute_action{emotion(sad)}"])
conversa.train(["fique normal","estou normal execute_action{emotion(neutral)}"])
#weather
conversa.train(["choverá hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["choverá amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["vai chover hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["vai chover amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["fará sol hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["fará sol amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["vai fazer sol hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["vai fazer sol amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["nevará hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["nevará amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["vai nevar hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["vai nevar amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["será que choverá hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["será que choverá amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["será que vai chover hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["será que vai chover amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["será que fará sol hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["será que fará sol amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["será que vai fazer sol hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["será que vai fazer sol amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["será que nevará hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["será que nevará amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["será que vai nevar hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["será que vai nevar amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["você sabe se choverá hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["você sabe se choverá amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["você sabe se vai chover hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["você sabe se vai chover amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["você sabe se fará sol hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["você sabe se fará sol amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["você sabe se vai fazer sol hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["você sabe se vai fazer sol amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["você sabe se nevará hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["você sabe se nevará amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["você sabe se vai nevar hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["você sabe se vai nevar amanhã?","execute_action{weather(forecast_tomorrow)}"])
conversa.train(["qual a temperatura?","execute_action{weather(temperature_today)}"])
conversa.train(["qual a temperatura hoje?","execute_action{weather(temperature_today)}"])
conversa.train(["qual a temperatura amanhã?","execute_action{weather(temperature_tomorrow)}"])
conversa.train(["qual será a temperatura amanhã?","execute_action{weather(temperature_tomorrow)}"])
#search
conversa.train(["quem foi","execute_action{search()}"])
conversa.train(["quem é","execute_action{search()}"])
conversa.train(["quando foi","execute_action{search()}"])
conversa.train(["quando foi","execute_action{search()}"])
conversa.train(["como foi","execute_action{search()}"])
conversa.train(["pesquise","execute_action{search()}"])
conversa.train(["quem foi","execute_action{search()}"])
#recognition
conversa.train(["quem sou eu?","execute_action{recognition()}"])
conversa.train(["qual é meu nome?","execute_action{recognition()}"])
conversa.train(["quem está falando contigo?","execute_action{recognition()}"])
#music
conversa.train(["toque uma musica","execute_action{music()}"])
conversa.train(["toque a musica","execute_action{music()}"])
conversa.train(["toque","execute_action{music()}"])
conversa.train(["tocar uma musica","execute_action{music()}"])
conversa.train(["tocar a musica","execute_action{music()}"])
conversa.train(["reproduza","execute_action{music()}"])
conversa.train(["reproduzir uma musica","execute_action{music()}"])
conversa.train(["reproduzir a musica","execute_action{music()}"])
conversa.train(["quero ouvir a musica","execute_action{music()}"])
conversa.train(["quero ouvir uma musica","execute_action{music()}"])
conversa.train(["quero ouvir a canção","execute_action{music()}"])
conversa.train(["quero ouvir uma canção","execute_action{music()}"])
conversa.train(["toque uma canção","execute_action{music()}"])
conversa.train(["toque a canção","execute_action{music()}"])
conversa.train(["tocar uma canção","execute_action{music()}"])
conversa.train(["tocar a canção","execute_action{music()}"])

print('treinamento realizado.')