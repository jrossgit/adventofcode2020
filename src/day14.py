import itertools
import re
from typing import Dict


class Computer:

    MEM_REGEX = re.compile(r"^mem\[(\d+)\] = (\d+)$")  # e.g. "mem[5] = 10"

    def __init__(self, version: int = 1):
        self.mask = "X" * 32
        self.memory: Dict = dict()
        self.version = version

    def execute(self, instruction: str) -> None:
        if self.version == 1:
            self.execute_v1(instruction)
        elif self.version == 2:
            self.execute_v2(instruction)
        else:
            raise RuntimeError(f"Invalid version {self.version} supplied")

    def execute_v1(self, instruction: str) -> None:

        if instruction.startswith("mask"):
            self.mask = instruction.split()[-1]
        elif instruction.startswith("mem"):
            match = self.MEM_REGEX.match(instruction)
            if match:
                address = int(match.groups()[0])
                value = int(match.groups()[1])

            new_value = 0
            for pos, char in enumerate(self.mask):
                digit = 2 ** (35 - pos)
                if char == "X":
                    new_value += value & digit
                elif char == "1":
                    new_value += digit

            self.memory[address] = new_value

        else:
            raise RuntimeError(f"Couldn't understand instruction {instruction}")

    def execute_v2(self, instruction: str) -> None:

        if instruction.startswith("mask"):
            self.mask = instruction.split()[-1]
        elif instruction.startswith("mem"):
            match = self.MEM_REGEX.match(instruction)
            if match:
                address = int(match.groups()[0])
                value = int(match.groups()[1])

            base_address = 0
            floating_digits = []
            # Perform initial mask application
            for pos, char in enumerate(self.mask):
                digit = 2 ** (35 - pos)
                if char == "0":
                    base_address += address & digit
                elif char == "1":
                    base_address += digit
                else:
                    floating_digits.append(digit)

            # Generate floating values
            for i in range(0, len(floating_digits) + 1):
                for subset in itertools.combinations(floating_digits, i):
                    self.memory[base_address + sum(subset)] = value

        else:
            raise RuntimeError(f"Couldn't understand instruction {instruction}")


def task_1(input_file: str) -> int:
    computer = Computer()
    with open(f"inputs/{input_file}") as f:
        for line in f:
            computer.execute(line)

    return sum(computer.memory.values())


def task_2(input_file: str) -> int:
    computer = Computer(version=2)
    with open(f"inputs/{input_file}") as f:
        for line in f:
            computer.execute(line)

    return sum(computer.memory.values())


if __name__ == "__main__":
    print(task_1("day_14"))
    print(task_2("day_14"))
