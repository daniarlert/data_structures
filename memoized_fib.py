"""
A memoized version of the fibonacci algorithm.

For doctest run:
python -m doctest -v memoized_fib.py

For manual testing:
python memoized_fib.py
"""

"""Dictionary to save previous calculations."""
cache = {}


def memo_fib(nth_number: int) -> int:
    """Memoized version of the fibonacci algorithm.

    : param nth_number: number in the succession to calculate.
    : return: fibonacci number.

    Examples:
    >>> memo_fib(10)
    55
    >>> memo_fib(20)
    6765
    """

    if nth_number in cache:
        return cache[nth_number]

    if nth_number == 1 or nth_number == 2:
        cache[nth_number] = 1
        return 1
    else:
        result = memo_fib(nth_number - 1)
        result += memo_fib(nth_number - 2)

        cache[nth_number] = result
        return result


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    nth_number = input('Enter numbers separated by a comma: ').strip()

    print(f'{memo_fib(int(nth_number)) = }')
