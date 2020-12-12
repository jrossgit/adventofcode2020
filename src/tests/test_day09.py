from src import day09


def test_valid_combination():
    assert day09.valid_combination([35, 20, 15, 25, 47], 62)
    assert day09.valid_combination([35, 20, 15, 25, 47], 35)
    assert not day09.valid_combination([35, 20, 15, 25, 47], 95)
    assert not day09.valid_combination([35, 20, 15, 25, 47], 32)


def test_task_1_with_test_input():
    assert day09.task_01("day_9_test", 5) == 127


def test_task_2_with_test_input():
    assert day09.task_02("day_9_test", 127) == (15, 47)
