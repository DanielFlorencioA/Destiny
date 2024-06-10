# Realizamos a importação da biblioteca SQLite
import sqlite3

# Abrimos a conexão e atribuimos ela a uma variável
conexao = sqlite3.connect('Biblioteca')
# Utilizamos as opções presentes na conexão
cursor = conexao.cursor()

#Executamos uma tarefa: criamos uma tabela caso ela não exista, especificamos os campos
# que precisam ser preenchidos com nome do campo, tipo de campo e , caso precise,
# chave primária.
cursor.execute('''
    CREATE TABLE IN NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY,
        nome TEXT,
        idade INTEGER
        )
    ''')

#Fechamos a conexão com o banco
conexao.close()