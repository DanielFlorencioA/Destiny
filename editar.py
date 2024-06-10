import sqlite3

conexao = sqlite3.connect('exemplo.db')
cursor = conexao.cursor()

cursor.execute('UPDATE usuarios SET idade = ? WHERE nome ?',(40, 'Alice'))
conexao.close

conexao.close()