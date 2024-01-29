from numpy import array

from solve.board.board import Board
from solve.fillers.cell_filler import CellFiller


class BasicCellFiller(CellFiller):

    def fill(self, board: array, cell_solutions: dict) -> array:

        for row in range(9):
            for column in range(9):
                if Board.is_empty_cell(board, row, column):
                    intersection = cell_solutions[row * 9 + column]
                    if len(intersection) == 1:
                        board = Board.fill_cell(board, row, column, list(intersection)[0])

        return board
