import csv


# Essa função será enviada para o email, copiar depois para o github
def read_csv (filepath):
	table = list ()		# cria uma lista vazia
	with open (filepath) as csv_file
		reader = csv.dictReader()
