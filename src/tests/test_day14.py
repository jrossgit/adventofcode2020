from src import day14


def test_computer_initialise():

    computer = day14.Computer()
    assert computer.mask == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    assert computer.memory == dict()


def test_computer_mask_iteration():

    computer = day14.Computer()
    computer.execute("mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
    assert computer.mask == "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"


def test_computer_memory_iteration():

    computer = day14.Computer()
    computer.mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
    computer.execute("mem[3] = 11")
    assert computer.memory == {3: 73}

    computer.execute("mem[3] = 0")
    assert computer.memory == {3: 64}


def test_computer_memory_locator():
    computer = day14.Computer(version=2)
    computer.mask = "000000000000000000000000000000X1001X"
    computer.execute("mem[42] = 100")
    assert sorted(computer.memory.keys()) == [26, 27, 58, 59]
    assert all([v == 100 for v in computer.memory.values()])

    computer.mask = "00000000000000000000000000000000X0XX"
    computer.execute("mem[26] = 1")
    assert sorted(computer.memory.keys()) == [16, 17, 18, 19, 24, 25, 26, 27, 58, 59]


def test_task_1():
    assert day14.task_1("day_14_test") == 101 + 64
