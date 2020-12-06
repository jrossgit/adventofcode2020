from typing import Tuple

Vector = Tuple[int]


def puzzle_01(input_file: str) -> Tuple[int, int, int]:
    """
    Takes a data file containing a list of integers (one per line),
    finds the two integers summing 2020 and multiplies them together

    :param input_file: Name of file containing data

    :returns: Tuple - (first number, second number, two numbers multiplied)
    """
    with open(f"inputs/{input_file}") as f:
        numbers = sorted([int(line.strip()) for line in f.readlines()])

    for number in numbers:
        if 2020 - number in numbers:
            return number, 2020 - number, number * (2020 - number)

    raise ValueError("Failed to find combination of numbers")


def puzzle_02(input_file: str) -> Tuple[int, int, int, int]:
    """
    Takes a data file containing a list of integers (one per line),
    finds the two integers summing 2020 and multiplies them together

    :param input_file: Name of file containing data

    :returns: Tuple - (first number, second number, two numbers multiplied)
    """
    with open(f"inputs/{input_file}") as f:
        numbers = sorted([int(line.strip()) for line in f.readlines()])

    for index, number1 in enumerate(numbers):
        difference = 2020 - number1
        for number2 in numbers[index:]:

            if difference - number2 in numbers:
                return (
                    number1,
                    number2,
                    difference - number2,
                    number1 * number2 * (difference - number2),
                )

    raise ValueError("Failed to find combination of numbers")


if __name__ == "__main__":

    print(puzzle_02("day_1"))
