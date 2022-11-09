"""
A complete solution for the fractional knapsack problem using
a greedy algorithm.

For doctest run:
python -m doctest -v greedy_fractional_knapsack.py
"""

from typing import List


def fractional_knapsack(
    values: List[int], weights: list[int], cap: int
) -> tuple[float, List[float]]:
    """
    >>> values = [1, 3, 5, 7, 9]
    >>> weights = [0.9, 0.7, 0.5, 0.3, 0.1]
    >>> fractional_knapsack(values, weights, 5)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(values, weights, 15)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(values, weights, 25)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(values, weights, 26)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack(values, weights, -1)
    (-90.0, [0, 0, 0, 0, -10.0])
    >>> fractional_knapsack([1, 3, 5, 7], weights, 30)
    (16, [1, 1, 1, 1])
    >>> fractional_knapsack(values, [0.9, 0.7, 0.5, 0.3, 0.1], 30)
    (25, [1, 1, 1, 1, 1])
    >>> fractional_knapsack([], [], 30)
    (0, [])
    """
    indexes: List[int] = list(range(len(values)))
    ratios: List[float] = [v / w for v, w in zip(values, weights)]
    indexes.sort(key=lambda i: ratios[i], reverse=True)

    max_value: float = 0
    fractions: list[float] = [0] * len(values)

    for i in indexes:
        if weights[i] <= cap:
            fractions[i] = 1
            max_value += values[i]
            cap -= weights[i]
        else:
            fractions[i] = cap / weights[i]
            max_value += values[i] * cap / weights[i]
            break

    return max_value, fractions


if __name__ == "__main__":
    import doctest

    doctest.testmod()
