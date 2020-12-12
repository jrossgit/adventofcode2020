from copy import copy
import re
from typing import Dict, List


def parse_rules(input_file: str) -> Dict:

    with open(f"inputs/{input_file}") as f:
        BAG_SPLIT_REGEX = re.compile("(\d+) ([a-z]+ [a-z]+)")
        LINE_SPLIT_REGEX = re.compile("^(.*) bags? contains? (.*)\.$")

        rules: Dict = {}
        for line in f.readlines():
            match = LINE_SPLIT_REGEX.match(line.strip())
            if match:
                node_bag, contains = match.groups()
            if contains == "no other bags":
                rules[node_bag] = []
            else:
                rules[node_bag] = []
                for s in contains.split(","):
                    groups = BAG_SPLIT_REGEX.findall(s)[0]
                    rules[node_bag].append((groups[1], int(groups[0])))
    return rules


def traverse_backwards(bags: Dict, starting_bag: str) -> int:
    bags_to_check = [starting_bag]
    bags.pop(starting_bag)
    visited_bags = [starting_bag]

    found_bags = True
    while found_bags:
        found_bags = False
        next_loop = copy(bags_to_check)
        bags_to_check = []
        for current_bag in next_loop:
            for node_bag, edge_bags in bags.items():
                if (
                    current_bag in [bag[0] for bag in edge_bags]
                    and node_bag not in visited_bags
                ):
                    bags_to_check.append(node_bag)
                    visited_bags.append(node_bag)
                    found_bags = True

        for bag in bags_to_check:
            bags.pop(bag)
    return len(visited_bags) - 1


def bags_contained(bags: Dict, starting_bag, indent=0) -> int:

    if not bags[starting_bag]:
        return 0

    total_bags = 0
    for bag in bags[starting_bag]:
        total_bags += (bags_contained(bags, bag[0], indent + 1) + 1) * bag[1]
    print(f"{' ' * indent}{starting_bag} contains {total_bags} bags")
    return total_bags


if __name__ == "__main__":

    data = parse_rules("day_7")
    # print(traverse_backwards(data, "shiny gold"))
    print(bags_contained(data, "shiny gold"))
