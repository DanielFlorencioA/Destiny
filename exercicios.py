'''
def soma_impares(lista):
    impares = [num for num in lista if num % 2 != 0]
    return sum(impares)

numeros = int (input"Digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]

soma = soma_impares(numeros)
print("A soma dos números impras da lista é: ", soma)
'''

'''
def num_maior(lista):
    return max(lista)

numeros = input("Digite uma lista de números separados por espaço: ").split()
numeros = [int(num) for num in numeros]

maior = num_maior(numeros)
print("O maior número é: ", maior)
'''

alunos = int(input("Digite a quantidade de alunos:"))
media_alunos = []
media_turma = []

for i in range(1, alunos+1):
    print (f"Aluno {i}: ")
    notas_aluno = []

    for j in range(1, 4):
        nota = float(input(f"Digite a nota {j}: "))
        notas_aluno.append(nota)
        media_turma.append(nota)

    media_aluno = sum( notas_aluno) / len(notas_aluno)
    media_alunos.append(media_alunos)
    print("A media do aluno é: ", media_alunos)