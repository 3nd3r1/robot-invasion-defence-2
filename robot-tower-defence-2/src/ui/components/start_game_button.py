import pygame
from utils.config import fonts, colors
from utils.file_reader import get_font


class StartGameButtonGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.__selected_arena = None

    def on_click(self, pos):
        for sprite in self:
            if sprite.rect.collidepoint(pos) and sprite.arena == self.__selected_arena:
                sprite.on_click()

    def draw(self, screen):
        for sprite in self:
            if sprite.arena != self.__selected_arena:
                continue

            screen.blit(sprite.image, sprite.rect)
            if sprite.rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(screen, colors["default_font_color"], sprite.rect.move(0, 10), 2)

    def select_arena(self, arena):
        self.__selected_arena = arena


class StartGameButton(pygame.sprite.Sprite):
    fonts = {}

    def __init__(self, text, pos, on_click, arena):
        super().__init__()
        self.image = pygame.surface.Surface((300, 50))
        self.rect = self.image.get_rect(center=pos)

        self.__click_handler = on_click

        self.arena = arena

        self.__text = text
        self.__render_text()

    @staticmethod
    def load_assets():
        StartGameButton.fonts["default"] = pygame.font.Font(get_font(fonts["default"]), 50)

    def on_click(self):
        self.__click_handler(self.arena)

    def __render_text(self):
        font = StartGameButton.fonts["default"]
        font_color = colors["default_font_color"]

        text = font.render(self.__text, True, font_color)

        text_rect = text.get_rect(center=self.image.get_rect().center)

        self.image.blit(text, text_rect)
