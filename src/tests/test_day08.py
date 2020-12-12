from unittest import mock
from src.day08 import Computer, generate_computer, run_through_corrupted_instructions

import pytest


@pytest.fixture
def computer():
    return Computer(["nop +0", "jump -1", "acc +2"], accumulator=0, cursor=0)


def test_computer_jump(computer):

    computer.jump(2)
    assert computer.cursor == 2
    assert computer.accumulator == 0

    computer.jump(-2)
    assert computer.cursor == 0
    assert computer.accumulator == 0


def test_computer_noop(computer):

    computer.noop()
    assert computer.cursor == 1
    assert computer.accumulator == 0


def test_computer_accumulate(computer):

    computer.accumulate(2)
    assert computer.cursor == 1
    assert computer.accumulator == 2


def test_computer_iterates(computer):

    computer.jump = mock.MagicMock()
    computer.accumulate = mock.MagicMock()
    computer.noop = mock.MagicMock()

    computer.iterate()
    assert computer.noop.called_once()

    computer.cursor = 1
    assert computer.jump.called_once_with(1)

    computer.cursor = 2
    assert computer.accumulate.called_once_with(2)


def test_with_test_input():
    computer = generate_computer("day_8_test")
    computer.run_program()
    assert computer.cursor == 1
    assert computer.accumulator == 5


def test_run_corrupted_input():
    assert run_through_corrupted_instructions("day_8_test") == (7, "jmp", 8)
