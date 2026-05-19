# A palavra "class" é usada para criar uma classe.
# Uma classe funciona como um molde para criar objetos.
class Carro:
# "def" definir uma função ou método
# "__init__" é o método construtor da classe
# Ele é executado automaticamente quando um
# objeto é criado

# "self" representa o próprio objeto
# É através do self que acessamos atributos e
# métodos do objeto

# Método Construtor
    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        # Método

    def acelerar(self, aumento):
        #self.velocidade = self.velocidade + aumento
        self.velocidade += aumento

        print(f"O carro acelerou para{self.velocidade} km/h")

#Criando um objeto da Classe Carro

# "carro1" é uma variável que recebe um objeto
carro1 = Carro("Chevrolet", "S10", 2013, 0)

#Exibe informações do carro
print(f"Marca: {carro1.marca}")
print(f"Modelo : {carro1.modelo}")
print(f"Ano : {carro1.ano}")

carro1.acelerar(50)

carro2 = Carro("Ford", "Mobiauto", 2015, 0)

#Exibe informações do carro
print(f"Marca: {carro2.marca}")
print(f"Modelo : {carro2.modelo}")
print(f"Ano : {carro2.ano}")

carro3 = Carro("Fiat", "Pulse Hybrid", 2024, 0)

#Exibe informações do carroh
print(f"Marca: {carro3.marca}")
print(f"Modelo : {carro3.modelo}")
print(f"Ano : {carro3.ano}")

class Moto:

    def __init__(self, marca, modelo, ano, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade

moto1 = Moto("Suzuki", "Espirit", 2013, 0)


print(f"Marca: {moto1.marca}")
print(f"Modelo : {moto1.modelo}")
print(f"Ano : {moto1.ano}")
print(f"Velocidade : {moto1.velocidade} km/h")

















          
        
        