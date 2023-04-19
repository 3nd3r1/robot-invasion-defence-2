""" src/utils/config.py """
general = {
    "debug": True,
    "display_width": 1220,
    "display_height": 774,
    "fps": 60,
}

arenas = {
    "grass_fields": {
        "num_rounds": 100,
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
        "projectile_damage": 5,
        "projectile_explosion_radius": 160,
        "projectile_explosion_damage": 10,
        "can_be_in_water": False,
    },
    "cannon": {
        "name": "cannon",
        "cost": 200,
        "range": 200,
        "shoot_interval": 500,
        "projectile_start_offset": (0, -20),
        "projectile_speed": 10,
        "projectile_damage": 1,
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
        "base_bounty": 1,
        "path_offset": (0, 0),
        "animation_interval": 100,
    },
    "nathan": {
        "name": "NATHAN",
        "health": 5,
        "speed": 1,
        "base_damage": 1,
        "base_bounty": 1,
        "path_offset": (0, 0),
        "animation_interval": 10,
    },
    "archie": {
        "name": "ARCHIE",
        "health": 100,
        "speed": 1,
        "base_damage": 1,
        "base_bounty": 1,
        "path_offset": (0, 0),
        "animation_interval": 100,
    }
}

images = {
    "ui": {
        "game_background": "ui/game_background.png",
    },
    "particles": {
        "explosion": {
            "sheet": "particles/explosion.png",
            "sheet_size": (4, 5),  # (columns, rows)
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
        "base": "towers/base.png",
        "turret": {
            "model_1": "towers/turret/1.png",
            "model_2": "towers/turret/2.png",
            "model_3": "towers/turret/3.png",
        },
        "missile_launcher": {
            "model_1": "towers/missile_launcher/1.png",
            "model_2": "towers/missile_launcher/2.png",
            "model_3": "towers/missile_launcher/3.png",
        },
        "cannon": {
            "model_1": "towers/cannon/1.png",
            "model_2": "towers/cannon/2.png",
            "model_3": "towers/cannon/3.png",
        }
    },
    "projectiles": {
        "bullet": "projectiles/bullet.png",
        "missile": "projectiles/missile.png",
        "shell": "projectiles/shell.png"
    }
}

colors = {
    "invalid_tower_range": (255, 0, 0, 100),
    "valid_tower_range": (50, 50, 50, 50),
}
