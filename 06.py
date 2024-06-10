#Primeiro exemplo de como integrar POO com Banco de Dados: SQLite
# Sistema genérico de Gerenciamento de Tabelas

import sqlite3

class BancoDeDadosSQLite:
    def __init__(self, nome_banco):
        self.conexao = sqlite3.connect(nome_banco)
        self.cursor = self.conexao.cursor()
        self.criar_tabela()

    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IN NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY,
                descricao TEXT,
                concluida BOOLEAN
            )
        ''')

    def adicionar_tarefa(self, descricao):
        self.cursor.execute('INSERT INTO tarefas(descricao, concluída) VALUES (?, ?)', (descricao, False))
        self.conexao.commit()

    def obter_tarefas(self):
        self.cursor.execute('SELECT * FROM tarefas')
        return self.cursor.fetchall()
    
    def marcar_tarefa_como_concluida(self, id_tarefa):
        self.cursor.execute('UPDATE tarefas SET concluida = ? WHERE id= ?', (True, id_tarefa))

class ListaDeTarefas:
    def __init__(self, db):
        self.db = db

    def adicionar_tarefa(self, descricao):
        self.db.adicionar_tarefa(descricao)

    def listar_tarefas(self):
        tarefas = self.db.obter_tarefas()
        for tarefa in tarefas:
           print(f'{tarefa[0]}. {tarefa[1]} - {Concluida if tarefa[2] else "Pendente"}')
           print