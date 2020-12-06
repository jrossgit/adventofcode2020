from src import day06


def test_file_is_parsed_correctly():
    assert day06.read_input("day_6_test") == [
        ["abc"],
        ["a", "b", "c"],
        ["ab", "ac"],
        ["a", "a", "a", "a"],
        ["b"],
    ]


def test_test_input_has_correct_number_answers():
    assert (
        day06.number_of_declared_items(
            [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
        )
        == 11
    )


def test_test_input_has_correct_number_answers_2():
    assert (
        day06.number_of_all_declared_items(
            [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]
        )
        == 6
    )
