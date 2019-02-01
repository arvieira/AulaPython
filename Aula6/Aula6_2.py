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

# A seguir temos uma classe quadrado que extende (herda) do retângulo
# mas ele redefine o construtor, de modo a colocar os lados iguais
class Quadrado (Retangulo):
	contador = 0

	def __init__ (self, lado):
		self.largura = lado
		self.altura = lado
		Quadrado.contador += 1




ret = Retangulo (3, 4)
print ("Retangulo")
print (ret.area())
print (ret.diagonal(), "\n")


ret = Retangulo (4, 5)
print ("Retangulo")
print (ret.area())
print (ret.diagonal(), "\n")

quad = Quadrado (4)
print ("Quadrado")
print (quad.area())
print (quad.diagonal(), "\n")

quad = Quadrado (2)
print ("Quadrado")
print (quad.area())
print (quad.diagonal(), "\n")

quad = Quadrado (3)
print ("Quadrado")
print (quad.area())
print (quad.diagonal(), "\n")

ret = Retangulo (4, 5)
print ("Retangulo")
print (ret.area())
print (ret.diagonal(), "\n")

quad = Quadrado (3)
print ("Quadrado")
print (quad.area())
print (quad.diagonal(), "\n")

print ("Total Retangulo", Retangulo.contador)
print ("Total Quadrado", Quadrado.contador)

# Observações de escopo
# Dentro de um método de uma classe, eu acesso as variáveis de instância com a palavra self.
# Se eu uso uma variável com self, sem ela estar no construtor, eu crio uma variável de instância desse objeto e não da classe.
# Para variáveis locais dos métodos, eu uso sem o self, assim elas só existirão dentro daquele método.
