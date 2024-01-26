from numpy import array
from typing import List


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
