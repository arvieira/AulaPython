import pandas as pd


passengerID = 10

titanic = pd.read_csv ("train.csv")
pclass = titanic[["Pclass", "Survived"]].groupby("Pclass").sum()
sex = titanic[["Sex", "Survived"]].groupby("Sex").sum()

print (pclass, "\n")
print (sex, "\n")

probsPclass = {
	1 : 1 / pclass.iloc[0]["Survived"],
	2 : 1 / pclass.iloc[1]["Survived"],
	3 : 1 / pclass.iloc[2]["Survived"]
}

probsSex = {
	"female" : 1 / sex.iloc[0]["Survived"],
	"male" : 1 / sex.iloc[1]["Survived"],
}

print (probsPclass)
print (probsSex, "\n")


choosen = titanic.iloc[passengerID - 1]
print ("Probabilidade de sobrevivência do passageiro", passengerID)
print (probsPclass[choosen.iloc[2]] * probsSex[choosen.iloc[4]])
