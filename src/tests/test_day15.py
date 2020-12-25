from src import day15


def test_task_1():
    assert day15.task1([0, 3, 6], 4) == 0
    assert day15.task1([0, 3, 6, 0], 5) == 3
    assert day15.task1([0, 3, 6, 0, 3], 6) == 3
    assert day15.task1([0, 3, 6, 0, 3, 3], 9) == 4
    assert day15.task1([0, 3, 6], 2020) == 436
