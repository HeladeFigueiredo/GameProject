import sqlite3

# Cria uma conexão com o DB (criar se não existir)
conexao = sqlite3.connect('animal.db')

# Cria um curso para executar comandos SQL
cursor = conexao.cursor()

#Selecionar todos os registros da tabela
cursor.execute('SELECT * FROM dog')

# Terá uma lista de linhas/registros
# Vamos considera que cada registro no DB é uma linha
rows = cursor.fetchall()

# Exibindos os registros
for row in rows:
    print(f'ID: {row[0]}, '
          f'NAME: {row[1]}, '
          f'AGE: {row[2]}, '
          f'WEIGHT: {row[3]}, '
          f'EIGHT: {row[4]}, '
          f'BREED: {row[5]}')

# Fechar conexão com DB
conexao.close()
