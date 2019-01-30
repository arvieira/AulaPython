# Trabalhando com arquivos em Python.
# Para abrir o arquivo usa a função open("nome/do/aruqivo", <parametro>)
# <parametro>:
# 	"w" para escrita texto
#	vazio para leitura de textos
# 	"rb" e wb para leitura e escrita de binários
#
# Encoding:
# Quando eu estou trabalhando com arquivos em modo binário, se eu quero escrever
# texto, eu preciso passar ele pelo encoding primeiro.
# arquivo.write("Olá".encode("utf8"))
#
# Unicode:
# utf-8, utf-16 e utf-32 são 3 tipos diferentes de codificações do unicode e muda
# o número de bits utilizados para codificar um caracter.


arquivo = open ("./saida.txt", "w")
arquivo.write ("Teste")
arquivo.close ()

arquivo = open ("./saida.txt")
print (arquivo.readline())
