import csv


def readCsv (filepath):
	table = list()  # Tabela é uma lista de linhas
	with open(filepath) as csv_file:
		reader = csv.DictReader(csv_file)
		for row in reader:
			table.append(row)
            
	return table


def varsInit ():
	return {
		"passengerNumber" : 0,
		"passengerSum" : 0,
		"deadNumber" : 0,
		"deadSum" : 0,
		"survivorNumber" : 0,
		"survivorSum" : 0
	}


def printResult (values):
	print ("ITEM 1:")
	print ("Total de passageiros", values["passengerNumber"])
	print ("Soma das idades", values["passengerSum"])
	print ("Média das idades", values["passengerSum"]/values["passengerNumber"])

	print ("\n\nITEM 2:")
	print ("Total de mortos", values["deadNumber"])
	print ("Soma das idades dos mortos", values["deadSum"])
	print ("Idade média dos mortos", values["deadSum"]/values["deadNumber"])
	print ("")
	print ("Total de sobreviventes", values["survivorNumber"])
	print ("Soma das idades dos sobrevivents", values["survivorSum"])
	print ("Idade média dos sobreviventes", values["survivorSum"]/values["survivorNumber"])

	print ("\n\nITEM 3:")
	print ("Percentual de passageiros sobreviventes", (100 * values["survivorNumber"]) / values["passengerNumber"])


def doLogic (titanic):
	values = varsInit()
	
	for passenger in titanic:
		if (passenger["Age"] != ""):
			values["passengerSum"] += float (passenger["Age"])

			if (passenger["Survived"] == "0"):
				values["deadNumber"] += 1
				values["deadSum"] += float (passenger["Age"])
			else:
				values["survivorNumber"] += 1
				values["survivorSum"] += float (passenger["Age"])

		values["passengerNumber"] +=1

	return values



titanic = readCsv ("./train.csv")
values = doLogic (titanic)
printResult(values)
