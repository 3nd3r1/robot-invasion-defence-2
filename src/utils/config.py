""" src/utils/config.py """
import os
import sys
from dotenv import load_dotenv
from utils.file_reader import get_env

try:
    load_dotenv(dotenv_path=get_env(".env"))
    load_dotenv(dotenv_path=get_env(".env.local"))
except FileNotFoundError:
    pass

general = {
    "debug": (os.getenv("DEBUG") == "True" or sys.argv[-1] == "debug"),
    "screen_width": 1280,
    "screen_height": 720,
    "fps": 60,
    "db_location": os.getenv("DATABASE_FILENAME", "database.db"),
}

arenas = {
    "grass_fields": {
        "title": "Grass Fields",
        "description": ["A large open field", "with a few trees and rocks."],
        "experience_reward": 100,
        "num_rounds": 60,
        "starting_money": 250,
        "map_file": "grass_fields.tmx",
        # The following rates are calculated with the formula: (final/base)**(1/num_rounds)

        # The base number of robots in a wave
        "robot_num_base": 10,
        # The rate at which the number of robots in a wave increases
        "robot_num_rate":  1.071519,
        # The base number of waves in a round
        "wave_num_base": 2,
        # The rate at which the number of waves in a round increases
        "wave_num_rate": 1.02035,
        # The base spawn interval of a wave
        "spawn_delay_base": 1000,
        # The minimum value of the spawn interval
        "spawn_delay_min": 100,
        # The rate at which the spawn interval of a wave increases
        "spawn_delay_rate": 0.63095,
        # The base wave interval of a round
        "wave_delay_base": 1000,
        # The rate at which the wave interval of a round increases
        "wave_delay_rate": 0.977237,
        # The base round delay
        "round_delay_base": 10000,
        # The rate at which the round delay increases
        "round_delay_rate": 0.977237,
    }
}

towers = {
    "base": "towers/base.png",
    "turret": {
        "name": "Turret",
        "cost": 200,
        "range": 200,
        "shoot_interval": 500,
        "projectile_start_offset": (0, -20),
        "projectile_speed": 10,
        "projectile_damage": 1,
        "projectile_explosion_radius": 0,
        "projectile_explosion_damage": 0,
        "can_be_in_water": False,
    },
    "missile_launcher": {
        "name": "Missile Launcher",
        "cost": 400,
        "range": 400,
        "shoot_interval": 2000,
        "projectile_start_offset": (0, -20),
        "projectile_speed": 20,
        "projectile_damage": 2,
        "projectile_explosion_radius": 110,
        "projectile_explosion_damage": 1,
        "can_be_in_water": False,
    },
    "cannon": {
        "name": "cannon",
        "cost": 325,
        "range": 200,
        "shoot_interval": 3000,
        "projectile_start_offset": (0, -20),
        "projectile_speed": 20,
        "projectile_damage": 30,
        "projectile_explosion_radius": 0,
        "projectile_explosion_damage": 0,
        "can_be_in_water": False,
    }
}

robots = {
    "minx": {
        "name": "MINX",
        "health": 1,
        "speed": 2,
        "base_damage": 1,
        "base_bounty": 2,
        "path_offset": (0, 0),
        "animation_interval": 100,
    },
    "nathan": {
        "name": "NATHAN",
        "health": 5,
        "speed": 1,
        "base_damage": 5,
        "base_bounty": 10,
        "path_offset": (0, 0),
        "animation_interval": 100,
    },
    "archie": {
        "name": "ARCHIE",
        "health": 100,
        "speed": 1,
        "base_damage": 30,
        "base_bounty": 200,
        "path_offset": (0, 0),
        "animation_interval": 100,
    }
}

images = {
    "ui": {
        "game_background": "ui/game_background.png",
        "ui_background": "ui/ui_background.png",
        "tower_button_background": "ui/tower_button_background.png",
        "arrow_up_button": "ui/arrow_up_button.png",
        "arrow_down_button": "ui/arrow_down_button.png",
        "pause_button": "ui/pause_button.png",  # (2x1 sheet)
        "back_button": "ui/continue_button.png",  # (2x1 sheet)
        "icon": "ui/icon.png",

    },
    "particles": {
        # Image contains tuple with sheet path, sheet size and tile scale
        "explosion": {
            "sheet": ("particles/explosion.png", (4, 5), 2),
            "animation_interval": 20,
        }
    },
    "robots": {
        "minx": {
            "walk_sheet": "robots/minx/walk.png",
            "walk_sheet_size": (9, 4),  # (columns, rows)
        },
        "nathan": {
            "walk_sheet": "robots/nathan/walk.png",
            "walk_sheet_size": (8, 4),  # (columns, rows)
        },
        "archie": {
            "walk_sheet": "robots/archie/walk.png",
            "walk_sheet_size": (8, 4),  # (columns, rows)
        }
    },
    "towers": {
        # Images contain tuple with image path, scale and offset
        "base": ("towers/base.png", 0.25),
        "turret": {
            "model_1": ("towers/turret/1.png", 0.4, (-10, -15)),
            "model_2": ("towers/turret/2.png", 0.4, (-10, -15)),
            "model_3": ("towers/turret/3.png", 0.4, (-10, -15)),
        },
        "missile_launcher": {
            "model_1": ("towers/missile_launcher/1.png", 0.35, (0, -15)),
            "model_2": ("towers/missile_launcher/2.png", 0.35, (0, -15)),
            "model_3": ("towers/missile_launcher/3.png", 0.35, (0, -15)),
        },
        "cannon": {
            "model_1": ("towers/cannon/1.png", 0.3, (0, -16)),
            "model_2": ("towers/cannon/2.png", 0.3, (0, -16)),
            "model_3": ("towers/cannon/3.png", 0.3, (0, -16)),
        }
    },
    "projectiles": {
        "turret": ("projectiles/bullet.png", 0.5),
        "missile_launcher": ("projectiles/missile.png", 0.5),
        "cannon": ("projectiles/shell.png", 0.5),
    }
}

fonts = {
    "default": "pdz.ttf",
}

colors = {
    "menu_background": (0, 0, 0),
    "invalid_tower_range": (255, 0, 0, 100),
    "valid_tower_range": (50, 50, 50, 50),
    "default_font_color": (192, 235, 248),
    "not_affordable_font_color": (225, 0, 0),
}
