'''
class ContaBancaria:
    def __init__(self, nome_titular, número_conta, saldo_conta ):
        self.nome_titular = nome_titular
        self.número_conta = número_conta
        self.saldo_conta = saldo_conta
    
    def depositar(self):
        self.saldo_conta += ()
        if self.saldo_conta < 0:
            self.saldo_atual()
'''

'''
print("=-"*40)
print('DESAFIO 70 - SIMULADOR DE CAIXA ELETRÔNICO')
print("=-"*40)

def caixa1():

    print("-"*40)
    print('{:^30}'.format('BANCO TALIZU'))
    print("-" * 40)

    valor = int(input('Qual valor requerido? R$'))
    total = valor
    cedula = 50
    totalCedula = 0

    while True:

        if total >= cedula:
            total -= cedula
            totalCedula += 1

        else:

            if totalCedula > 0:
                print(f'Total de {totalCedula} cedulas de R${cedula} reais')

            if cedula == 50:
                cedula = 20

            elif cedula == 20:
                cedula = 10

            elif cedula == 10:
                cedula = 1

            totalCedula = 0

            if total == 0:
                break
    print("=" * 40)
    print("Volte sempre ao banco TaliZu!")

def caixa2():

    saque = int(input('Sacar R$: '))
    cedulas = [1, 10, 20, 50]
    c = 3
    while saque > 0:
        qtdced = saque // cedulas[c]
        saque -= qtdced * cedulas[c]
        c -= 1
        if qtdced > 0:
            print(f'{qtdced} cédulas de R$ {cedulas[c]}')


caixa1()
'''

'''
print('='*30)
print("{:^30}".format("CAIXA ELETRÔNICO TaliZu"))
print('='*30)

valor_do_saque = int(input('Digite o valor do saque: R$'))
total = valor_do_saque

print('\n\nAnalisando a transação....')
print('-[ Verificando disponiblidade de cédulas ]-')


cedula = 100
total_de_cedulas = 0

while True:

    if valor_do_saque >= cedula:
        valor_do_saque -= cedula
        total_de_cedulas += 1

    else:
        if total_de_cedulas > 0:
            print(f"Total de {total_de_cedulas} cédulas de R${cedula}...[OK]")

        if cedula == 100:
            cedula = 50

        elif cedula == 50:
            cedula = 20

        elif cedula == 20:
            cedula = 10

        elif cedula == 10:
            cedula = 5

        elif cedula == 5:
            cedula = 2


        total_de_cedulas = 0
        if valor_do_saque == 0:
            print('=' * 40)
            print(f"Transação realizada com sucesso!\nSaque no valor total de => : R${total}")
            exit()
        elif valor_do_saque == 1:
            print("\nOPERAÇÃO CANCELADA!"
                  "\nAs cédulas disponíveis neste caixa não permitem concluir esta transação.\n"
                  "Por favor, refaça sua operação com outro valor!")
'''


class ContaBancaria:
    def __init__(self, nome_titular, numero_conta, saldo_inicial=0):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor < 0:
                print("Valor de depósito inválido!")
        else:
            self.saldo += valor

    def sacar(self, valor):
        if valor > 0:
            if self.saldo > valor:
                self.saldo -= valor 
            else:
                print("Saldo insuficiente!")
        else:
            print("Valor de saque inválido!")

    def consultar_saldo(self):
        return self.saldo
    
    def transferir(self, valor, outra_conta):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                outra_conta.depositar(valor)
                print("Transferência feita com sucesso!")
            else:
                print("Você não possui saldo necessário para transferir! Deixe de ser liso!")
        else: 
            print("Valor da transferência deve ser maior do que 0, deixe de doideira")