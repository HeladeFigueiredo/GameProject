import sqlite3

# Cria uma conexão com o DB (criar se não existir)
conexao = sqlite3.connect('animal.db')

# Cria um curso para executar comandos SQL
cursor = conexao.cursor()

# Executar a primeira query - criar uma tabela
cursor.execute('''CREATE TABLE IF NOT EXISTS dog (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    age INTEGER,
                    weight REAL,
                    height REAL,
                    breed TEXT
                )''')

# Dados para preencher a tabela
pets_data = [
    ('Pablito', 3, 7, 0.5, 'Rajado'),
    ('Shitake', 2, 3, 0.4, 'Siames'),
    ('Gatarina', 1, 2, 0.3, 'Siames'),
    ('Mavies', 1, 2, 0.3, 'Preto e branco'),
    ('Virginia', 1, 1, 0.2, 'Siames'),
]

# Inserir dados na tabela
for pet in pets_data:
    cursor.execute('INSERT INTO dog'
                   '(name, age, weight, height, breed)'
                   'VALUES (?, ?, ?, ?, ?)',
                    pet)

# Commit das alteracoes realizadas no DB
conexao.commit()

# Fechando a conexão com o DB
# conexao.close()

print('Registros inseridos com sucesso.')

