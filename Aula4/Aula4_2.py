import csv


# Essa função será enviada para o email, copiar depois para o github
def read_csv (filepath):
	table = list ()					# cria uma lista vazia
	with open (filepath) as csv_file:
		reader = csv.DictReader(csv_file)	# reader é um conjunto de vários dicionários
		for row in reader:
			table.append (row)		# table será uma lista de dicionários
	return table


read_csv ("./products.csv")
