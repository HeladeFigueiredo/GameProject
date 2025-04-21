from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/' + name + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1]) #0 posição X e 1 posição Y
        self.speed = 0

    @abstractmethod #Decorator
    def move(self):
        pass