import json
from typing import TextIO

# Dados para serem salvos em um arquivo JSONM
# Já está no formato JSON - dicionário
# Sempre usando "aspas duplas"
data = {
    "name": "Pablito",
    "age": 3,
    "weight": 7,
    "height": 0.5,
    "breed": "Rajado"
}

# Criar um caminho/nome para o arquivo JSON
file_path = 'data.json'

# Salvar dados em formato JSON no arquivo
# Abra esse arquivo, eu quero fazer uma operação de escrita (write)
with open(file_path, 'w') as json_file:
    #Empurre estes dados para o arquivo e indente 4 espaços antes de cada propriedade
    json.dump(data, json_file, indent=4) #type: ignore

print('Dados salvos em JSON')

# Carregando dados de um arquivo JSON
# Abra o arquivo, quero fazer uma leitura (read)
with open(file_path, 'r') as json_file:
    #Carregue os dados do arquivo
    loaded_data = json.load(json_file)

print('Dados carregados do JSON:')
print(loaded_data)


