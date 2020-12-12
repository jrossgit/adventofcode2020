from itertools import permutations
from typing import List, Optional, Tuple


def valid_combination(values: List[int], total: int) -> bool:
    return total in [sum(perm) for perm in permutations(values, 2)]


def task_01(input_file: str, preamble: int) -> int:
    with open(f"inputs/{input_file}") as f:
        numbers = [int(line) for line in f.readlines()]

    for i in range(len(numbers) - preamble):
        if not valid_combination(numbers[i : i + preamble], numbers[i + preamble]):
            return numbers[i + preamble]

    raise RuntimeError("No invalid step found")


def task_02(input_file: str, target: int) -> Tuple[int, int]:
    with open(f"inputs/{input_file}") as f:
        numbers = [int(line) for line in f.readlines()]

    for i in range(len(numbers)):
        offset = 0
        total = numbers[i]
        while total < target:
            offset += 1
            total += numbers[i + offset]
        if total == target:
            return min(numbers[i : i + offset]), max(numbers[i : i + offset])

    raise RuntimeError("No combination found")


if __name__ == "__main__":
    task_1_result = task_01("day_9", 25)
    print(task_1_result)
    lower, upper = task_02("day_9", task_1_result)
    print(lower + upper)
