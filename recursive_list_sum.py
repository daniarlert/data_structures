"""
A recursive sum for lists.

For doctest run:
python -m doctest -v recursive_list_sum.py

For manual testing:
python recursive_list_sum.py
"""


def recursive_list_sum(l: list) -> int:
    """A recursive sum for lists.

    : param l: a list of numbers
    : return: sum of all elements on l

    Examples:
    >>> recursive_list_sum([4, 4])
    8
    >>> recursive_list_sum([0, 5, 7, 10, 15])
    37
    >>> recursive_list_sum([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    45
    """

    if len(l) == 0:
        return 0
    elif len(l) == 1:
        return l[0]
    else:
        mid = len(l)//2
        left = recursive_list_sum(l[0:mid])
        right = recursive_list_sum(l[mid:len(l) + 1])

        return left + right


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_list = input('Enter numbers separated by a comma: ').strip()
    l = [int(item) for item in user_list.split(',')]

    print(f'{recursive_list_sum(l) = }')
