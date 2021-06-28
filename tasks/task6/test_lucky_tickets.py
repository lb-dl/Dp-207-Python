import pytest

from .lucky_tickets import LuckyTickets, gen_six_digit_tickets


def test_gen_six_digit_tickets():
    expected_len = 999999
    result = len(gen_six_digit_tickets())
    assert expected_len == result


@pytest.fixture
def lucky_tickets():
    tickets = ['000001', '020002', '104003', '203210']
    return LuckyTickets(tickets)


def test_get_moscow_lucky_tickets(lucky_tickets):
    assert lucky_tickets.get_moscow_lucky_tickets()


def test_get_piter_lucky_tickets(lucky_tickets):
    assert lucky_tickets.get_moscow_lucky_tickets()
