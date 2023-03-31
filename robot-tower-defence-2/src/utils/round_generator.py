"""
This module generates rounds
"""
from random import uniform
from game.arenas.arenas import arenas


def generate_rounds(arena: str) -> list:
    """ This function generates randomized rounds for the given arena """
    num_rounds = arenas[arena]["num_rounds"]
    spawn_location = arenas[arena]["spawn_location"]
    robot_num_multiplier = arenas[arena]["robot_num_multiplier"]
    wave_num_multiplier = arenas[arena]["wave_num_multiplier"]

    def generate_wave(num_round: int) -> list:
        wave = []
        robots_in_wave = int(10 * num_round * robot_num_multiplier)
        for _ in range(robots_in_wave):
            health = uniform(1, 5)
            robot = {"health": health, "spawn_location": spawn_location}
            wave.append(robot)
        return wave

    def generate_round(num_round: int) -> list:
        current_round = []
        waves_in_round = int(min(max((num_round/10)*wave_num_multiplier, 1), 10))
        for _ in range(waves_in_round):
            wave = generate_wave(num_round)
            current_round.append(wave)
        return current_round

    return [generate_round(i) for i in range(num_rounds)]
