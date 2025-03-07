from aula.animal_class import Animal


class Cachorro(Animal):
    def __init__(self, name: str, age: int, height: int, position: tuple):
        super().__init__(name, age, height, position)
        # Preciso chamar o construtor da classe pai/super. Leia como chame a classe pai, chame o construtor da classe pai e passe os seguintes atributos. Isso inicializa a classe pai.
        # Também pode ser escrito de forma explícita pra facilitar a visualização
        # Ficaria assim:
        # Animal.__init__(name, age, height, position)

    # Aqui estou sobrescrevendo o metodo move_z da classe pai
    def move_z(self):
        self.position[2] += 2


# Nessa forma de instanciar precisa ser colocado na ordem
catioroAndando = Cachorro('Jade', 8, 30, (0, 0, 0))
print(catioroAndando.age)
print(catioroAndando.position)


# Nessa forma de instanciar não precisa ser colocado na ordem, porque o atributo é especificado
catioroCorrendo = Cachorro(name='Amanda', position=(0, 0, 0), age=2, height=12)

print(catioroCorrendo.age)
print(catioroCorrendo.position)
