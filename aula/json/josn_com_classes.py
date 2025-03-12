import json

#CRIAÇÃO DA CLASSE DOG =====================================================================================================================
#=====================================================================================================================

class Dog:
    def __init__(self, name, age, weight, height, breed):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.breed = breed

    #Função para transformar o objeto Dog para um JSON
    def to_json(self):
        return {
            "name": self.name,
            "age": self.age,
            "weight": self.weight,
            "height": self.height,
            "breed": self.breed
        }

    #@classmethod é um decorador em Python
    # Transforma um metodo normal de uma classe em um metodo de classe
    #Significa que ao invés de operar em uma instância específica da classe (metodos com self), ele opera diretamente sobre a classe
    #Metodos normais usam self - opera na instancia 0 lida com os dados de um objeto criado a partir da classe
    #Metodos de classe - usam cls - opera na própria classe
    # Lida com dados/atributos que pertencem a classe e nao a uma instancia específica
    @classmethod
    # cls é abreviacao de classe
    # Representa a própria classe usado em métodos da classe @classmethod.
    # Permite criar instancias sem precisar referenciar diretamente.
    #cls refere-se a própria classe e self refere-se a uma instância da classe
    def from_json(cls, data):
        return cls(data["name"], data["age"], data["weight"], data["height"], data["breed"])

    # #Define a apresentação textual do objeto Dog
    def __repr__(self):
        return f"Dog(name={self.name}, age={self.age}, weight={self.weight}, height={self.height}, breed={self.breed})"


#=====================================================================================================================
#=====================================================================================================================

# Criando um objeto da classe Dog
dog = Dog('Tunico', 1, 5, 0.2, 'Chiwawa')

# Cria o nome para o arquivo JSON
file_path = "dog.json"

# Serialização - transformando o objeto/dados da classe para dicionário (formato JSON)
# Salvando o dicionario formato JSON no arquivo
with open(file_path, 'w') as json_file:
    #chama a classe dog e a função to_json
    json.dump(dog.to_json(), json_file, indent=4)  # type: ignore

print('Objeto da classe Dog salvo em formato JSON')
print('Dados salvos em JSON')

#Desserialização - transformar o dado do formato JSON para o formato da classe
#Carregar e ler dados de um arquivo JSON
with open(file_path, 'r') as json_file:
    loaded_json = json.load(json_file)

#Chama a classe dog e a função from_json e passa o dado em formato json para ser transformado
dog_classe = dog.from_json(loaded_json)

print('Dados carregados do JSON:')
print(dog_classe)





