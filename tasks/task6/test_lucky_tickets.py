import pytest
import random

from .lucky_tickets import *


def test_get_six_digit_tickets():
    assert gen_six_digit_tickets().__len__() == 999999


def numbers():
    start = random.randint(0, 999990)
    yield from gen_six_digit_tickets()[start:start+2]


@pytest.mark.parametrize("ticket_number", numbers())
def test_num_moscow_lucky_tickets(ticket_number):
    assert LuckyTickets(ticket_number).get_moscow_lucky_tickets


@pytest.mark.parametrize("ticket_number", numbers())
def test_num_piter_lucky_tickets(ticket_number):
    assert LuckyTickets(ticket_number).get_piter_lucky_tickets


@pytest.fixture
def mock_data_file_moskow(tmpdir):
    test_file = tmpdir.mkdir("test_path").join("file.txt")
    test_file.write(MOSKOW)
    return test_file


def test_read_file_moscow(mock_data_file_moskow):
    assert read_file(mock_data_file_moskow) == MOSKOW


@pytest.fixture
def mock_data_file_piter(tmpdir):
    test_file = tmpdir.mkdir("test_path").join("file.txt")
    test_file.write(PITER)
    return test_file


def test_read_file_piter(mock_data_file_piter):
    assert read_file(mock_data_file_piter) == PITER


def test_get_path(mocker):
    mocker.patch('argparse.ArgumentParser.parse_args',
                 return_value=argparse.Namespace(file_path='test_file.txt'))
    res = get_path()
    assert res == 'test_file.txt'
