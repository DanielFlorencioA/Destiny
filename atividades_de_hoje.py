import sqlite3

class banco:
    def __init__(self, nome_titular='banco'):
        self.nome_titular = nome_titular
        self.conn = sqlite3.connect(self.nome_titular)
        self.cursor = self.conn.cursor()
        self.editar_banco()

    def ediar_banco(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contas (
                numero_conta TEXT PRIMARY KEY,
                nome_titular TEXT,
                saldo
            )
        ''')
        self.conn.commit()

    def criar_conta(self, numero_conta, nome_titular, saldo):
        self.cursor.execute('''
            INSERT OR REPLACE INTO conta (numero_conta, nome_titular, saldo) VALUES (?, ?, ?)
        ''', (numero_conta, nome_titular, saldo))
        self.conn.commit()

    def editar_saldo(self, numero_conta, saldo):
        self.cursor.execute('''
            UPDATE contas SET saldo = ? WHERE numero_conta = ?
        ''', (saldo, numero_conta))
        self.conn.commit()

    def fechar_conexao(self):
        self.conn.close()

class conta:
    def __init__(self, nome_titular, numero_conta, saldo, banco=None):
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo
        self.banco = banco
        self.salvar_conta()

    def salvar_conta(self):
        self.banco.conta(self.numero_conta, self.nome_titular, self.saldo)

    def atualizar_saldo(self):
        self.banco.editar(self.numero_conta, self.saldo)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.atualizar_saldo()
            print(f"deposito no valor de R${valor} realizado com sucesso.")
        else:
            print("O valor do depósito está incorreto.")

    def sacar(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.atualizar_saldo()
                print(f"saque no valor R${valor} realizado com sucesso.")
            else:
                print("saldo insuficiente para o valor disponivel.")
        else:
            print("digite um valor maior que zero..")

    def consulta_de_saldo(self):
        return self.saldo

    def transferir(self, saldo, conta_2):
        if saldo > 0:
            if self.saldo >= saldo:
                self.saldo -= saldo
                self.atualizar_saldo()
                conta_2.depositar(saldo)
                print(f"valor da transferência de R${saldo} para a conta {conta_2.numero_conta} realizada com sucesso.")
            else:
                print("Você não possui saldo suficiente para realizar a transição.")
        else:
            print("digite um valor maior que zero para realizar transferência.")