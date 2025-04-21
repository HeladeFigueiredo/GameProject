import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WINDOW_WIDTH, COLOR_ORANGE, MENU_OPTIONS, COLOR_WHITE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()  # Carrego a imagem
        # Crio o retangulo e mesmo que esse já seja o default, está também explícito que vai começar no canto superior esquerdo
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        pygame.mixer.music.load('./asset/music/theme_music.wav')
        # pygame.mixer.music.play(-1) # O parâmetro -1 indica que quando a música finalizar ela deve começar de novo infinitamente

        while True:
            # Desenha uma imagem dentro da outra
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text='CYBERPUNK:', text_size=50, text_color=COLOR_ORANGE,
                           text_center_post=((WINDOW_WIDTH / 2), 70))
            self.menu_text(text='FOR GIRLS AND GAYMERS', text_size=25, text_color=COLOR_ORANGE,
                           text_center_post=((WINDOW_WIDTH / 2), 100))

            for title in range(len(MENU_OPTIONS)):
                if title == menu_option:
                    # Se o título for igual a opção do menu, então ele vai ficar amarelo
                    self.menu_text(text=MENU_OPTIONS[title], text_size=25, text_color=COLOR_YELLOW, text_center_post=((WINDOW_WIDTH / 2), 200 + 25 * title))
                else:
                    # Se não, ele vai ficar branco
                    self.menu_text(text=MENU_OPTIONS[title], text_size=25, text_color=COLOR_WHITE,
                                   text_center_post=((WINDOW_WIDTH / 2), 200 + 25 * title))
            pygame.display.flip() # Atualiza o display

            # Checagens de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT: #Se o evento for de sair/fechar a janela
                    pygame.quit()  # Fechar a window
                    quit()  # Fechar o pygame

                if event.type == pygame.KEYDOWN:  # Se o evento for de pressionar uma tecla
                    # Tecla para baixo
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTIONS) - 1:
                            menu_option += 1 # Se o menu_option for menor que o tamanho da lista de opções do menu - 1, então ele pode aumentar
                        else:
                            menu_option = 0 # Se não, ele volta para o começo

                    # Tecla para cima
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1 # Se o menu_option for maior que 0, então ele pode diminuir
                        else:
                            menu_option = len(MENU_OPTIONS) - 1 # Se não, ele volta para o final

                    # Tecla enter
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTIONS[menu_option]



    def menu_text(self, text: str, text_size: int, text_color: tuple, text_center_post: tuple):
        # TODO: TROCAR A FONTE
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)  # Qual fonte será usada
        text_surf: Surface = text_font.render(text, True,
                                              text_color).convert_alpha()  # Renderiza e cria uma superfície com o texto
        text_rect: Rect = text_surf.get_rect(center=text_center_post)  # Cria um retangulo
        self.window.blit(source=text_surf,
                         dest=text_rect)  # Desenha uma imagem dentro da outra, no caso a imagem do texto em cima da imagem do retangulo
