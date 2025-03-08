from abc import ABC

from aula.animal_class import Animal

# Como essa classe também é abstrada, ela não precisa impplementar obrigatoriamente os métodos abstratos de Animal
class Mammal(Animal, ABC):
    def __init__(self, name: str, age: int, weight: int  , height: int, position: int):
        super().__init__(name, age, weight, height, position)

    def fur_types(self):
        pass