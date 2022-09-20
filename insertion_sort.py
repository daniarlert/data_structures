"""
An implementation of the insertion sort algorithm.

This sorting algorithm sorts a list or collection by sorting
a subset of the list and expanding this sorted range until the
entire list is in order. This is done by comparing adjacent
elements, when it finds that the order is not correct, it moves
the element compared baward until the order is correct.

It has a cost of O(n^2) in the worst case sceneario.

For doctest run:
python -m doctest -v insertion_sort.py

For manual testing:
python insertion_sort.py
"""


def insertion_sort(l: list) -> list:
    """An implementation of the insertion sort algorithm.

    :l list: a list of comparable items.
    :return: the received list in ascending order.

    Examples:
    >>> insertion_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> insertion_sort([]) == sorted([])
    True
    >>> insertion_sort([-2, -5, -45]) == sorted([-2, -5, -45])
    True
    >>> insertion_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> insertion_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> insertion_sort(collection) == sorted(collection)
    True
    """

    numbers_items: int = len(l)
    i: int = 1  # insertion index

    while i < numbers_items:
        tmp = l[i]
        j = i - 1

        while j >= 0 and l[j] > tmp:
            l[j + 1] = l[j]
            j = j - 1

        l[j + 1] = tmp
        i = i + 1

    return l


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_input = input('Enter numbers separated by a comma: ').strip()
    unsorted = [int(item) for item in user_input.split(',')]
    print(f'{insertion_sort(unsorted) = }')
