import requests
import json


# Entrada e saída da internet
# Primeiro eu defino os parâmetros em um dicionário
parameters = {
	"q" : "Teste+1+2"
}

# Defino o endereço de destino em uma variável
url = "http://www.google.com"

# Realizo efetivamente o get ou o post, recebendo a resposta para tratar depois
req = requests.get (url, parameters)
json = req.json

arquivo = open ("./saida.html", "w")
arquivo.write (req.text)
arquivo.close()

