import sqlite3  

# Conectar ao banco de dados
conexao = sqlite3.connect("oficina.db")

cursor = conexao.cursor()

# Criar a tabela mecanico
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mecanico(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL           
)
''')

# Criar a tabela servicos com chave estrangeira para mecanico
cursor.execute('''                                                      
    CREATE TABLE IF NOT EXISTS servicos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    carro TEXT NOT NULL,
    id_mecanico INTEGER,
    FOREIGN KEY (id_mecanico) REFERENCES mecanico (id)
)
''')

# Confirmar alterações
conexao.commit()

# Fechar conexão
conexao.close()
