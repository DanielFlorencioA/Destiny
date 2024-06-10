import random

def jogo_adivinhaçao():
    numero_aleatorio = random.randint(1,100)
    tentativas = 0


    while True:
        palpite = int(input("Tente adivinhar o número entre 1 e 100!"))
        tentativa += 1
    
        if palpite < numero_aleatorio:
            print("Número Baixo. Tente novamente")
        elif palpite > numero_aleatorio:
            print("Número Alto. Tente novamente")
        else:
            print(f"Parabéns!! Você acertou o número {numero_aleatorio}")
            break

jogo_adivinhaçao()
