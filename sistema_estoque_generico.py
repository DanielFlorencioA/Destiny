import sqlite3

class ItemEstoque:
    def __init__(self, nome, marca, modelo, preco, quantidade):
        self.nome = nome 
        self.marca = marca
        self.modelo = modelo
        self.preco = preco
        self.quantidade = quantidade

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}, Marca: {self.marca}, Modelo: {self.modelo}, Preço: {self.preco}. Quantidade: {self.quantidade}")

class Estoque:
    def __init__(self, db_name="estoque.db"):
        self.conn = sqlite3.connect(db_name)
        self.criar_tabela()

    def criar_tabela(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS itens(
                    id INTEGER PRIMARY KEY,
                    nome TEXT NOT NULL,
                    marca TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    preco REAL NOT NULL,
                    quantidade INTEGER NOT NULL   
            )
        """)
            
    def adicionar_item(self, item):
        with self.conn:
            self.conn.execute("""
                 INSERT INTO itens (nome, marca, modelo, preco, quantidade)             
                 VALUES (?, ?, ?, ?, ?)""",(item.nome, item.marca, item.modelo, item.preco, item.quantidade))
        print("Item adicionado ao estoque com sucesso!")

    def remover_item(self, nome_item):
        with self.conn:
            cursor = self.conn.execute("DELETE FROM itens WHERE nome = ?", (nome_item,))
        if cursor.rowcount > 0:
            print("Item removido com sucesso!")
        else:
            print("Item não encontrado no estoque.")
        
    def editar_itens(self, nome_item, marca):
        with self.conn:
            cursor = self.conn.execute("UPDATE itens SET nome = ? WHERE marca = ?", (nome_item, marca))
        if cursor.rowcount > 0:
            print("Item atualizado com sucesso!")
        else:
            print("Item não encontrado no estoque.")

    def visualizar_itens(self):
        with self.conn:
            self.conn.execute("SELECT * FROM itens").fetchall()