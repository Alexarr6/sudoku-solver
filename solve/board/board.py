from numpy import array
from typing import List

from solve.tools.valid_sudoku_checker import ValidSudokuChecker


class Board:

    @staticmethod
    def is_empty_cell(board: array, row: int, col: int) -> bool:

        if array(board)[row, col] == '.':
            return True
        return False

    @staticmethod
    def fill_cell(board: array, row: int, col: int, value: str) -> List[List[int]]:

        board[row, col] = value
        return board

    @staticmethod
    def has_no_solution(board: List[List[str]], backups_boards: List[List[List[str]]]) -> bool:

        if not backups_boards and not ValidSudokuChecker().check(board):
            print("Sudoku without solution!")
            print(board)
            return True
        return False

    @staticmethod
    def is_complete(board: List[List[str]], cell_solutions: dict) -> bool:

        if not cell_solutions and ValidSudokuChecker().check(board):
            return True
        return False
