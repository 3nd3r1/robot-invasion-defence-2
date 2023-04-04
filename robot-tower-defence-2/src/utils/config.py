""" src/utils/config.py """
general = {
    "debug": True,
    "display_width": 1220,
    "display_height": 774
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
        "range": 100,
        "can_be_in_water": False,
        "model_1": "towers/turret/1.png",
        "model_2": "towers/turret/2.png",
        "model_3": "towers/turret/3.png",
        "projectile": "towers/turret/projectile.png"
    }
}

images = {
    "game_background": "ui/game_background.png"
}
