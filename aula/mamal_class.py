from aula.animal_class import Animal


class Mamal(Animal):
    def __init__(self, name, age, height, position, fur: str):
        super().__init__(name, age, height, position)
        self.fur = fur

