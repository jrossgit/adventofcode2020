from src import day05

def test_that_airport_code_returns_correct_ids():

    assert day05.get_seat_id("BFFFBBFRRR") == 567
    assert day05.get_seat_id("FFFBBBFRRR") == 119
    assert day05.get_seat_id("BBFFBBFRLL") == 820


def test_that_max_id_is_returned():

    assert day05.max_boarding_pass("day_5_test") == 820