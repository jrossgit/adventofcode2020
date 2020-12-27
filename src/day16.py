from math import prod
import re
from typing import Dict, List, Tuple


def errors_in_ticket(ranges: Dict, ticket: List[int]) -> List[int]:
    errors = []
    for field in ticket:
        found_range = False
        for rng in ranges.values():
            if (rng[0][0] <= field <= rng[0][1]) or (rng[1][0] <= field <= rng[1][1]):
                found_range = True
                break
        if not found_range:
            errors.append(field)
    return errors


def deduce_fields(ranges: Dict, tickets: List):

    field_options = [list(ranges.keys()) for _ in range(len(ranges))]

    field_options = []
    for i in range(len(tickets[0])):
        possible_fields = []
        for field_key, limits in ranges.items():
            field_possible = True
            for ticket in tickets:
                if (limits[0][0] > ticket[i] or limits[0][1] < ticket[i]) and (
                    limits[1][0] > ticket[i] or limits[1][1] < ticket[i]
                ):
                    field_possible = False
            if field_possible:
                possible_fields.append(field_key)
        field_options.append(possible_fields)

    while not all([len(f) == 1 for f in field_options]):
        changes_made = False
        for i, field_option_list in enumerate(field_options):
            if len(field_option_list) == 1:
                for field_options_2 in field_options:
                    if (
                        len(field_options_2) > 1
                        and field_option_list[0] in field_options_2
                    ):
                        field_options_2.remove(field_option_list[0])
                        changes_made = True
        if not changes_made:
            break

    return [f[0] for f in field_options]


def read_puzzle_input(input_file: str):

    with open(f"inputs/{input_file}") as f:

        ranges = {}
        your_ticket: List[int] = []
        other_tickets: List[List[int]] = []

        RANGE_REGEX = re.compile(r"^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+$)")
        TICKET_REGEX = re.compile(r"\d+")

        for line in f.readlines():
            match = RANGE_REGEX.match(line)
            if match:
                field, lower1, upper1, lower2, upper2 = match.groups()
                ranges[field] = [(int(lower1), int(upper1)), (int(lower2), int(upper2))]
            elif TICKET_REGEX.match(line):
                if your_ticket:
                    other_tickets.append([int(field) for field in line.split(",")])
                else:
                    your_ticket = [int(field) for field in line.split(",")]

    return (ranges, your_ticket, other_tickets)


def task_1(input_file: str) -> List[int]:

    ranges, _, other_tickets = read_puzzle_input(input_file)

    errors = []
    for ticket in other_tickets:
        errors.extend(errors_in_ticket(ranges, ticket))

    return errors


def task_2(input_file: str):

    ranges, your_ticket, other_tickets = read_puzzle_input(input_file)

    tickets = []
    for ticket in other_tickets:
        if not errors_in_ticket(ranges, ticket):
            tickets.append(ticket)

    fields = deduce_fields(ranges, tickets)
    departure_values = []
    for field, value in zip(fields, your_ticket):
        if field.startswith("departure"):
            departure_values.append(value)

    assert len(departure_values) == 6
    return prod(departure_values)


if __name__ == "__main__":
    print(sum(task_1("day_16")))
    print(task_2("day_16"))
