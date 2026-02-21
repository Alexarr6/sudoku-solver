from copy import deepcopy

from solve.main.main import SudokuSolver
from sudoku_daily_bot.core.models import Board


class ExistingSolverAdapter:
    def __init__(self) -> None:
        self._solver = SudokuSolver()

    def solve(self, board: Board) -> Board:
        solution = self._solver.solve(deepcopy(board))
        if solution is None:
            raise ValueError("Sudoku solver could not find a valid solution")
        return [[str(cell) for cell in row] for row in solution.tolist()]
