import datetime
import math
import requests
import json

print ("Exemplo 1:")
print (math.sqrt(121))
print (math.log(math.e))
print (math.cos(math.pi))


print ("\nExemplo 2:")
print (sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1,]))
print (math.fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1,]))


print ("\nExemplo 3:")
lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)
print (lista)


print ("\nExemplo 4:")
numbers = {}
for i in range(101):
	numbers.update({i : 0})
for i in lista:
	numbers[i] += 1

print (numbers)



# Comentários:
# A seção dos imports devem estar separada do resto do código por pelo menos 
# uma linha. De preferência, usar duas linhas.
#
# O ponto flutuante do python possui um erro de arredondamento, de modo que 
# somando 10 vezes 0.1, você não obtem 1 e sim 0,99999999.
# No entanto, a biblioteca math possui o método fsum, o qual é mais preciso 
# que o sum propriamente dito nativo da linguagem.
#
# Em Python, quando se quer indicar números decimais, nos quais a parte inteira
# é zero, basta utilizar .1 ou .2 ou etc. Não precisa colocar o zero, assim como
# é feito na engenharia. 
#
# Git linha de comando:
# git config --global user.email "andreribeirovieira@gmail.com"
# git config --global user.name "Andre"
# git add TesteGit.py
# git commit ===> Ele irá pedir uma msg pelo nano
# git push ===> Ele irá pedir o usuário e a senha
# 
