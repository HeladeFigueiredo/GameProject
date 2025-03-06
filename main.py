import pygame

pygame.init()
windown = pygame.display.set_mode((800, 600))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #Fechar a window
            quit() #Fechar o pygame
