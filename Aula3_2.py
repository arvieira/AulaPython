import requests
import json
from collections import Counter


print ("\nExemplo 1:")
lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)
texto = requests.get("https://bit.ly/2Cu73N6").text

# Funções em Python
# As funções em python começam com a palavra reservada def
# Por padrão o Python nao se preocupa com tipos de variáveis, logo não preciso nem definir o 
# tipo do parâmetro nem o tipo de retorno
def quadrado (x):
	return x*x

# Chamada da função que foi definida.
print (quadrado(10))



def maisFrequente (lista):
	if type(lista) == str:
		lista = lista.split()

	contador = Counter(lista)
	return contador.most_common(10)

print ("\n", maisFrequente(lista))
print ("\n", maisFrequente(texto))
