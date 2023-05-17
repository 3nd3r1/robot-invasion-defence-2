""" src/ui/components/icon_button.py """
import pygame

from utils.sheet_reader import get_sheet_images


class IconButtonGroup(pygame.sprite.Group):
    def draw(self, screen):
        """ Draws all buttons in the group """
        for button in self:
            if button.rect.collidepoint(pygame.mouse.get_pos()):
                button.on_hover()
            else:
                button.on_unhover()
            screen.blit(button.image, button.rect)

    def on_click(self, pos):
        """ Checks if a button was clicked """
        for button in self:
            if button.rect.collidepoint(pos):
                button.on_click()


class IconButton(pygame.sprite.Sprite):
    """ A button that displays an icon """

    def __init__(self, sheet, pos, on_click, *args):
        """ sheet: the (2x1) sprite sheet to use. sheet has default image and hover image """
        super().__init__()
        self.__images = self.__load_images(sheet)

        self.image = self.__images[0]
        self.rect = self.image.get_rect(center=pos)

        self.__click_handler = on_click
        self.__click_handler_args = args

    def __load_images(self, sheet):
        """ Loads the images from the sprite sheet """
        images = []
        for image in get_sheet_images(sheet, (2, 1)):
            images.append(pygame.transform.scale_by(image, 4))
        return images

    def on_click(self):
        self.__click_handler(*self.__click_handler_args)

    def on_hover(self):
        self.image = self.__images[1]

    def on_unhover(self):
        self.image = self.__images[0]
