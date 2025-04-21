from code.const import WINDOW_WIDTH, ENTITY_SPEED
from code.entity import Entity

class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name] #Velocidade das imagens
        if self.rect.right <= 0:
            self.rect.left = WINDOW_WIDTH
        pass