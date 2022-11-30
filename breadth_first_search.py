"""
An implementation of the Breadth-first Search algorithm.

BFS is an algorithm for searching a tree data structure for a node
that satisfies a given property. It starts at the tree root and explores
all nodes at the present depth prior to moving on to the nodes at the
next depth level. Usually a queue is needed to keep track of the child
nodes that were encountered but not explored yet.

For doctest run:
python -m doctest -v depth_first_search.py

For manual testing:
python depth_first_search.py
"""

from typing import Union

# Graph represented with an adjacency list.
G = {
    "A": ["B", "C", "E"],
    "B": ["A", "D", "E"],
    "C": ["A", "F", "G"],
    "D": ["B"],
    "E": ["A", "B", "D"],
    "F": ["C"],
    "G": ["C"],
}


def breadth_first_search(
    graph: dict[str, list[str]], start: str
) -> dict[str, Union[str, None]]:
    """
    Breadth-first Search implementation on a graph.

    :param graph: directed graph as an adjacency list.
    :param start: starting vertext.
    :returns: trace of the search.

    >>> breadth_first_search(G, 'G')
    {'G': None, 'C': 'G', 'A': 'C', 'F': 'C', 'B': 'A', 'E': 'A', 'D': 'B'}
    """
    parent: dict[str, Union[str, None]] = {}
    parent[start] = None

    visited: set[str] = {start}
    queue: list[str] = [start]

    while queue:
        vertex = queue.pop(0)

        for adjacent in graph[vertex]:
            if adjacent not in visited:
                visited.add(adjacent)
                parent[adjacent] = vertex
                queue.append(adjacent)

    return parent


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(breadth_first_search(G, "A"))
