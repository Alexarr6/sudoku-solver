from dataclasses import dataclass
from datetime import date

Board = list[list[str]]


@dataclass(frozen=True)
class DailySudoku:
    puzzle_date: date
    board: Board
