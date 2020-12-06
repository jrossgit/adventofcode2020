from functools import reduce
import re
from typing import List


def read_input(input_file: str) -> List[List[str]]:
    with open(f"inputs/{input_file}") as f:
        file_body = f.read()

    declarations = []
    for declaration in re.split("\n\n", file_body):
        declarations.append(declaration.split())
    return declarations


def number_of_declared_items(parsed_items: List[List]) -> int:
    return sum([len(set("".join(declaration))) for declaration in parsed_items])


def number_of_all_declared_items(parsed_items: List[List]) -> int:

    return sum(
        [
            len(reduce(lambda x, y: set(x) & set(y), declaration))
            for declaration in parsed_items
        ]
    )


if __name__ == "__main__":
    print(number_of_declared_items(read_input("day_6")))
    print(number_of_all_declared_items(read_input("day_6")))
