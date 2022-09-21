"""
An implementation of the binary search algorithm.

The binary search algorithm compares the target value to the
middle element of the list. If they are not equal, the half
in which the target cannot lie is eliminated and the search
continues on the remaining hald, again taking the middle element
to compare to the target value and repeating until the target is
found or is clear that the target is not in the list.

It has a cost of O(log n), where n is the number of elements.

For doctest run:
python -m doctest -v binary_search.py

For manual testing:
python binary_search.py
"""


from math import floor


def binary_search(l: list[int], target: int) -> int:
    """An implementation of the binary search algorithm.

    The list must be ascending sorted, otherwise the results
    will be unpredictable.

    : param l: an ascending sorted collection.
    : param target: target value to search for.
    : return: index of the target item or -1 if not found.

    Examples:
    >>> binary_search([0, 5, 7, 10, 15], 0)
    0
    >>> binary_search([0, 5, 7, 10, 15], 15)
    4
    >>> binary_search([0, 5, 7, 10, 15], 5)
    1
    >>> binary_search([0, 5, 7, 10, 15], 6)
    -1
    """

    high = len(l) - 1
    low = 0

    while low <= high:
        mid = floor((high+low)/2)

        if l[mid] == target:
            return mid
        elif l[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    user_list = input('Enter numbers separated by a comma: ').strip()
    target = input('Enter the target number: ').strip()

    sorted = [int(item) for item in user_list.split(',')]
    print(f'{binary_search(sorted, int(target)) = }')
