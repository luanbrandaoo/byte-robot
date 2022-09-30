from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Byte',logic_adapters=['chatterbot.logic.BestMatch'],storage_adapter='chatterbot.storage.SQLStorageAdapter',database_uri='sqlite:///database.sqlite3')

conversa = ListTrainer(bot)

conversa.train(["Bom dia","Bom dia!"])
conversa.train(["Bom tarde","Boa tarde!"])
conversa.train(["Boa noite","Boa noite!"])
conversa.train(["Eai?","Eai, como vai?"])
conversa.train(["Eai?","O que deseja?"])
conversa.train(["Eai?","O que você quer?"])
conversa.train(["Olá","Oi"])
conversa.train(["Oi","Olá"])
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
conversa.train(["ande para o lado esquerdo","ok execute_action{move(left)}"])
conversa.train(["ande para o lado direito","ok execute_action{move(right)}"])
conversa.train(["ande para a frente","ok execute_action{move(front)}"])
conversa.train(["ande para trás","ok execute_action{move(back)}"])
conversa.train(["fique feliz","estou feliz execute_action{emotion(happy)}"])
conversa.train(["fique triste","por que tenho que ficar triste? execute_action{emotion(sad)}"])
conversa.train(["fique normal","estou normal execute_action{emotion(neutral)}"])
conversa.train(["vai chover hoje?","execute_action{weather(forecast_today)}"])
conversa.train(["vai chover amanhã?","execute_action{weather(forecast_tomorrow)}"])
