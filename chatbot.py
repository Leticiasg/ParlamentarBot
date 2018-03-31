# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from api_request import api_request
def main():
    # my code here
	bot = instanceBot()
	trainBot(bot)
	welcomeConversation()
	
def instanceBot():
	# Create a new instance of a ChatBot
	chatbot = ChatBot(
		"ParlamentarBot",
		storage_adapter='chatterbot.storage.MongoDatabaseAdapter',
		logic_adapters=[
			"chatterbot.logic.BestMatch"
		],
		database='chatterbot-database'
	)
	return chatbot

def trainBot(chatbot):
	conversation = ['oi', 'olá', 'olá', 'bom dia', 'bom dia, como vai?', 'estou bem']
	chatbot.set_trainer(ListTrainer)
	chatbot.train(conversation)

def welcomeConversation():
	print("Olá! Sou o ParlamentarBot. Com a ajuda da iniciativa Dados Abertos, posso trazer a você muitas informações sobre a atuação dos nossos deputados federais e senadores! Para começar, me pergunte qual são os senadores do seu estado.")
	question = input('Você: ')
	api_request("https://dadosabertos.camara.leg.br/api/v2/deputados?nome=bolsonaro&ordenarPor=nome","nome")
	#response = chatbot.get_response(question)
	#print('ParlamentarBot:',response)

if __name__ == "__main__":
	main()
