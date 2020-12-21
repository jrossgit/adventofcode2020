from typing import Callable, List, Tuple


NEIGHBOURS = [
    [0, 1],
    [0, -1],
    [1, -1],
    [1, 0],
    [1, 1],
    [-1, -1],
    [-1, 0],
    [-1, 1],
]


def number_neighbours_immediate(plan: List[str], row: int, col: int) -> int:
    no_neighbours = 0
    for neighbour in NEIGHBOURS:
        x, y = neighbour
        try:
            if col + x >= 0 and row + y >= 0 and plan[col + x][row + y] == "#":
                no_neighbours += 1
        except IndexError:
            pass
    return no_neighbours


def number_neighbours_line_of_sight(plan: List[str], row: int, col: int) -> int:
    no_neighbours = 0
    for neighbour in NEIGHBOURS:
        x, y = neighbour
        i = 1
        try:
            while col + x * i >= 0 and row + y * i >= 0:
                if plan[col + x * i][row + y * i] == "#":
                    no_neighbours += 1
                    break
                elif plan[col + x * i][row + y * i] == "L":
                    break
                i = i + 1
        except IndexError:
            continue
    return no_neighbours


def iterate(
    plan: List[str], seat_tolerance: int, neighbour_algo: Callable
) -> Tuple[bool, List]:
    width = len(plan[0])
    length = len(plan)
    changed = False

    plan_out: List[str] = []
    for col in range(length):
        next_row = []
        for row in range(width):
            if plan[col][row] == ".":
                next_row.append(".")
                continue
            no_neighbours = neighbour_algo(plan, row, col)
            if plan[col][row] == "#" and no_neighbours >= seat_tolerance:
                next_row.append("L")
                changed = True
            elif plan[col][row] == "#" and no_neighbours < seat_tolerance:
                next_row.append("#")
            elif plan[col][row] == "L" and no_neighbours == 0:
                next_row.append("#")
                changed = True
            elif plan[col][row] == "L" and no_neighbours > 0:
                next_row.append("L")
        plan_out.append("".join(next_row))
    return (changed, plan_out)


def task_1(input_file: str) -> int:
    with open(f"inputs/{input_file}") as f:
        plan = [line.strip() for line in f.readlines()]

    changed = True
    while changed:
        changed, plan = iterate(plan, 4, number_neighbours_immediate)

    return sum([s.count("#") for s in plan])


def task_2(input_file: str) -> int:
    with open(f"inputs/{input_file}") as f:
        plan = [line.strip() for line in f.readlines()]

    changed = True
    while changed:
        changed, plan = iterate(plan, 5, number_neighbours_line_of_sight)

    return sum([s.count("#") for s in plan])


if __name__ == "__main__":
    print(task_1("day_11"))
    print(task_2("day_11"))
