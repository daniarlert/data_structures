"""
A recursive reverse string algorithm.

For doctest run:
python -m doctest -v recursive_reverse_str.py

For manual testing:
python recursive_reverse_str.py
"""


def recursive_reverse_str(text: str) -> str:
    """A recursive reverse string algorithm

    : param text: string to reverse
    : return: reversed string

    Examples:
    >>> recursive_reverse_str('hola')
    'aloh'
    >>> recursive_reverse_str('')
    ''
    >>> recursive_reverse_str('Hello, World!')
    '!dlroW ,olleH'
    """

    if len(text) == 0 or len(text) == 1:
        return text
    else:
        head = text[0]
        tail = text[1:]

        return recursive_reverse_str(tail) + head


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    text = input('Write anything you want: ').strip()

    print(f'{recursive_reverse_str(text) = }')
