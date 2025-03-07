class Animal:
    #Tupla é uma lista estática
    def __init__(self, name: str, age: int, height: int, position: tuple):
        self.name = name
        self.age = age
        self.height = height

        self.position: tuple = position #pode reforçar o tipo do atributo aqui. Pra que? Não sei kk
        # Position será [x, y, z]


        # Função que ao ser chamada, adiciona mais um "passo/movimento" ao animal no eixo X
    def move_x(seft):
        seft.position[0] += 1

    def move_y(seft):
        seft.position[1] += 1

    def move_z(seft):
        seft.position[2] += 1

