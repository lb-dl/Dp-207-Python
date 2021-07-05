import pytest
import random

from ..task6.lucky_tickets import *


def test_get_six_digit_tickets():
    assert len(gen_six_digit_tickets()) == 999999


@pytest.fixture
def lucky_tickets():
    tickets = ['000001', '020002', '104003', '203210']
    return LuckyTickets(tickets)


def test_num_moscow_lucky_tickets(lucky_tickets):
    assert LuckyTickets.get_moscow_lucky_tickets(lucky_tickets) == 1


def test_num_piter_lucky_tickets(lucky_tickets):
    assert LuckyTickets.get_piter_lucky_tickets(lucky_tickets) == 2


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
