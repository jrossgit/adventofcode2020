from src import day03

def test_2020_toboggan_runs():
    assert day03.toboggan_trees("day_3_test", 3, 1) == 7
    assert day03.toboggan_trees("day_3_test", 1, 1) == 2
    assert day03.toboggan_trees("day_3_test", 2, 2) == 1
