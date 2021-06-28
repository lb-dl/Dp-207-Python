from .fibonacci import FibonacciSequence


def test_fibonacci_list():
    f = FibonacciSequence(89, 225)
    assert f.fib_list()
