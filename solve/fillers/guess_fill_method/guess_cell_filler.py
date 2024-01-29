from numpy import array
from math import floor

from solve.board.board import Board
from solve.fillers.cell_filler import CellFiller
from solve.fillers.guess_fill_method.solution_roller_back import SolutionRollerBack


class GuessCellFiller(CellFiller):

    def __init__(self, backups_boards: list):
        self.backups_boards = backups_boards

    def fill(self, board: array, cell_solutions: dict) -> array:

        min_len = 10
        min_key, min_values = 0, 0

        for key, value in cell_solutions.items():
            if len(value) == 2:
                min_key, min_values = key, value
                break

            if len(value) < min_len:
                min_len = len(value)
                min_key, min_values = key, value

        if min_values == 0 or min_values == set():
            board = SolutionRollerBack.roll_back(self.backups_boards)
        else:
            current_guess = min_values.pop()
            self.backups_boards.append([min_key, min_values, array(board)])
            board = Board.fill_cell(board, floor(min_key / 9), min_key % 9, current_guess)

        return board
