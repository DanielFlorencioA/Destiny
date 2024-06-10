'''
#Q06

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = 5
resultado = fatorial(numero)
print("O fatorial de", numero, "é", resultado)
'''

'''
#Q07

import re

print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
senha = input("Digite sua senha: ")

while not (re.search(r'.{8,}', senha) and   
           re.search(r'[A-Z]', senha) and 
           re.search(r'\d', senha) and   
           re.search(r"!@#$%¨&*", senha)):  
    senha = input("Use como base os critérios informado : ")

print("Senha cadastrada com sucesso!")
'''


#Q01

classificar_idades = int(input('Digite sua idade: '))
if classificar_idades >= 0 and classificar_idades < 13:
    print('Criança')
if classificar_idades >= 14 and classificar_idades < 18:
    print('Adolescente')
elif classificar_idades >= 18 and classificar_idades < 60:
    print('Adulto')
elif classificar_idades >= 60 and classificar_idades <= 100:
    print('Idoso')
else:
    print('Avatar')


    
'''
#Q02

escolha=True
while escolha:
    print("\n")
    print("Unidades de Medida de Comprimento")
    print("""
    1.Milímetro (mm)
    2.Centímetro (cm)
    3.Decímetro (dm)  
    4.Metro(m)
    5.Decâmetro (dam)
    6.Hectômetro (hm) 
    7.Quilômetro (km) 
    8.Exit/Quit/Saída
    """)
    

    escolha= input("Escolha uma opção:  ")
    if escolha=="1":
        mm = float(input("Digite o número em mm: "))
        km = mm / 1000000
        hm = mm / 100000
        dam = mm / 10000
        m = mm / 1000
        dm = mm / 100
        cm = mm / 10
        print(f'{mm} milímetros são {km} quilômetros')
        print(f'{mm} milímetros são {hm} hectômetros')
        print(f'{mm} milímetros são {dam} decâmetros')
        print(f'{mm} milímetros são {m} metros')
        print(f'{mm} milímetros são {dm} decímetros')
        print(f'{mm} milímetros são {cm} centímetros')
    elif escolha=="2":
        cm = float(input("Digite o número em dm: "))
        km = cm / 100000
        hm = cm / 10000
        dam = cm / 1000
        m = cm / 100
        dm = cm/10
        mm = cm * 10
        print(f'{cm} centímetros são {km} quilômetros')
        print(f'{cm} centímetros são {hm} hectômetros')
        print(f'{cm} centímetros são {dam} decâmetros')
        print(f'{cm} centímetros são {m} metros')
        print(f'{cm} centímetros são {dm} decímetros')
        print(f'{cm} centímetros são {mm} milímetros')

    elif escolha=="3":
        dm = float(input("Digite o número em dm: "))
        km = dm / 10000
        hm = dm / 1000
        dam = dm / 100
        m = dm /10
        cm = dm * 10
        mm = dm * 100
        print(f'{dm} decímetros são {km} quilômetros')
        print(f'{dm} decímetros são {hm} hectômetros')
        print(f'{dm} decímetros são {dam} decâmetros')
        print(f'{dm} decímetros são {m} metros')
        print(f'{dm} decímetros são {cm} centímetros')
        print(f'{dm} decímetros são {mm} milímetros')
    elif escolha == "4":
        m = float(input("Digite o número em m: "))
        km = m / 1000
        hm = m / 100
        dam = m / 10
        dm = m * 10
        cm = m * 100
        mm = m * 1000
        print(f'{m} metros são {km} quilômetros')
        print(f'{m} metros são {hm} hectômetros')
        print(f'{m} metros são {dam} decâmetros')
        print(f'{m} metros são {dm} decímetros')
        print(f'{m} metros são {cm} centímetros')
        print(f'{m} metros são {mm} milímetros')
    elif escolha == "5":
        dam = float(input("Digite o número em dam: "))
        km = dam / 100
        hm = dam / 10
        m = dam * 10
        dm = dam * 100
        cm = dam * 1000
        mm = dam * 10000

        print(f'{dam} decâmetros são {km} quilômetros')
        print(f'{dam} decâmetros são {hm} hectômetros')
        print(f'{dam} decâmetros são {m} metros')
        print(f'{dam} decâmetros são {dm} decímetros')
        print(f'{dam} decâmetros são {cm} centímetros')
        print(f'{dam} decâmetros são {mm} milímetros')
    elif escolha == "6":
        hm = float(input("Digite o número em hm: "))
        km = hm/10
        dam = hm * 10
        m = hm * 100
        dm = hm * 1000
        cm = hm * 10000
        mm = hm * 100000
        print(f'{hm} hectômetros são {km} quilômetros')
        print(f'{hm} hectômetros são {dam} decâmetro')
        print(f'{hm} hectômetros são {m} metros')
        print(f'{hm} hectômetros são {dm} decímetros')
        print(f'{hm} hectômetros são {cm} centímetros')
        print(f'{hm} hectômetros são {mm} milímetros')
    elif escolha == "7":
       km=float(input("Digite o número em km: "))
       hm = km*10
       dam = km*100
       m = km*1000
       dm = km*10000
       cm = km*100000
       mm = km*1000000
       print(f'{km} quilômetros são {hm} hectômetros')
       print(f'{km} quilômetros são {dam} decâmetro')
       print(f'{km} quilômetros são {m} metros')
       print(f'{km} quilômetros são {dm} decímetros')
       print(f'{km} quilômetros são {cm} centímetros')
       print(f'{km} quilômetros são {mm} milímetros')

    elif escolha=="8":
      print("\n Adeus")
      escolha = None
    else:
       print("\n Escolha não válida.\n Tente outra vez.")

'''

'''
#Q03

gerenciar_contatos = [[]]

while True:
    print("1-Cadastrar pessoa: ")
    print("2-Lista Cadastros: ")
    print("3-Procurar Pessoa Especifica: ")
    print("4-Sair: ")

    op = int(input())
    if op == 1:
        nova = []
        id = input("Id da pessoa: ")
        nome = input("Digite o nome da pessoa: ")
        idade = input("Idade da pessoa: ")
        nova.append(id)
        nova.append(nome)
        nova.append(idade)
        gerenciar_contatos.append(nova)

    elif op == 2:
        for mostrar in gerenciar_contatos:
            for mostrar2 in mostrar:
                print(mostrar2)

    elif op == 3:
        print("pensando")
    '''