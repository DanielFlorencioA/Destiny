import sqlite3

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

cursor.execute('SELECT * FROM usuarios')
dados = cursor.fetchall()
for linha in dados:
    print(linha)

conexao.close()