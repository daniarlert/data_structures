"""
An implementation of the Karatsuba algorithm for multiplication.

The Karatsuba algorithm is a fast divide-and-conquer algorithm that
reduces the multiplication of two n-digit numbers to three multiplications
or n/2-digit numbers and, by repeating this process its asymptotically
faster than the traditional algorihtm.

For doctest run:
python -m doctest -v karatsuba_multiplication.py

For manual testing:
python karatsuba_multiplication.py
"""

from math import floor


LOOKUP_TABLE = {}


def __init__():
    for i in range(10):
        for j in range(10):
            LOOKUP_TABLE[(i, j)] = i * j


def pad_zeros(string: str, pad_size: int, side: str = 'left') -> str:
    """Return a string padded with zeros."""
    if side == 'left':
        return '0' * pad_size + string
    elif side == 'right':
        return string + pad_size * '0'


def karatsuba(x: int, y: int) -> int:
    """Multiply two integers using the Karatsuba algorithm.

    :param x: an integer.
    :param y: an integer.
    : return: x * y

    Examples:
    >>> __init__()
    >>> karatsuba(1357, 2468)
    3349076
    >>> karatsuba(4242, 5656) == 4242*5656
    True
    """
    assert isinstance(x, int), 'x must be an integer.'
    assert isinstance(y, int), 'y must be an integer.'

    x = str(x)
    y = str(y)

    if len(x) == 1 and len(y) == 1:
        return LOOKUP_TABLE[(int(x), int(y))]

    if len(x) < len(y):
        x = pad_zeros(x, len(y) - len(x))
    elif len(y) < len(x):
        y = pad_zeros(y, len(x) - len(y))

    mid = floor(len(x)/2)

    a = int(x[:mid])
    b = int(x[mid:])
    c = int(y[:mid])
    d = int(y[mid:])

    first_step = karatsuba(a, c)
    second_step = karatsuba(b, d)
    third_step = karatsuba(int(a + b), int(c + d))

    fourth_step = third_step - second_step - first_step

    first_step_padding = (len(x) - mid) + (len(x) - mid)
    first_step_padded = int(
        pad_zeros(str(first_step), first_step_padding, 'right'))

    fourth_step_padding = len(x) - mid
    fourth_step_padded = int(
        pad_zeros(str(fourth_step), fourth_step_padding, 'right'))

    return first_step_padded + second_step + fourth_step_padded


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    x = input('Enter first number: ').strip()
    y = input('Enter second number: ').strip()
    x = int(x)
    y = int(y)

    __init__()

    print(f'{karatsuba(x, y) = }')
