from aula.animal_factory_class import AnimalFactory

# Não é chamado o constutor do AnimalFactory, é chamado o metodo new_animal

new_dog = AnimalFactory.new_animal(animal_type='dog', name='Catioro Meu', height=20, weight=10, age=1)

print(new_dog.name)
print(new_dog.position)