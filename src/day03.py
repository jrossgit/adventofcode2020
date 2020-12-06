import logging
from math import prod
import re
from typing import Tuple


def toboggan_trees(input_file: str, steps_across: int, steps_down: int) -> int:
    """
    Takes a map of a toboggan run and, following discrete steps down the map,
    returns a number of trees (represented by hashes) encountered

    :param input_file: Name of file containing data

    :returns: int - Number of trees encountered
    """
    position = {"x": 0, "y": 0}
    number_of_trees = 0
    with open(f"inputs/{input_file}") as f:
        for line in f.readlines():
            if position["y"] % steps_down:
                position["y"] += 1
                continue

            if line[position["x"] % len(line.strip())] == "#":
                number_of_trees += 1
            position["x"] += steps_across
            position["y"] += 1

    return number_of_trees


def toboggan_trees_task_2(input_file: str) -> Tuple[Tuple, int]:

    results = (
        toboggan_trees(input_file, 1, 1),
        toboggan_trees(input_file, 3, 1),
        toboggan_trees(input_file, 5, 1),
        toboggan_trees(input_file, 7, 1),
        toboggan_trees(input_file, 1, 2),
    )

    return (results, prod(results))


if __name__ == "__main__":
    print(toboggan_trees("day_3", 3, 1))
    print(toboggan_trees_task_2("day_3"))
