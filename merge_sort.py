"""
An implementation of the merge-sort algorithm.

This sorting algorihtm i a divide-and-conquer algorithm that 
divides the unsorted list into n sublists, each containing
one element. Then it repeatedly merges the sublists to produce
new sorted sublists until there is only one sublist remaining, which
will be the sorted list.

It has a cost of O(n log n) in the worst case sceneario.

For doctest run:
python -m doctest -v merge_sort.py

For manual testing:
python merge_sort.py
"""


from math import floor


def merge_sort(l: list) -> list:
    """An implementation of the merge-sort algorithm.

    :l list: a list of comparable items.
    :return: the received list in ascending order.

    Examples:
    >>> merge_sort([0, 5, 3, 2, 2])
    [0, 2, 2, 3, 5]
    >>> merge_sort([]) == sorted([])
    True
    >>> merge_sort([-2, -5, -45]) == sorted([-2, -5, -45])
    True
    >>> merge_sort(['d', 'a', 'b', 'e', 'c']) == sorted(['d', 'a', 'b', 'e', 'c'])
    True
    >>> import random
    >>> collection = random.sample(range(-50, 50), 100)
    >>> merge_sort(collection) == sorted(collection)
    True
    >>> import string
    >>> collection = random.choices(string.ascii_letters + string.digits, k=100)
    >>> merge_sort(collection) == sorted(collection)
    True
    """

    if len(l) == 0 or len(l) == 1:
        return l

    mid = floor(len(l)/2)
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])

    sorted = []
    left_index = 0
    right_index = 0

    while len(sorted) < len(l):
        if left[left_index] < right[right_index]:
            sorted.append(left[left_index])
            left_index += 1
        else:
            sorted.append(right[right_index])
            right_index += 1

        if left_index == len(left):
            sorted.extend(right[right_index:])
            break
        elif right_index == len(right):
            sorted.extend(left[left_index:])
            break

    return sorted
