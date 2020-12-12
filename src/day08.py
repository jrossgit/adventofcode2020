import copy


class Computer:

    SUCCESS = 0
    INFINITE_LOOP = 1

    def __init__(self, instructions, cursor=0, accumulator=0):
        if not instructions:
            raise ValueError(f"Instructions must be supplied - {instructions} found")

        self.instructions = instructions
        self.cursor = cursor
        self.accumulator = accumulator

        self.executed_instructions = [0 for _ in instructions]

    def run_program(self):
        while True:
            self.executed_instructions[self.cursor] += 1
            self.iterate()
            try:
                if self.executed_instructions[self.cursor]:
                    return self.INFINITE_LOOP
            except IndexError:
                return self.SUCCESS

    def iterate(self):
        instruction, value = (
            self.instructions[self.cursor][:3],
            self.instructions[self.cursor][3:],
        )
        if instruction == "nop":
            self.noop()
        elif instruction == "jmp":
            self.jump(int(value))
        elif instruction == "acc":
            self.accumulate(int(value))

    def jump(self, offset):
        self.cursor += offset

    def noop(self):
        self.cursor += 1

    def accumulate(self, value):
        self.cursor += 1
        self.accumulator += value


def generate_computer(input_file) -> Computer:
    with open(f"inputs/{input_file}") as f:
        instructions = [line.strip() for line in f.readlines()]
    return Computer(instructions)


def run_through_corrupted_instructions(input_file):
    with open(f"inputs/{input_file}") as f:
        instructions = [line.strip() for line in f.readlines()]

    for i in range(len(instructions)):
        if instructions[i].startswith("jmp"):
            new_instructions = copy.copy(instructions)
            new_instructions[i] = new_instructions[i].replace("jmp", "nop")
            computer = Computer(new_instructions)
            if computer.run_program() == Computer.SUCCESS:
                return i, "jmp", computer.accumulator
        elif instructions[i].startswith("nop"):
            new_instructions = copy.copy(instructions)
            new_instructions[i] = new_instructions[i].replace("nop", "jmp")
            computer = Computer(new_instructions)
            if computer.run_program() == Computer.SUCCESS:
                return i, "nop", computer.accumulator
    raise RuntimeError("Not found correct line")


if __name__ == "__main__":
    computer = generate_computer("day_8")
    computer.run_program()
    print(computer.accumulator)

    print(run_through_corrupted_instructions("day_8"))
