""" Settings for all arenas """
from game.arenas import grass_fields

arenas = {
    "grass_fields": {
        "num_rounds": grass_fields.NUM_ROUNDS,
        "spawn_location": grass_fields.SPAWN_LOCATION,
        "robot_num_multiplier": grass_fields.ROBOT_NUM_MULTIPLIER,
        "wave_num_multiplier": grass_fields.WAVE_NUM_MULTIPLIER,
        "map_file": grass_fields.MAP_FILE
    }
}
