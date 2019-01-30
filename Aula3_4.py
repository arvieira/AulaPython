import requests
import json
from Aula3_3 import maisFrequente


# Observe a forma como é importada uma função específica de um outro arquivo
# Se utiliza a linha from Aula3_3 import maisFrequente
# Aula3_3 é o nome do arquivo sem a extensão
# maisFrquente é o nome da função que eu estou importando
lista = json.loads(requests.get("https://bit.ly/2RXuXsD").text)
texto = requests.get("https://bit.ly/2Cu73N6").text

print ("\n", maisFrequente(lista))
print ("\n", maisFrequente(texto))

