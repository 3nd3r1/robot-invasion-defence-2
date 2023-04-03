""" Settings for all arenas """
from game.arenas import GRASS_FIELDS

arenas = {
    "grass_fields": {
        "num_rounds": GRASS_FIELDS.NUM_ROUNDS,
        "spawn_location": GRASS_FIELDS.SPAWN_LOCATION,
        "robot_num_multiplier": GRASS_FIELDS.ROBOT_NUM_MULTIPLIER,
        "wave_num_multiplier": GRASS_FIELDS.WAVE_NUM_MULTIPLIER,
        "map_file": GRASS_FIELDS.MAP_FILE
    }
}
