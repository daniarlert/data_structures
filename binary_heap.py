"""
An implementation of the binary heap data structure.

A binary heap is a data structure that takes the form of a binary
tree. This is a common way to implement priority queues.
A binary heap is defined as a binary tree with two additional constraints:
    1. Shaper property: a binary heap is a complete binary tree.
    2. Heap property: the key stored in each node is either greater
    than or equal to or less than or equal to the key in the node's
    children, according to some total order (max-heaps or min-heaps).

For doctest run:
python -m doctest -v binary_heap.py
"""


class BinaryHeap:
    """
    A max-heap implementation in Python
    >>> binary_heap = BinaryHeap()
    >>> binary_heap.insert(6)
    >>> binary_heap.insert(10)
    >>> binary_heap.insert(15)
    >>> binary_heap.insert(12)
    >>> binary_heap.pop()
    15
    >>> binary_heap.pop()
    12
    >>> len(binary_heap)
    2
    """

    def __init__(self) -> None:
        self.__heap = [0]
        self.__size = 0

    def __len__(self) -> None:
        return self.__size

    def __swap_up(self, i: int) -> None:
        """Swap element up."""
        while i//2 > 0:
            if self.__heap[i] > self.__heap[i//2]:
                self.__heap[i], self.__heap[i //
                                            2] = self.__heap[i//2], self.__heap[i]

            i //= 2

    def insert(self, value: int) -> None:
        """Insert new element."""
        self.__heap.append(value)
        self.__size += 1
        self.__swap_up(self.__size)

    def __swap_down(self, i: int) -> None:
        """Swap element down."""
        while self.__size >= 2*i:
            if 2 * i + 1 > self.__size:
                bigger = 2 * 1
            else:
                if self.__heap[2 * 1] > self.__heap[2 * i + 1]:
                    bigger = 2 * i
                else:
                    bigger = 2 * i + 1

            if self.__heap[i] < self.__heap[bigger]:
                self.__heap[i], self.__heap[bigger] = self.__heap[bigger], self.__heap[i]

            i = bigger

    def pop(self) -> None:
        """Pop root element."""
        max_value = self.__heap[1]
        self.__heap[1] = self.__heap[self.__size]

        self.__size -= 1
        self.__heap.pop()
        self.__swap_down(1)

        return max_value
