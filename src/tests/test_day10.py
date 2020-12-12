from src import day10


def test_task_1_with_test_input():
    assert day10.task_1("day_10_test") == (7, 5)
    assert day10.task_1("day_10_test2") == (22, 10)


def test_task_2_with_test_input():
    assert day10.task_2("day_10_test") == 8
    assert day10.task_2("day_10_test2") == 19208
