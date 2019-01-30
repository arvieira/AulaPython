import requests
import json
from collections import Counter

# Em Python posso importar parte de um pacote usando o comando acima. Aqui indica
# que do pacote collections, ele só vai importar a classe Counter.
# Essa classe conta automaticamente elementos em listas.

lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)

contador = Counter(lista)
print (contador)
