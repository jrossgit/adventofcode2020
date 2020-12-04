import logging
import re


def validate_password_file(input_file: str) -> int:
    """
    Takes a list of password rules and passwords in the format, one per line:
    "1-3 e: abcse"
    The above line should be read as "The letter 'e' should be found between
    one and three times in the password 'abcse', therefore the given password
    is valid"

    :param input_file: Name of file containing data

    :returns: int - Number of valid passwords found
    """
    PASSWORD_VALIDATE_RE = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+$)")

    correct_passwords = 0
    with open(f"inputs/{input_file}") as f:
        for line in f.readlines():
            lower, upper, char, password = PASSWORD_VALIDATE_RE.match(line).groups()

            if int(lower) <= password.count(char) <= int(upper):
                correct_passwords += 1

    return correct_passwords


def validate_password_file_positional(input_file: str) -> int:
    """
    Takes a list of password rules and passwords in the format, one per line:
    "1-3 e: abcse"
    The above line should be read as "The letter 'e' should be found in exactly
    one of positions 1 and 3 (one-indexed). Therefore the above password
    is invalid"

    :param input_file: Name of file containing data

    :returns: int - number of correct passwords
    """
    PASSWORD_VALIDATE_RE = re.compile(r"(\d+)-(\d+) ([a-z]): ([a-z]+$)")

    correct_passwords = 0
    with open(f"inputs/{input_file}") as f:
        for line in f.readlines():
            first, last, char, password = PASSWORD_VALIDATE_RE.match(line).groups()

            if bool(password[int(first) - 1] == char) ^ bool(
                password[int(last) - 1] == char
            ):
                correct_passwords += 1

    return correct_passwords


if __name__ == "__main__":
    print(validate_password_file_positional("day_2"))
