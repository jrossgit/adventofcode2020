from typing import Tuple

def get_seat_id(seat_partition: str) -> int:

    return int(seat_partition
        .replace("F", "0").replace("B", "1")
        .replace("L", "0").replace("R", "1"),
        base=2

    )
def max_boarding_pass(input_file: str) -> int:

    with open(f"inputs/{input_file}") as f:
        return max([get_seat_id(line.strip()) for line in f.readlines()])


def find_seat(input_file: str) -> int:

    with open(f"inputs/{input_file}") as f:
        seats = sorted([get_seat_id(line.strip()) for line in f.readlines()])

    for i in range(2, len(seats) - 1):
        if seats[i] - seats[i-1] == 1 and seats[i+1] - seats[i] == 2:
            return seats[i] + 1

if __name__ == '__main__':
    print(max_boarding_pass('day_5'))
    print(find_seat('day_5'))
