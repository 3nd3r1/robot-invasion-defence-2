"""
This module generates rounds
"""
from utils.config import arenas


def generate_robots(robot_num: int, robot_type: str,
                    robot_mod: int, robot_round: int, num_round: int, arena: str) -> list:
    """ This function generates a list of robots """
    spawn_delay_base = arenas[arena]["spawn_delay_base"]
    spawn_delay_rate = arenas[arena]["spawn_delay_rate"]
    spawn_delay_min = arenas[arena]["spawn_delay_min"]

    robots = 0
    if robot_num > robot_mod:
        robots = robot_num // robot_mod

    spawn_delay = max(spawn_delay_min, round(spawn_delay_base *
                                             spawn_delay_rate**(max(1, num_round-1-robot_round))))

    return [{"type": robot_type, "delay": spawn_delay} for _ in range(robots)]


def generate_wave(num_round: int, arena: str) -> list:
    """ This function generates a wave of robots"""
    robot_num_base = arenas[arena]["robot_num_base"]
    robot_num_rate = arenas[arena]["robot_num_rate"]
    wave_delay_base = arenas[arena]["wave_delay_base"]
    wave_delay_rate = arenas[arena]["wave_delay_rate"]

    robot_num = round(robot_num_base * robot_num_rate**(num_round-1))

    wave_delay = wave_delay_base * wave_delay_rate**(num_round-1)

    wave = {"robots": [], "delay": wave_delay}

    wave["robots"] += generate_robots(robot_num, "archie", 100, 40, num_round, arena)
    wave["robots"] += generate_robots(robot_num % 101, "nathan", 10, 20, num_round, arena)
    wave["robots"] += generate_robots(robot_num % 11, "minx", 1, 0, num_round, arena)

    return wave


def generate_round(num_round: int, arena: str) -> list:
    """ This function generates a round of waves"""
    wave_num_base = arenas[arena]["wave_num_base"]
    wave_num_rate = arenas[arena]["wave_num_rate"]
    round_delay_base = arenas[arena]["round_delay_base"]
    round_delay_rate = arenas[arena]["round_delay_rate"]

    wave_num = round(wave_num_base * wave_num_rate**(num_round-1))
    round_delay = round_delay_base * round_delay_rate**(num_round-1)

    waves = [generate_wave(num_round, arena) for _ in range(1, wave_num+1)]

    return {"waves": waves, "delay": round_delay}


def generate_rounds(arena: str) -> list:
    """ This function generates randomized rounds for the given arena """
    num_rounds = arenas[arena]["num_rounds"]
    return [generate_round(i, arena) for i in range(1, num_rounds+1)]
