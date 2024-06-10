# Realizamos a importação da biblioteca SQLite
import  sqlite3

# Abrimos a conexão e atribuimos ela a uma variável
conexao = sqlite3.connect('exempl.db')
# Utilizamos as opções presentes na conexão
cursor = conexao.curso()

#Realizamos a operação de inserir dados nos campos informados e colocamos placeholders
# em seguida nós informamos os dados 
cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', ('Alice', 30))
cursor.execute('INSERT INTO usuarios (nome, idade) VALUES (?, ?)', ('Marcos', 25))

#Comprometemos nossa alteração para o banco
conexao.commit()

#Fechamos a conexão do banco de dados
conexao.close()