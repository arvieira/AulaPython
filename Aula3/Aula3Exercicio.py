import requests
import json
from collections import Counter

texto = requests.get("https://bit.ly/2Cu73N6").text
print ("Texto Original")
print (texto)
print ("\n")

# Uma string é uma lista de caracteres. Logo, se eu usar o contador diretamente na string
# terei um problema de que ele vai contar letra por letra e não palavras. Então, preciso
# cortar a string que contem o texto em uma lista de palavras usando o método split da string.
# Desse modo, posso usar o contador logo após.
words = texto.split()
contador = Counter(words)
print (contador)
print ("\n")
print (contador.most_common(10))
print ("\n")

# Por padrão o separador do split é o espaço ou o tab. Eu posso mudar esse delimitador.
exemplo = "Teste | BLBL | nada"
lista_exemplo = exemplo.split(" | ")
print (lista_exemplo)
print ("\n")

