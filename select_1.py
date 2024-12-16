import sqlite3

conexao = sqlite3.connect("oficina.db")

cursor = conexao.cursor()

cursor.execute('SELECT * FROM servicos')
resultados = cursor.fetchall()
print("----------------------------NOMES DAS MARCAS----------------------------")
for marca in resultados:
    print("MARCA:")
    print(marca)


cursor.execute('SELECT * FROM mecanico')
resultados = cursor.fetchall()
print("-----------------------NOMES DOS FUNCIONARIOS----------------------------")
for nome in resultados:
    print("NOME:")
    print(nome)
    
    


conexao.close