from src.fibonacci import generateFibonacci


def test_fibonacci():
    assert generateFibonacci(1) == [1]


def test_fibonacci_2():
    assert [1, 1, 2, 3, 5, 8, 13, 21] == generateFibonacci(8)


def test_fibonacci_length():
    assert len(generateFibonacci(2)) == 2


def test_fibonacci_negative_number():
    assert generateFibonacci(-12) == []
