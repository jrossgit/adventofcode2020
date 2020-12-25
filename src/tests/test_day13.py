from src import day13


def test_buses_task_01():
    assert day13.task_1("day_13_test") == 944


def test_buses_task_2():
    assert day13.earliest_bus_sequence([17, None, 13, 19]) == 3417
    assert day13.earliest_bus_sequence([67, 7, 59, 61]) == 754018
    assert day13.earliest_bus_sequence([67, None, 7, 59, 61]) == 779210
    assert day13.earliest_bus_sequence([67, 7, None, 59, 61]) == 1261476
    assert day13.earliest_bus_sequence([1789, 37, 47, 1889]) == 1202161486
