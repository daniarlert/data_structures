"""
An implementation of the quicksort sorting algorithm.

This sorting algorithm sorts a list or collection by selecting a
'pivot' from the list and partitioning the other elements into two
sub-lists according to wheter they're less than or greater than
the pivot. The sub-lists are then sorted recursively.

It has a cost of O(n^2) in the worst case sceneario.

For doctest run:
python -m doctest -v quicksort.py

For manual testing:
python quicksort.py
"""


def quicksort(l: list, left: int = None, right: int = None) -> None:
    """An implementation of the quicksort sorting algorithm.

    :l list: a list of comparable items.

    Examples:
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> quicksort(collection)
    >>> collection == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> quicksort(collection)
    >>> collection == sorted(collection)
    True
    """
    if left is None:
        left = 0
    if right is None:
        right = len(l) - 1

    if right <= left:
        return

    i = left
    pivot = l[right]

    for j in range(left, right):
        if l[j] <= pivot:
            l[i], l[j] = l[j], l[i]
            i += 1

    l[i], l[right] = l[right], l[i]

    quicksort(l, left, i - 1)
    quicksort(l, i + 1, right)


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_input = input('Enter numbers separated by a comma: ').strip()
    unsorted = [int(item) for item in user_input.split(',')]

    quicksort(unsorted)
    print(f'{unsorted}')
