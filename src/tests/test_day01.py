from src import day01

def test_2020_sum_with_2_numbers():
    assert day01.puzzle_01("day_1_test") == (299, 1721, 514579)

def test_2020_sum_with_3_numbers():
    assert day01.puzzle_02("day_1_test") == (366, 675, 979, 241861950)
