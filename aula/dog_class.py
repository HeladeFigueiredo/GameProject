from aula.animal_class import Animal


class Dog:
    familia = 'Canidae' # atributo da classe

    # é boa prática sempre tipificar os atributos, mas também podemos criar sem tipificar
    def __init__(self, nome: str, idade, brinquedoFavorito: str, corPelagem: str): #nome é um atributo com passagem de parâmetro no construtor da classe
        self.nome = nome  ## todos os atributos devem ser instanciados no inicializador da classe
        self.idade = idade
        self.raca = 'cachorro' #isso é um atributo com um valor fixo que será inserido ao instanciar a classe
        self._brinquedoFavorito = brinquedoFavorito # Um _ significa que o atributo é privado. Usado quando não queremos instanciar esse atributo fora da classe. Vai rodar mas a interface vai apontar que tem algo não conforme
        self.__corPelagem = corPelagem # Dois __ significa que o atributo é protegido e não deve ser acessado. Não vai rodar e vai dar erro
        # Para conseguir acessar atributos protegidos precisa-se de getters e setters

    def get_brinquedoFavorito(self) -> str:
            return self._brinquedoFavorito

    def get_corPelagem(self) -> str:
            return self.__corPelagem

    def set_corPelagem(self, corPelagem: str):
            self.__corPelagem = corPelagem

catioroPadrao = Dog('Rex', 5, 'Bola', corPelagem='Loiro') # O código tá rodando, mas o correto é passar essa informação com o get e set
catioroCaramelo = Dog('Caramelo', 10, 'Motoqueiro', corPelagem='Caramelo né') # O código tá roadando, mas o correto é passar essa informação com o get e set

catioroPadrao.set_corPelagem('Ruivo Patricinha')

print(catioroPadrao)
print(f'O {catioroPadrao.nome} tem {catioroPadrao.idade} anos e é da raça {catioroPadrao.raca}. A família dele é {Dog.familia}.')
print(f'O {catioroCaramelo.nome} tem {catioroCaramelo.idade} e é da raça {catioroPadrao.raca}. A família dele é {catioroCaramelo.familia}.')
# O atributo família é chamado da classe e não do objeto, porque este atributo pertence a classe.
# O atributo família também pode ser chamado no objeto, porque esse objeto é do tipo classe Dog.

print(f'f O {catioroPadrao.nome} tem o brinquedo favorito {catioroPadrao._brinquedoFavorito}') # Esse é exibido no terminal mas fica com um sinal de erro no código
# print(f'O catioro {catioroCaramelo.nome} tem a cor {catioroCaramelo.corPelagem}') # Esse dá erro no terminal

#Para printar atributos protegidos e privados usa-se get e set
print(f'O Rex tem o brinquedo favorito {catioroPadrao.get_brinquedoFavorito()}')

print(f'O Rex tem a cor {catioroPadrao.get_corPelagem()}')
print(f'O Caramelo tem a cor {catioroCaramelo.get_corPelagem()}')

# Para saber qual é a classe do objeto
print(f'O catioroPadrao é um objeto da classe {catioroPadrao.__class__.__name__}.')

