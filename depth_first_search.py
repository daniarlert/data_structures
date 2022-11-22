"""
A non-recursie implementation of the depth-first search algorithm.

Depth-first search is an algorithm for traversing or searching tree
or graph data structures. The algorithm starts at the root node and
explores as far as possible along each branch before backtracking.
A Stack is needed to keep track of the nodes discovered so far along
a specified branch which helps in backtracking of the graph.

For doctest run:
python -m doctest -v depth_first_search.py

For manual testing:
python depth_first_search.py
"""

# Graph represented with an adjacency list.
G = {
    "A": ["B", "C", "D"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "D"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
}


def depth_first_search(graph: dict[str, list[str]], start: str) -> set[str]:
    """
    Depth-first Search implementation on a graph.

    :param graph: directed graph as an adjacency list.
    :param start: starting vertex.
    :returns: trace of the search

    >>> input_G = { "A": ["B", "C", "D"], "B": ["A", "D", "E"],
    ... "C": ["A", "F"], "D": ["B", "D"], "E": ["B", "F"],
    ... "F": ["C", "E", "G"], "G": ["F"] }
    >>> output_G = list({'A', 'B', 'C', 'D', 'E', 'F', 'G'})
    >>> all(x in output_G for x in list(depth_first_search(input_G, "A")))
    True
    >>> all(x in output_G for x in list(depth_first_search(input_G, "G")))
    True
    """
    visited, stack = set(start), [start]

    while stack:
        current = stack.pop()
        visited.add(current)

        for adj in reversed(graph[current]):
            if adj not in visited:
                stack.append(adj)

    return visited


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(depth_first_search(G, "A"))
