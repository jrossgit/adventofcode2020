from typing import List


def task1(input_numbers: List, end_step: int):

    last_seen = {number: i for i, number in enumerate(input_numbers[:-1])}
    previous_number = input_numbers[-1]

    for i in range(len(input_numbers), end_step):

        if previous_number in last_seen:
            current_number = i - last_seen[previous_number] - 1
        else:
            current_number = 0
        last_seen[previous_number] = i - 1

        previous_number = current_number

    return current_number


if __name__ == "__main__":

    print(task1([1, 0, 16, 5, 17, 4], 2020))
    print(task1([1, 0, 16, 5, 17, 4], 30000000))
