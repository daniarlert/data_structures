from enum import Enum
from typing import List, NamedTuple
import random
from utils import T


class Cell(str, Enum):
    EMPTY = ' '
    BLOCKED = '#'
    START = 'S'
    GOAL = 'G'
    PATH = '·'


class MazeLocation(NamedTuple):
    row: int
    column: int


class Maze:
    def __init__(self, rows: int = 20, columns: int = 20, sparseness: float = 0.2, start: MazeLocation = MazeLocation(0, 0), goal: MazeLocation = MazeLocation(19, 19)) -> None:
        # initialize basic instance variables.
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal

        # fill the grid with empty cells.
        self._grid: List[List[Cell]] = [
            [Cell.EMPTY for c in range(columns)] for r in range(rows)]

        # fill the start and goal locations.
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows: int, columns: int, sparseness: float) -> None:
        for r in range(rows):
            for c in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[r][c] = Cell.BLOCKED

    def neighbors(self, ml: MazeLocation) -> bool:
        locations: List[MazeLocation] = []

        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))

        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))

        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))

        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column * 1))

        return locations

    def get_location(self, ml: MazeLocation) -> Cell:
        return self._grid[ml.row][ml.column]

    def is_goal(self, ml: MazeLocation) -> bool:
        return self._grid[ml.row][ml.column] == self.goal

    def __str__(self) -> str:
        output: str = ''
        for r in self._grid:
            output += ''.join([c.value for c in r]) + '\n'

        return output
