from typing import Any, Dict, Iterable, List, Tuple


def task_1(input_file: str) -> Tuple[int, int]:
    with open(f"inputs/{input_file}") as f:
        adaptors = sorted([int(line.strip()) for line in f.readlines()])

    joltage_jumps = [b - a for a, b in zip(adaptors[:-1], adaptors[1:])]
    joltage_jumps.append(min(adaptors))
    joltage_jumps.append(3)
    return joltage_jumps.count(1), joltage_jumps.count(3)


def task_2(input_file: str) -> int:
    with open(f"inputs/{input_file}") as f:
        adaptors = sorted([int(line.strip()) for line in f.readlines()])
        adaptors.append(adaptors[-1] + 3)
        adaptors.reverse()
        adaptors.append(0)
        adaptors.reverse()

    graph: Dict[int, Any] = {}
    for i, adaptor in enumerate(adaptors):
        graph[adaptor] = []
        try:
            graph[adaptor].append(adaptors[i + 1])
            if adaptors[i + 2] - adaptor <= 3:
                graph[adaptor].append(adaptors[i + 2])
            if adaptors[i + 3] - adaptor <= 3:
                graph[adaptor].append(adaptors[i + 3])
        except IndexError:
            pass

    for node in reversed(graph.keys()):
        if not graph[node]:
            graph[node] = 1
        else:
            graph[node] = sum([graph[next_node] for next_node in graph[node]])

    return graph[0]


if __name__ == "__main__":
    task_1_result = task_1("day_10")
    print(task_1_result[0] * task_1_result[1])
    print(task_2("day_10"))
