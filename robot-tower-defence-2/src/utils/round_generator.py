"""
This module generates rounds
"""
from utils.config import arenas


def generate_rounds(arena: str) -> list:
    """ This function generates randomized rounds for the given arena """
    num_rounds = arenas[arena]["num_rounds"]

    robot_num_base = arenas[arena]["robot_num_base"]
    wave_num_base = arenas[arena]["wave_num_base"]
    spawn_delay_base = arenas[arena]["spawn_delay_base"]
    wave_delay_base = arenas[arena]["wave_delay_base"]
    round_delay_base = arenas[arena]["round_delay_base"]

    spawn_delay_min = arenas[arena]["spawn_delay_min"]

    robot_num_rate = arenas[arena]["robot_num_rate"]
    wave_num_rate = arenas[arena]["wave_num_rate"]
    spawn_delay_rate = arenas[arena]["spawn_delay_rate"]
    wave_delay_rate = arenas[arena]["wave_delay_rate"]
    round_delay_rate = arenas[arena]["round_delay_rate"]

    def generate_wave(num_round: int) -> list:
        robot_num = round(robot_num_base * robot_num_rate**(num_round-1))

        minx_num = 0
        nathan_num = 0
        archie_num = 0

        wave_delay = wave_delay_base * wave_delay_rate**(num_round-1)

        wave = {"robots": [], "wave_delay": wave_delay}

        if robot_num > 100:
            archie_num = robot_num // 100
            robot_num -= archie_num * 100

        if robot_num > 10:
            nathan_num = robot_num // 10
            robot_num -= nathan_num * 10

        minx_num = robot_num

        spawn_delay_minx = max(spawn_delay_min, round(spawn_delay_base *
                                                      spawn_delay_rate**(num_round-1)))
        spawn_delay_nathan = max(spawn_delay_min, round(spawn_delay_base *
                                                        spawn_delay_rate**(max(1, num_round-1-20))))
        spawn_delay_archie = max(spawn_delay_min, round(spawn_delay_base *
                                                        spawn_delay_rate**(max(1, num_round-1-40))))

        for _ in range(archie_num):
            robot = {"type": "archie", "spawn_delay": spawn_delay_archie}
            wave["robots"].append(robot)

        for _ in range(nathan_num):
            robot = {"type": "nathan", "spawn_delay": spawn_delay_nathan}
            wave["robots"].append(robot)

        for _ in range(minx_num):
            robot = {"type": "minx", "spawn_delay": spawn_delay_minx}
            wave["robots"].append(robot)

        return wave

    def generate_round(num_round: int) -> list:
        wave_num = round(wave_num_base * wave_num_rate**(num_round-1))
        round_delay = round_delay_base * round_delay_rate**(num_round-1)

        waves = [generate_wave(num_round) for _ in range(1, wave_num+1)]

        return {"waves": waves, "round_delay": round_delay}

    return [generate_round(i) for i in range(1, num_rounds+1)]
