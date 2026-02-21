from abc import ABC, abstractmethod

from sudoku_daily_bot.core.models import Board, DailySudoku


class DailySudokuProvider(ABC):
    @abstractmethod
    def fetch_daily_sudoku(self) -> DailySudoku:
        raise NotImplementedError


class SudokuSolverPort(ABC):
    @abstractmethod
    def solve(self, board: Board) -> Board:
        raise NotImplementedError


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        raise NotImplementedError
