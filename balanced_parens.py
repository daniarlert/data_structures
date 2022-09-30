"""
A recursive algorithm that generates a list with balanced
parens.

For doctest run:
python -m doctest -v balanced_parens.py

For manual testing:
python balanced_parens.py
"""


def balanced_parens(pairs: int = 0, open_rem=None, close_rem=None, current: str = '') -> list:
    """A recursive algorithm that generates a list with
    balanced parens.

    :param pairs: number of parens to balance.
    :param open_rem: open parens remaining.
    :param close_rem: closing parens remaining.
    :param current: current balanced parens string.
    : return: list with balanced parens.

    Examples:
    >>> balanced_parens(2)
    ['(())', '()()']
    >>> balanced_parens(3)
    ['((()))', '(()())', '(())()', '()(())', '()()()']
    """

    if open_rem is None:
        open_rem = pairs
    if close_rem is None:
        close_rem = pairs

    if open_rem == 0 and close_rem == 0:
        return [current]

    results = []
    if open_rem > 0:
        results.extend(
            balanced_parens(pairs, open_rem - 1, close_rem, current + '('))
    if close_rem > open_rem:
        results.extend(
            balanced_parens(pairs, open_rem, close_rem - 1, current + ')'))

    return results


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    parens = input('Enter number of parens: ').strip()
    print(f'{balanced_parens(int(parens)) = }')
