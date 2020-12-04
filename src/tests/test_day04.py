from src import day04


def test_passport_parsing():
    parsed_passports = day04.parse_file("day_4_test")

    assert len(parsed_passports) == 4
    assert list(sorted(parsed_passports[0].keys())) == [
        "byr",
        "cid",
        "ecl",
        "eyr",
        "hcl",
        "hgt",
        "iyr",
        "pid",
    ]
    assert parsed_passports[0]["hcl"] == "#fffffd"


def test_passport_validity():

    test_passport_1 = {
        "ecl": "gry",
        "pid": "860033327",
        "eyr": "2020",
        "hcl": "#fffffd",
        "byr": "1937",
        "iyr": "2017",
        "cid": "147",
        "hgt": "183cm",
    }
    test_passport_2 = {
        "iyr": "2013",
        "ecl": "amb",
        "cid": "350",
        "eyr": "2023",
        "pid": "028048884",
        "hcl": "#cfa07d",
        "byr": "1929",
    }

    test_passport_3 = {
        "hcl": "#ae17e1",
        "iyr": "2013",
        "eyr": "2024",
        "ecl": "brn",
        "pid": "760753108",
        "byr": "1931",
        "hgt": "179cm",
    }

    test_passport_4 = {
        "hcl": "#cfa07d",
        "eyr": "2025",
        "pid": "166559648",
        "iyr": "2011",
        "ecl": "brn",
        "hgt": "59in",
    }

    assert day04.passport_is_valid(test_passport_1)
    assert not day04.passport_is_valid(test_passport_2)
    assert day04.passport_is_valid(test_passport_3)
    assert not day04.passport_is_valid(test_passport_4)


def test_passport_fields_validity():

    assert day04.year_range_validator(1920, 2002, "2002")
    assert not day04.year_range_validator(1920, 2002, "2003")

    assert day04.height_validator("60in")
    assert day04.height_validator("190cm")
    assert not day04.height_validator("190in")
    assert not day04.height_validator("190")

    assert day04.hex_colour_validator("#123abc")
    assert not day04.hex_colour_validator("#123abz")
    assert not day04.hex_colour_validator("123abc")

    assert day04.eye_colour_validator("brn")
    assert not day04.eye_colour_validator("wat")

    assert day04.passport_id("000000001")
    assert not day04.passport_id("0123456789")


# def test_2020_sum_with_3_numbers():
#     assert day01.puzzle_02("day_1_test") == (366, 675, 979, 241861950)
