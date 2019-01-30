import requests
import json

texto = requests.get("https://bit.ly/2Cu73N6").text
print ("Texto Original")
print (texto)


contador = {}
words = texto.split()
for word in words:
	contador.update ({word : 0})
for word in words:
	contador[word] += 1

print ("\nContador")
print (contador)
