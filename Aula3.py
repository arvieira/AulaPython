import requests
import json
from collections import Counter

# Em Python posso importar parte de um pacote usando o comando acima. Aqui indica
# que do pacote collections, ele só vai importar a classe Counter.
# Essa classe conta automaticamente elementos em listas.
print ("\nExemplo 1:")
lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)

contador = Counter(lista)
print (contador)



# Para imprimir as keys de um dicionário
# Mas esse método retorna um objeto chamado dict_keys e não uma lista 
# A diferença entre dict_keys e uma lista é que a lista é carregada inteira na memória
# quando fazendo uma busca. Já o dict_keys, ele carrega uma chave por vez na memória, 
# gastando mto menos e sendo mto mais rápido.
print ("\nExemplo 2:")
print (contador.keys())
print (contador.values())	# O mesmo serve para os valores
print (contador.items())	# Items é a tupla chave valor



# Para o acesso aos elementos da tupla, é semelhante a trabalhar com uma lista
print ("\nExemplo 3:")
for item in contador.items():
	print ("Tupla:", item[0], item[1])



# Posso desmembrar a minha tupla no for
print ("\nExemplo 4:")
for chave, valor in contador.items():
	print ("\nChave:", chave)
	print ("Valor:", valor)



# Tupla de um elemento só: Eu posso definir uma tupla com um elemento só da seguinte maneira
# Esse exemplo gera um erro pq a tupla foi mal formada. Na hora de fazer o unpack do for, 
# chegando na última tupla, essa não tem o elemento necessário para preencher a variável valor
# print ("\nExemplo 5:")
# lista_tuplas = [(1, 2), (2, 3), (3, )]
# for chave, valor in lista_tuplas:
#	print (chave, valor)
