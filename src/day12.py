from cmath import exp


class Ship:

    DIRECTIONS = ["N", "E", "S", "W"]

    def __init__(self, direction):
        self.direction = direction
        self.location = [0, 0]

    def execute(self, instruction):

        command = instruction[0]
        value = int(instruction[1:])
        if command == "F":
            self.move(self.direction, value)
        elif command in self.DIRECTIONS:
            self.move(command, value)
        elif command == "R":
            index = (self.DIRECTIONS.index(self.direction) + int(value / 90)) % 4
            self.direction = self.DIRECTIONS[index]
        elif command == "L":
            index = (self.DIRECTIONS.index(self.direction) - int(value / 90)) % 4
            self.direction = self.DIRECTIONS[index]
        else:
            raise RuntimeError(f"{instruction} not recognised")

    @property
    def manhatten_distance(self):
        return abs(self.location[0]) + abs(self.location[1])

    def move(self, direction, value):

        if direction == "N":
            self.location[1] += value
        if direction == "E":
            self.location[0] += value
        if direction == "S":
            self.location[1] -= value
        if direction == "W":
            self.location[0] -= value


class ShipWaypoint:
    def __init__(self, waypoint):
        self.waypoint = waypoint
        self.location = 0 + 0j

    def execute(self, instruction):

        command = instruction[0]
        value = int(instruction[1:])
        if command == "F":
            self.location += self.waypoint * value
        elif command == "N":
            self.waypoint += value * (0 + 1j)
        elif command == "S":
            self.waypoint += value * (0 - 1j)
        elif command == "E":
            self.waypoint += value
        elif command == "W":
            self.waypoint -= value
        elif command == "R":
            self.waypoint = self.waypoint * (0 - 1j) ** (value / 90)
        elif command == "L":
            self.waypoint = self.waypoint * (0 + 1j) ** (value / 90)
        else:
            raise RuntimeError(f"{instruction} not recognised")

    @property
    def manhatten_distance(self):
        return abs(self.location.real) + abs(self.location.imag)


def task_1(input_file: str) -> int:
    with open(f"inputs/{input_file}") as f:
        plan = [line.strip() for line in f.readlines()]

    ship = Ship("E")
    for instruction in plan:
        ship.execute(instruction)
    return ship.manhatten_distance


def task_2(input_file: str) -> int:
    with open(f"inputs/{input_file}") as f:
        plan = [line.strip() for line in f.readlines()]

    ship = ShipWaypoint(10 + 1j)
    for instruction in plan:
        ship.execute(instruction)
    return ship.manhatten_distance


if __name__ == "__main__":
    print(task_1("day_12"))
    print(task_2("day_12"))
