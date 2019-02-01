import math


# O construtor da classe se define com o __init__(self)
# Nele é que se coloca as variáveis de instância da classe
# Caso eu tenho uma classe que não tenha construtor, não poderei declarar e inicializar as variáveis de instância
# como nesse exemplo. Nesse caso, eu posso criar variáveis dentro de métodos e colocar ela como de instância
# daquele objeto e não da classe como um todo.

class Aluno:
	def __init__ (self):
		self.nome = ""
		self.curso = ""
		self.matricula = 0

aluno = Aluno()
print (aluno.matricula)




# Herança
class Retangulo:
	cor = "Branco"			# Funciona como o static do Java 
	contador = 0

	def __init__ (self, largura, altura):
		self.largura = largura
		self.altura = altura
		Retangulo.contador += 1		# Acesso a variável estática

	def area (self):
		return self.largura * self.altura

	def diagonal (self):
		return math.sqrt(self.largura ** 2 + self.altura ** 2)

# Métodos estáticos não aqueles que apenas operam em variáveis estáticas da classe
# Não possui uma palavra reservada para isso, mas eu devo chamar pelo nome da classe

# A seguir temos uma classe quadrado que extende (herda) do retângulo
# mas ele redefine o construtor, de modo a colocar os lados iguais
class Quadrado (Retangulo):
	contador = 0			# Preciso redeclarar o contador, pq senão ele compartilha as estáticas da classe pai

	def __init__ (self, lado):	# O mesmo compartilhamento ocorre com o construtor que herdará a inicialização das
		self.largura = lado	# variáveis do retangulo. Desse modo, eu preciso redeclarar as variáveis estáticas
		self.altura = lado	# e os construtores de classe para não ter esse compartilhamento.
		Quadrado.contador += 1




ret1 = Retangulo (3, 4)
print ("Retangulo")
print (ret1.area())
print (ret1.diagonal(), "\n")

ret2 = Retangulo (4, 5)
print ("Retangulo")
print (ret2.diagonal())
ret2.altura = 9
print (ret2.diagonal(), "\n")

quad1 = Quadrado (4)
print ("Quadrado")
print (quad1.area())
print (quad1.diagonal(), "\n")

quad2 = Quadrado (2)
print ("Quadrado")
print (quad2.area())
print (quad2.diagonal(), "\n")

quad3 = Quadrado (3)
print ("Quadrado")
print (quad3.area())
print (quad3.diagonal(), "\n")

ret3 = Retangulo (4, 5)
print ("Retangulo")
print (ret3.area())
print (ret3.diagonal(), "\n")

quad4 = Quadrado (3)
print ("Quadrado")
print (quad4.area())
print (quad4.diagonal(), "\n")

print ("Total Retangulo", Retangulo.contador)
print ("Total Quadrado", Quadrado.contador)

# Observações de escopo
# Dentro de um método de uma classe, eu acesso as variáveis de instância com a palavra self.
# Se eu uso uma variável com self, sem ela estar no construtor, eu crio uma variável de instância desse objeto e não da classe.
# Para variáveis locais dos métodos, eu uso sem o self, assim elas só existirão dentro daquele método.
