""" src/ui/start_game_menu.py """
import pygame

from ui.components.menu_button import MenuButtonGroup, MenuButton
from ui.components.start_game_button import StartGameButtonGroup, StartGameButton
from ui.components.icon_button import IconButtonGroup, IconButton

from utils.config import fonts, colors, images, arenas
from utils.file_reader import get_font
from utils.db import get_player_scores, get_game_saves
from utils.text import draw_text


class StartGameMenu:
    """ Static class for the start game menu """
    select_buttons = MenuButtonGroup()
    icon_buttons = IconButtonGroup()
    start_buttons = StartGameButtonGroup()
    fonts = {}

    selected_arena = None
    player_scores = {}
    player_saves = {}

    @staticmethod
    def load_assets():
        StartGameMenu.fonts["title"] = pygame.font.Font(get_font(fonts["default"]), 100)
        StartGameMenu.fonts["arena_info"] = pygame.font.Font(get_font(fonts["default"]), 50)
        StartGameButton.load_assets()

    @staticmethod
    def load_menu(screen, set_state, start_game):
        select_pos = (350, screen.get_height() / 2 - 50)
        start_pos = (900, 500)

        StartGameMenu.player_scores = get_player_scores()
        StartGameMenu.player_saves = get_game_saves()

        StartGameMenu.select_buttons.add(MenuButton(
            "Grass Fields", select_pos, StartGameMenu.select_arena, "grass_fields"))

        StartGameMenu.start_buttons.add(StartGameButton(
            "New Game", start_pos, start_game, "grass_fields"))
        if StartGameMenu.player_saves.get("grass_fields", False):
            StartGameMenu.start_buttons.add(StartGameButton(
                "Continue", (start_pos[0], start_pos[1] + 100), start_game, "grass_fields", 1))

        StartGameMenu.icon_buttons.add(IconButton(
            images["ui"]["back_button"], (67, 100), set_state, "main_menu"))

    @staticmethod
    def draw(screen):
        title_pos = (400, 180)
        font = StartGameMenu.fonts["title"]
        color = colors["default_font_color"]

        draw_text(screen, font, color, "Select Arena", title_pos)

        StartGameMenu.select_buttons.draw(screen)
        StartGameMenu.icon_buttons.draw(screen)

        StartGameMenu.draw_arena_info(screen)

    @staticmethod
    def draw_arena_info(screen):
        if not StartGameMenu.selected_arena:
            return

        title_font = StartGameMenu.fonts["title"]
        info_font = StartGameMenu.fonts["arena_info"]
        font_color = colors["default_font_color"]

        arena = StartGameMenu.selected_arena
        title = arenas[arena]["title"]
        description = arenas[arena]["description"]
        max_round = arenas[arena]["num_rounds"]
        highscore = StartGameMenu.player_scores.get(arena, 0)

        draw_text(screen, title_font, font_color, title, (900, 180))
        draw_text(screen, info_font, font_color, description, (900, 250))
        draw_text(screen, info_font, font_color, f"Rounds: {max_round}", (900, 350))
        draw_text(screen, info_font, font_color, f"Highscore: {highscore}/{max_round}", (900, 380))

        StartGameMenu.start_buttons.draw(screen)

    @staticmethod
    def on_click(pos):
        StartGameMenu.select_buttons.on_click(pos)
        StartGameMenu.icon_buttons.on_click(pos)
        StartGameMenu.start_buttons.on_click(pos)

    @staticmethod
    def select_arena(arena):
        StartGameMenu.selected_arena = arena
        StartGameMenu.start_buttons.select_arena(arena)
