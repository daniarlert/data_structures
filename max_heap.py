"""
A max-heap implementation.

For manual testing:
python max_heap.py
"""


class MaxBinaryHeap:
    """
    Max-heap implementation.
    """

    heap: list[int] = [0]
    size: int = 0

    def __swap_up(self, i: int) -> None:
        """
        Swap the element i up.
        """

        while i // 2 > 0:
            if self.heap[i] > self.heap[i // 2]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]

            i //= 2

    def __swap_down(self, i: int) -> None:
        """
        Swap the element *i* down.
        """

        while self.size >= 2 * i:
            if 2 * i + 1 > self.size:
                bigger = 2 * i
            else:
                if self.heap[2 * i] > self.heap[2 * i + 1]:
                    bigger = 2 * i
                else:
                    bigger = 2 * i + 1

            if self.heap[i] < self.heap[bigger]:
                self.heap[i], self.heap[bigger] = self.heap[bigger], self.heap[i]

            i = bigger

    def insert(self, value: int) -> None:
        """
        Insert new element.
        """

        self.heap.append(value)
        self.size += 1
        self.__swap_up(self.size)

    def pop(self) -> int:
        """
        Pop the root element.
        """

        max_value = self.heap[1]

        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.__swap_down(1)

        return max_value

    @property
    def get_list(self):
        return self.heap[1:]

    def __len__(self):
        """
        Lenght of the heap.
        """

        return self.size


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    binary_heap = MaxBinaryHeap()

    binary_heap.insert(6)
    binary_heap.insert(10)
    binary_heap.insert(15)
    binary_heap.insert(12)

    print(binary_heap.pop())  # 15
    print(binary_heap.pop())  # 12

    print(binary_heap.get_list)
    print(len(binary_heap))
