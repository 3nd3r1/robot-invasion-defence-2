"""
This module generates rounds
"""
from random import randint
from utils.config import arenas


def generate_rounds(arena: str) -> list:
    """ This function generates randomized rounds for the given arena """
    num_rounds = arenas[arena]["num_rounds"]

    robot_num_base = arenas[arena]["robot_num_base"]
    wave_num_base = arenas[arena]["wave_num_base"]
    spawn_interval_base = arenas[arena]["spawn_interval_base"]
    wave_interval_base = arenas[arena]["wave_interval_base"]
    round_delay_base = arenas[arena]["round_delay_base"]

    robot_num_rate = arenas[arena]["robot_num_rate"]
    wave_num_rate = arenas[arena]["wave_num_rate"]
    spawn_interval_rate = arenas[arena]["spawn_interval_rate"]
    wave_interval_rate = arenas[arena]["wave_interval_rate"]
    round_delay_rate = arenas[arena]["round_delay_rate"]

    def generate_wave(num_round: int) -> list:
        robot_num = round(robot_num_base * robot_num_rate**(num_round-1))

        minx_num = 0
        nathan_num = 0
        archie_num = 0

        spawn_interval = round(spawn_interval_base *
                               spawn_interval_rate**(num_round-1))

        wave = {"robots": [], "spawn_interval": spawn_interval}

        if robot_num > 100:
            archie_num = robot_num // 100
            robot_num -= archie_num * 100

        if robot_num > 10:
            nathan_num = robot_num // 10
            robot_num -= nathan_num * 10

        minx_num = robot_num

        for _ in range(minx_num):
            robot = {"type": "minx"}
            wave["robots"].append(robot)

        for _ in range(nathan_num):
            robot = {"type": "nathan"}
            wave["robots"].append(robot)

        for _ in range(archie_num):
            robot = {"type": "archie"}
            wave["robots"].append(robot)

        return wave

    def generate_round(num_round: int) -> list:
        wave_num = round(wave_num_base * wave_num_rate**(num_round-1))
        wave_interval = wave_interval_base * wave_interval_rate**(num_round-1)
        round_delay = round_delay_base * round_delay_rate**(num_round-1)

        return {"waves": [generate_wave(num_round) for _ in range(1, wave_num+1)], "wave_interval": wave_interval, "round_delay": round_delay}

    return [generate_round(i) for i in range(1, num_rounds+1)]
