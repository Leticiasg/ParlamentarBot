import requests
import json

def main():
    # my code here
	api_request("https://dadosabertos.camara.leg.br/api/v2/deputados?nome=bolsonaro&ordenarPor=nome","nome")

def api_request(url,info):
	response = requests.get(url)
	result = json.loads(response.content)
	for i in range(len(result['dados'])):
		print(result['dados'][i][info])

if __name__ == "__main__":
    main()
