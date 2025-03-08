from aula.cachorro_class import Cachorro
from aula.cat_class import Cat

class AnimalFactory:

    @staticmethod
    def new_animal(animal_type, name, age, weight, height):
        match animal_type:
            case 'dog':
                return Cachorro(name=name, age=age, position=0, weight=weight, height=height)
            case 'cat':
                return Cat(name=name, age=age, position=20, weight=weight, height=height)