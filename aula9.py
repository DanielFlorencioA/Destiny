'''
class Pessoa:
    Nome = input("Digite seu nome: ")
    Idade = int(input("Digite sua idade: "))
    Peso = float(input("Digite seu peso: "))
    Altura = float(input("Digite sua altura: "))
    
    print("Seu nome é:", Nome, "Sua idade é:", Idade, "Seu peso é:", Peso, "Sua idade é:", Altura)

Pessoa()

Name = input("Digite seu nome: ")

def __init__(self,nome,idade,peso, altura):
    self.nome = nome
    self.idade = idade
    self.peso = peso
    self.altura = altura

def envelhecer(self, anos):
    self.idade += 1
    return self.idade
def engordar(self, kilos):
    self.peso += kilos
    return self.peso
def emagrecer(self,kilos_perdidos):
    self.peso -= kilos_perdidos
    return self.peso

def crescer(self,anos):
    if self.idade<21:
        self.altura += (0.5)*anos
    return self.altura

Apelido = Pessoa()

print(Apelido.__dict__)
print(f'seu nome é {Apelido.nome}, você tem {Apelido.idade} anos, pesa {Apelido.peso} kgs e tem uma altura de {Apelido.altura}')
'''

#Correção

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade += 1
        if self.idade < 21:
            self. crescer(0.5)

    def engordar(self, peso):
        self.peso += peso
    
    def emagrecer(self, peso):
        self.peso -= peso

    def crescer(self, altura):
        self.altura += altura

    def __str__(self):     
        return f"Nome: {self.nome}, Idade: {self.idade}, Peso : {self.peso}, Altura: {self.altura}"
    
pessoa1 = Pessoa("João", 20, 150, 165)
print("Dados Iniciais: ")
print(pessoa1)