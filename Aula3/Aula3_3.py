from collections import Counter


def maisFrequente (lista):
	if type(lista) == str:
		lista = lista.split()

	contador = Counter(lista)
	return contador.most_common(10)
