import sys


# Definição da função main como um ponto de entrada
def main (argv):
	if (len(argv) > 1):
		print ("Olá", argv[1])
	else:
		print ("Faltou o parâmetro")

# Esse if indica que se eu executar esse programa a partir da linha de comando,
# ele irá executar a função main. Observe a passagem de parâmetros para o programa em si.
# Ele pega o parâmetro do sistema operacional e repassa para a main
if __name__ == "__main__":
	main (sys.argv)
