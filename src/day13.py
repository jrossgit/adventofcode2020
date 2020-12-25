from typing import List


def task_1(input_file: str) -> int:
    with open(f"inputs/{input_file}") as f:
        timestamp = int(f.readline())
        ids: List = [int(line) for line in f.readline().split(",") if line != "x"]

    departures = [id - (timestamp % id) for id in ids]

    return min(departures) + timestamp


def earliest_bus_sequence(bus_schedule: List, start_timestamp: int = 0) -> int:

    schedule = [(i, id) for i, id in enumerate(bus_schedule) if id is not None]
    print(schedule)

    time = 0
    repeat = schedule[0][1]
    for i, bus_id in schedule[1:]:

        while (time % bus_id) != (bus_id - i) % bus_id:
            time += repeat

        print(time, repeat, bus_id)
        repeat *= bus_id
    return time


def task_2(input_file: str) -> int:
    with open(f"inputs/{input_file}") as f:
        _ = int(f.readline())
        ids: List = []
        for service in f.readline().split(","):
            if service == "x":
                ids.append(None)
            else:
                ids.append(int(service))

    return earliest_bus_sequence(ids)


if __name__ == "__main__":

    print(task_1("day_13"))
    print(task_2("day_13"))
