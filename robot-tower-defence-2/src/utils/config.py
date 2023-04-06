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
        "robot_num_multiplier": 1,
        "wave_num_multiplier": 1,
        "map_file": "grass_fields.tmx"
    }
}

towers = {
    "base": "towers/base.png",
    "turret": {
        "name": "Turret",
        "price": 200,
        "range": 200,
        "shoot_interval": 10,
        "projectile_start_offset": (20, -70),
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
    "mech": {
        "name": "Mech",
        "speed": 1,
        "damage": 1,
        "walk_sheet": "robots/mech/walk.png",
        "walk_rects": [(0, 0, 64, 64), (64, 0, 64, 64), (128, 0, 64, 64), (192, 0, 64, 64), (256, 0, 64, 64), (320, 0, 64, 64), (384, 0, 64, 64), (448, 0, 64, 64), (0, 64, 64, 64), (64, 64, 64, 64), (128, 64, 64, 64), (192, 64, 64, 64), (256, 64, 64, 64), (320, 64, 64, 64), (384, 64, 64, 64), (448, 64, 64, 64), (0, 128, 64, 64), (64, 128, 64, 64), (128, 128, 64, 64), (192, 128, 64, 64), (256, 128, 64, 64), (320, 128, 64, 64), (384, 128, 64, 64), (448, 128, 64, 64), (0, 192, 64, 64), (64, 192, 64, 64), (128, 192, 64, 64), (192, 192, 64, 64), (256, 192, 64, 64), (320, 192, 64, 64), (384, 192, 64, 64), (448, 192, 64, 64)],
        "animation_interval": 10,
    }
}

images = {
    "game_background": "ui/game_background.png"
}
