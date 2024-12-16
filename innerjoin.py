import sqlite3  

# Conectar ao banco de dados
conexao = sqlite3.connect("oficina.db")

cursor = conexao.cursor()

# Consultar serviços e mecânicos
cursor.execute('''
    SELECT servicos.carro, mecanico.nome
    FROM servicos
    INNER JOIN mecanico ON servicos.id_mecanico = mecanico.id
''')

resultados = cursor.fetchall()

# Imprimir os resultados
print("CARRO | MECANICO RESPONSAVEL")
for carro, mecanico in resultados:
    print(f"{carro} | {mecanico}")

# Fechar conexão
conexao.close()
