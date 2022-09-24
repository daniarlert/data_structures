"""
A Trie or Prefix Tree is a type of k-ary search tree which is used
to locate specific keys from withing a set. These keys normally
are just strings.

A Trie is in reality not a very practical data structure unless
memory is not a problem.
"""


class Node:
    """Trie node."""

    def __init__(self):
        self.children = dict()
        self.is_leaf = False


class Trie:
    """A Trie data structure."""

    def __init__(self) -> None:
        """Initializes the root of the Trie."""

        self.root = Node()

    def insert(self, word: str) -> None:
        """Inserts a word into the Trie.

        :param word: word to be inserted.
        :return: None
        """
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = Node()

            current = current.children[ch]

        current.is_leaf = True

    def insert_many(self, words: list[str]) -> None:
        """Insert a list of words into a Trie.

        :param words: a list of words.
        :return: None
        """
        for word in words:
            self.insert(word)

    def search(self, word: str) -> bool:
        """Check if a word is in the Trie or not.

        :param word: word to search for.
        :return: True if the word is found. False if not.
        """
        current = self.root

        for ch in word:
            if ch not in current.children:
                return False

            current = current.children[ch]

        return current.is_leaf

    def starts_with(self, prefix: str) -> bool:
        """Check if a prefix is in the Trie or not.

        :param prefix: prefix to search for.
        :return: True if the prefix is found. False if not.
        """

        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return False

            current = current.children[ch]

        return True

    def print(self, node: Node, word: str = '') -> None:
        """Prints all the words in the Trie."""
        if node.is_leaf:
            print(word, end=' ')

        for k, val in node.children.items():
            print(val, word + k)


def test_trie() -> bool:
    """Assertions to check the Trie's functionality."""

    words = "banana bananas bandana band apple all beast".split()
    trie = Trie()
    trie.insert_many(words)

    assert all(trie.search(word) for word in words)
    assert trie.search("banana")
    assert not trie.search("bandanas")
    assert not trie.search("apps")
    assert trie.search("apple")
    assert trie.search("all")
    assert trie.search("bananas")

    return True


if __name__ == "__main__":
    test_trie()
