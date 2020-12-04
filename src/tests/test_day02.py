from src import day02


def test_2020_password_rule_validation_letter_count():
    assert day02.validate_password_file("day_2_test") == 2


def test_2020_password_rule_validation_positions():
    assert day02.validate_password_file_positional("day_2_test") == 1
