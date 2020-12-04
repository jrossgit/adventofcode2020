from functools import partial
import re
from typing import Dict, List

def parse_file(input_file: str) -> List[Dict]:
    """
    Parses the file of passports

    :param input_file: Name of file containing data

    :returns: Parsed and formatted data
    """
    with open(f"inputs/{input_file}") as f:
        file_body = f.read()

    passports = []
    for passport in re.split("\n\n", file_body):
        passports.append({field[:3]: field[4:] for field in passport.split()})

    return passports


def year_range_validator(start_year: int, end_year: int, value: str) -> bool:
    try:
        return start_year <= int(value) <= end_year
    except ValueError:
        return False


def height_validator(value: str) -> bool:

    try:
        if value[-2:] == "in":
            return 59 <= int(value[:-2]) <= 76
        elif value[-2:] == "cm":
            return 150 <= int(value[:-2]) <= 193
        else:
            return False
    except (ValueError, IndexError):
        return False


def hex_colour_validator(value: str) -> bool:
    return bool(re.match(r"^#[0-9a-f]{6}$", value))


def eye_colour_validator(value: str) -> bool:
    return value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def passport_id(value: str) -> bool:
    return bool(re.match(r"^\d{9}$", value))


def passport_is_valid(passport: Dict, validate: bool = False) -> bool:
    """
    Checks the validity of the given passport

    :param passport: Data contained within the passport
    :param validate: Check the validity of individual fields

    :returns: boolean indicating the validity of the given passport
    """
    required_validators = {
        "byr": partial(year_range_validator, 1920, 2002),
        "ecl": eye_colour_validator,
        "eyr": partial(year_range_validator, 2020, 2030),
        "hcl": hex_colour_validator,
        "hgt": height_validator,
        "iyr": partial(year_range_validator, 2010, 2020),
        "pid": passport_id,
    }

    for field, validator in required_validators.items():
        if field not in passport:
            return False
        if validate and not validator(passport[field]):
            return False

    return True


def challenge_01(input_file: str) -> int:

    return sum(
        [passport_is_valid(passport) for passport in parse_file(input_file)]
    )


def challenge_02(input_file: str) -> int:

    return sum(
        [passport_is_valid(passport, validate=True)
            for passport in parse_file(input_file)]
    )



if __name__ == "__main__":
    print(challenge_01("day_4"))
    print(challenge_02("day_4"))
