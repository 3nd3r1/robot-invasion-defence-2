import pygame
from utils.config import fonts, colors
from utils.file_reader import get_font


class MenuButton(pygame.sprite.Sprite):
    fonts = {}

    def __init__(self, text, pos, on_click, *args):
        super().__init__()
        self.image = pygame.surface.Surface((300, 50), pygame.constants.SRCALPHA, 32)
        self.rect = self.image.get_rect(center=pos)

        self.__click_handler = on_click
        self.__click_handler_args = args

        self.__text = text
        self.__render_text()

        pygame.draw.rect(self.image, (0, 0, 0), self.rect)

    @staticmethod
    def load_assets():
        MenuButton.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 50)

    def on_click(self):
        self.__click_handler(*self.__click_handler_args)

    def __render_text(self):
        font = MenuButton.fonts["default"]
        font_color = colors["default_font_color"]

        text = font.render(self.__text, True, font_color)
        text_rect = text.get_rect(center=self.image.get_rect().center)

        self.image.blit(text, text_rect)
