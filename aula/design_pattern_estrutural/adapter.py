import json
import sqlite3

# Adapter para converter JSON em SQLite
class JsonSqliteAdapter:
    def __init__(self, db_name):
        self.db_name = db_name

    # Metodo para conectar ao banco de dados
    def connect(self):
        self.conexao = sqlite3.connect(self.db_name)
        self.conexao.execute("CREATE TABLE IF NOT EXISTS data "
                             "(id INTEGER PRIMARY KEY, json_data TEXT)")

    # Metodo para converter JSON em um JSON
    def save_data(self, data):
        # Transforma o dado de JSON para uma tupla que será inserida no banco de dados
        json_data = json.dumps(data)

        # Insere o json no banco de dados
        self.conexao.execute("INSERT INTO data (json_data) VALUES (?)", (json_data,))
        self.conexao.commit()

    # Metodo para carregar os dados do banco de dados
    def load_data(self):
        # Selecione do json_data a tabela data
        cursor = self.conexao.execute("SELECT json_data FROM data")
        json_data_list = [row[0] for row in cursor.fetchall()]
        data_list = [json.loads(json_data) for json_data in json_data_list]
        return data_list

    def close(self):
        self.conexao.close()


# Se esse arquivo é executável, se aqui está rodando a aplicação, execute e chame ele de main
if __name__ == "__main__":
    # Cria uma instância do Adapter que cria um banco de dados e cria conexão
    adapter = JsonSqliteAdapter("data.db")
    adapter.connect()

    # Lista de JSONs para salvar no banco de dados
    data_to_save = [{"name": "Pablito", "age": 3},
                    {"name": "Pablito", "age": 3}]

    # Transforma o dado de JSON para uma tupla que será inserida no banco de dados e salva no banco
    adapter.save_data(data_to_save)

    # Carrega os dados do banco de dados
    loaded_data = adapter.load_data()
    for item in loaded_data:
        print(item)

    # Fechar conexão com o banco de dados
    adapter.close()
