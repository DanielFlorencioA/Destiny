'''
def fatorial (a):
    if a == 0:
        return 1
    else:
        fat = 1
        for i in range (1, a+1):
            fat *= i
            return fat
        
x = int (input("Digite um número inteiro: "))
print("O fatorial de", x, " é: ", fatorial (x))
'''

'''
Nome = input ("Digite seu nome: ")
Tem_carro = input("Você possui algum carro? (Sim/Não): ")
Altura = float(input("Digite sua altura: "))
Idade = int(input("Digite sua idade: "))

Tem_carro = Tem_carro.lower() == "sim"

print("Informações Digitadas: ")
print("Nome: ", Nome)
print("Idade: ", Idade)
print("Altura: ", Altura)
print("Tem carro? ", "Sim" if Tem_carro else "Não")
'''


'''
def contagem_regressiva():
    numero = int(input("Digite um número inteiro positivo: "))

    if numero <=0:
        print("Por favor, digite um número inteiro positivo.")
        contagem_regressiva()

    else: 
        while numero >= 0:
            print(numero)
            numero -= 1

contagem_regressiva()

'''


def soma (a, b):
    return a + b
def subtracao (a, b):
    return a - b
def multiplicacao (a, b):
    return a * b
def divisao (a, b):           
    if b != 0:
        return a / b
    else:
        return "Divisão Inválida"
    
def calculadora():
    print("Bem-vindo a calculadora em Python")
    print("Selecione a operação desejada!")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")

escolha = input("Digite sua escolha 1/2/3/4: ")
if escolha in ('1', '2', '3', '4'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    
    if escolha == '1':
        print("Resultado", soma(num1, num2))