#Questão 6
'''
def fatorial(n):
    resultado = 1
    for i in range(2, n+1):
        resultado *= i

numero = int(input("Digite um número inteiro: "))
print(f"Fatorial de {numero} é de {fatorial(numero)}")
'''
'''
#Questão 7

import re 

def validar_senha(senha):
    if (len(senha) >= 8 and 
        re.search(r"[A-Z]", senha) and
        re.search(r"[a-z]", senha) and
        re.search(r"[\d]", senha) and
        re.search(r"[!@#$%""*()[]{}]")):
        return True
    else:
        return False
'''

#Questão 5

def lista_de_compras():
    compras = []

    while True:
        print("Menu de lista de compras!")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Visualizar item")
        print("4 Sair")
        escolha = input("DIgite o número da opção desejada")

        if escolha == "1":
            item = input("Digite o item que deve ser adicionado")
            compras.append(item)
        elif escolha == "2":
            item = input("Digite o item que quer remover")
            if item in compras:
                compras.remove(item)
            else:
                print("Está tentando remover algo que nunca existiu!")
                for item in compras:
                    print(item)
        elif escolha == "3":
            print("Itens da lista de compras até agora: ")
            for item in compras:
                print(item)
        elif escolha == "4":
                print ("Saindo...")
                break
        else:
            print("Opção inválida. Tente novamente!")