from numpy import array

from solve.board.board import Board
from solve.fillers.cell_filler import CellFiller


class BasicCellFiller(CellFiller):

    def fill(self, board: array, cell_solutions: dict) -> array:

        for i in range(9):
            for j in range(9):
                if Board.is_empty_cell(board, i, j):
                    intersection = cell_solutions[i * 9 + j]
                    if len(intersection) == 1:
                        board = Board.fill_cell(board, i, j, list(intersection)[0])

        return board
