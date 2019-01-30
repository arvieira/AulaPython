import csv


# A primeira coisa que vem depois do arquivo é um recurso.
# Após o recurso, coloco um "as" e como o recurso vai ser tratado.
# O with faz o recurso ficar disponível para o bloco do with, ou seja, 
# o arquivo aqui só está disponível durante o bloco do with, depois ele fecha
# sozinho, não preciso me preocupar
with open ('./products.csv') as arq_csv:
	reader = csv.DictReader (arq_csv)	# Lê um arquivo csv e coloca em um dicionário
	for linha in reader:			# Lê o reader linha por linha. Cada linha é um dicionário
						# Acesso os valores no dicionário usando o cabeçalho do csv como chaves
		print (linha['ProductName'], " | ", linha['QuantityPerUnit'], " | ", linha ['UnitPrice'])

# Em arquivos csv, a primeira linha é o cabeçalho da tabela, no caso o nome de cada coluna
# As demais linhas, serão os registros da tabela.
# Os atributos são separados por ","
