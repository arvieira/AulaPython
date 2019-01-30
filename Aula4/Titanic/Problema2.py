import pandas as pd


titanic = pd.read_csv ("train.csv")
#print (titanic.head(), "\n")
#print (titanic.describe(), "\n")

#nameClass = titanic[["Name", "Pclass"]]
#print (nameClass.head(), "\n")

#print (titanic[["Survived", "Age"]].groupby("Age").mean(), "\n")
print (titanic[["Age", "Survived", "Sex"]].groupby("Sex").mean(), "\n")
print (titanic[["Age", "Survived", "Pclass"]].groupby("Pclass").mean(), "\n")
