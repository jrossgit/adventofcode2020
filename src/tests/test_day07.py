from src import day07


def test_rule_parser():
    assert day07.parse_rules("day_7_test_mini") == {
        "vibrant plum": [("faded blue", 5), ("dotted black", 6)],
        "shiny gold": [("faded blue", 2)],
        "faded blue": [],
    }


def test_rule_traversal():

    test_data = {
        "vibrant plum": [("faded blue", 5), ("dotted black", 6)],
        "shiny gold": [("faded blue", 2)],
        "faded blue": [],
    }

    assert day07.traverse_backwards(test_data, "faded blue") == ["vibrant plum"]
