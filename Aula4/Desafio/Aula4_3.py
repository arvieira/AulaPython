import pandas as pd
from matplotlib import pyplot as plt


# A classe pandas é uma classe científica que possui dentro dela um leitor de csv também
titanic_df = pd.read_csv ("./train.csv")	# Lendo o csv
print (titanic_df.head)				# Imprime o head da tabela
print (titanic_df.describe())			# Imprime dados estatísticos sobre a tabela


# A linha abaixo gera um gráfico histograma da tabela em memória
# Preciso colocar esse gráfico em um arquivo
# titanic_df["Age"].hist()
