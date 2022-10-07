from typing import List, Generic
from utils import T


class Stack(Generic[T]):
    def __init__(self) -> None:
        super().__init__()
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

    def __str__(self) -> str:
        return str(self._container)
