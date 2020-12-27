from src import day16


def test_invalid_fields():
    assert day16.task_1("day_16_test") == [4, 55, 12]


def test_field_deduction():
    assert day16.deduce_fields(
        {
            "class": [(0, 1), (4, 19)],
            "row": [(0, 5), (8, 19)],
            "seat": [(0, 13), (16, 19)],
        },
        [[3, 9, 18], [15, 1, 5], [5, 14, 9]],
    ) == ["row", "class", "seat"]
