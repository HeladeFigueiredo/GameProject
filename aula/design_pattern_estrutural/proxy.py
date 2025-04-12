#Classe Dog
import sqlite3


class Dog:
    def __init__(self, name, age, weight, height, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.breed = breed


# Proxy para interagir com banco de dados SQLite3
class DbProxy:
    def __init__(self, database_path='catioooros.db'):
        self.database_path = database_path

    # Função responsável por inserir um cão no banco de dados
    def insert_dog(self, new_dog):
        conexao = sqlite3.connect(self.database_path) #Abre conexão
        cursor = conexao.cursor() #Cria cursor

        # Se não tiver uma tabela, cria ela
        cursor.execute('''CREATE TABLE IF NOT EXISTS dogs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            weight REAL,
            height REAL,
            breed TEXT
        )''')

        cursor.execute("INSERT INTO dogs (name, age, weight, height, breed)"
                        "VALUES (?, ?, ?, ?, ?)",
                (new_dog.name,
                            new_dog.age,
                            new_dog.weight,
                            new_dog.height,
                            new_dog.breed))

        conexao.commit()
        conexao.close()
        print('Dog inserido com sucesso!')


    # Função responsável por retornar todos os cães do banco de dados
    def get_all_dogs(self):
        conexao = sqlite3.connect(self.database_path) #Abre conexão
        cursor = conexao.cursor() #Cria cursor

        cursor.execute('SELECT * FROM dogs') #Selecionar todos os registros da tabela
        rows = cursor.fetchall()   # Terá uma lista de linhas/registros

        dogs = []
        for row in rows:
            dog = Dog(row[1], row[2], row[3], row[4], row[5]) # Cria um objeto Dog
            dogs.append(dog)

        conexao.close()
        return dogs


# Cria um objeto do tipo Dog
dog = Dog('Pablito', 3, 7, 0.5, 'Rajado')

# Cria instânca do proxy
# Acesso mais discreto e limpo do DB
# Não precisa saber como funciona o DB - abstração
# Conexão com banco de dados fica caixinha preta - simplificado
# Mais fácil de usar
# Não precisa encher de conexao, cursor, etc

proxy = DbProxy()

# Insere o cão no banco de dados
proxy.insert_dog(dog)

# Recupera todos os cães do banco de dados
all_dogs = proxy.get_all_dogs()

for dog in all_dogs:
    print(f'Name: {dog.name}, '
          f'Age: {dog.age}, '
          f'Weight: {dog.weight}, '
          f'Height: {dog.height}, '
          f'Breed: {dog.breed}')