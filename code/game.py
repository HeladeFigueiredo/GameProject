import pygame

from code.const import WINDOW_HEIGHT, WINDOW_WIDTH, MENU_OPTIONS
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run() #Retorna o menu selecionado

            if menu_return in [MENU_OPTIONS[0], MENU_OPTIONS[1], MENU_OPTIONS[2]]: #Game 1P, Game 2P Coop, Game 2P Comp
                level = Level(self.window, 'Level1', menu_return) #Cria
                level_return = level.run() #Executa
            elif menu_return == MENU_OPTIONS[4]: #Quit
                pygame.display.quit() #Fecha a janela
                quit() #Fecha o pygame
            else:
                pass


