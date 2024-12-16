import sqlite3  

# Conectar ao banco de dados
conexao = sqlite3.connect("oficina.db")

cursor = conexao.cursor()

# Inserir mecânicos
cursor.execute("INSERT INTO mecanico (nome) VALUES ('João')")
cursor.execute("INSERT INTO mecanico (nome) VALUES ('Maria')")

# Inserir serviços associados aos mecânicos
cursor.execute("INSERT INTO servicos (carro, id_mecanico) VALUES ('Ferrari A', 1)")  # João é o mecânico
cursor.execute("INSERT INTO servicos (carro, id_mecanico) VALUES ('Opel B', 2)")  # Maria é a mecânica

# Confirmar alterações
conexao.commit()

# Fechar conexão
conexao.close()
