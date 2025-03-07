import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WINDOW_WIDTH, WINDOW_HEIGHT, COLOR_ORANGE, MENU_OPTIONS, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/menuBackground.png')  # Carrego a imagem
        self.rect = self.surf.get_rect(left=0,
                                       top=0)  # Crio o retangulo e mesmo que esse já seja o default, está também explícito que vai começar no canto superior esquerdo

    def run(self):
        pygame.mixer.music.load('./asset/theme_music.wav')
        # pygame.mixer.music.play(
        #     -1)
        # O parâmetro -1 indica que quando a música finalizar ela deve começar de novo infinitamente

        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # Desenha uma imagem dentro da outra
            self.menu_text(text='CYBERPUNK:', text_size=90, text_color=COLOR_ORANGE,
                           text_center_post=((WINDOW_WIDTH / 2), 125))
            self.menu_text(text='FOR GIRLS AND GAYMERS', text_size=35, text_color=COLOR_ORANGE,
                           text_center_post=((WINDOW_WIDTH / 2), 165))

            for title in range(len(MENU_OPTIONS)):
                self.menu_text(text=MENU_OPTIONS[title], text_size=30, text_color=COLOR_WHITE,
                               text_center_post=((WINDOW_WIDTH / 2), 350 + 38 * title))

            pygame.display.flip()  # Atualiza o display

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Fechar a window
                    quit()  # Fechar o pygame

    def menu_text(self, text: str, text_size: int, text_color: tuple, text_center_post: tuple):
        # TODO: TROCAR A FONTE
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)  # Qual fonte será usada
        text_surf: Surface = text_font.render(text, True,
                                              text_color).convert_alpha()  # Renderiza e cria uma superfície com o texto
        text_rect: Rect = text_surf.get_rect(center=text_center_post)  # Cria um retangulo
        self.window.blit(source=text_surf,
                         dest=text_rect)  # Desenha uma imagem dentro da outra, no caso a imagem do texto em cima da imagem do retangulo
