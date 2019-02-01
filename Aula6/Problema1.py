# Como um banco de dados, temos uma tabela de alunos, uma de disciplina e uma de relacionamento
# que faz o papel das inscrições em disciplinas
alunos = [{"Matricula" : 1, "Nome" : "André"}, 
	{"Matricula" : 2, "Nome" : "Bernardo"}]

disciplinas = [{"ID": 1, "Nome": "Python 1", "Professor" : "Charles", "Dependencias" : []}, 
	{"ID": 2, "Nome": "Python 2", "Professor" : "Diego", "Dependencias" : [0]}, 
	{"ID": 3, "Nome": "Python 3", "Professor" : "Evandro", "Dependencias" : [0, 1]},
	{"ID": 4, "Nome": "Estatística", "Professor" : "Fred", "Dependencias" : []}]

inscricoes = [{"IdDisciplina" : 1, "Inscritos" : [1]}, 
	{"IdDisciplina" : 2, "Inscritos" : [2]}, 
	{"IdDisciplina" : 4, "Inscritos" : [1, 2]}]









# Uma query pelos alunos que estão escritos em Estatística
idDisciplina = 0
for disciplina in disciplinas:
	if (disciplina["Nome"] == "Estatística"):
		idDisciplina = disciplina["ID"]
print (idDisciplina)

inscritos = []
for inscricao in inscricoes:
	if (inscricao["IdDisciplina"] == idDisciplina):
		inscritos = inscricao["Inscritos"]
print (inscritos)

listaDeNomes = []
for inscrito in inscritos:
	for aluno in alunos:
		if (inscrito == aluno["Matricula"]):
			listaDeNomes.append(aluno["Nome"])
print (listaDeNomes)










# Solução do professor
# Passo 1
id_estatistica  = [disciplina for disciplina in disciplinas
	if (disciplina["Nome"] == "Estatística")][0]["ID"]	# Como o if me retorna uma lista de 1 elemento
								# Eu pego o elemento 0 dele, o qual é um dicionário
								# Desse dicionário eu pego o id da disciplina
print (id_estatistica)


# Passo 2
inscritos_estatistica = [inscricao for inscricao in inscricoes 
			if (inscricao["IdDisciplina"] == id_estatistica)][0]["Inscritos"]
print (inscritos_estatistica)


# Passo 3
nomes_alunos = [aluno["Nome"] for aluno in alunos
		if (aluno["Matricula"] in inscritos_estatistica)]
print (nomes_alunos)


# Observação:
# Eu tenho como um select em um banco de dados, haja à vista que tenhos tabelas como em um banco de dados
# [aluno["Nome"] for aluno in alunos -> Aqui eu tenho aluno["Nome"] como as colunas selecionadas na query
#					e tenho o in alunos como a tabela da qual vou selecionar
# 	if (aluno["Matricula"] in inscritos_estatistica) -> aqui eu tenho o where da query
#
# Traduzindo o passo 2:
# select * from inscricao
#	where IdDisciplina = "id_estatistica"a
#
# Pegando a linha 0 da resposta e a coluna Inscritos
# Não poderia colocar 
# select Inscritos from inscricao
# Pq eu preciso do IdDisciplina para fazer o where
