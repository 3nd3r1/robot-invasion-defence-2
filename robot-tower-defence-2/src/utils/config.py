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
        "spawn_interval_base": 1000,
        # The rate at which the spawn interval of a wave increases
        "spawn_interval_rate": 0.63095,
        # The base wave interval of a round
        "wave_interval_base": 1000,
        # The rate at which the wave interval of a round increases
        "wave_interval_rate": 0.977237,
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
        "price": 200,
        "range": 200,
        "shoot_interval": 500,
        "projectile_start_offset": (0, -20),
        "projectile_speed": 10,
        "projectile_damage": 1,
        "can_be_in_water": False,
        "model_1": "towers/turret/1.png",
        "model_2": "towers/turret/2.png",
        "model_3": "towers/turret/3.png",
        "projectile": "towers/turret/projectile.png"
    }
}

robots = {
    "minx": {
        "name": "MINX",
        "health": 1,
        "speed": 1,
        "base_damage": 1,
        "base_bounty": 1,
        "walk_sheet": "robots/minx/walk.png",
        "walk_sheet_size": (9, 4),  # (columns, rows)
        "animation_interval": 100,
    },
    "nathan": {
        "name": "NATHAN",
        "health": 1,
        "speed": 1,
        "base_damage": 1,
        "base_bounty": 1,
        "walk_sheet": "robots/nathan/walk.png",
        "walk_sheet_size": (8, 4),  # (columns, rows)
        "animation_interval": 100,
    },
    "archie": {
        "name": "ARCHIE",
        "health": 1,
        "speed": 1,
        "base_damage": 1,
        "base_bounty": 1,
        "walk_sheet": "robots/archie/walk.png",
        "walk_sheet_size": (8, 4),  # (columns, rows)
        "animation_interval": 100,
    }
}

images = {
    "game_background": "ui/game_background.png"
}
