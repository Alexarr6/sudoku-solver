from typing import List
from numpy import array
import numpy as np

from solve.fillers.deep_fill_method.deep_cell_filler import DeepCellFiller
from solve.fillers.basic_fill_method.basic_cell_filler import BasicCellFiller
from solve.fillers.guess_fill_method.guess_cell_filler import GuessCellFiller
from solve.tools.valid_sudoku_checker import ValidSudokuChecker
from solve.repositories.example_boards import boards
from solve.tools.cell_solution_computer import CellSolutionComputer


class SudokuSolver:

    def __init__(self):
        self.backups_boards = []

    def solve(self, board: List[List[str]]) -> List[List[str]]:

        board = np.array(board)
        deep_cell_filler = DeepCellFiller()

        while True:

            previous_board = board.copy()
            cell_solutions = CellSolutionComputer.compute(board)

            board = BasicCellFiller().fill(board, cell_solutions)

            if cell_solutions == {} and ValidSudokuChecker().check(board):
                return board

            if (previous_board == board).all():
                board = deep_cell_filler.fill(board, cell_solutions)

            if (previous_board == board).all():
                board = GuessCellFiller(self.backups_boards).fill(board, cell_solutions)


if __name__ == "__main__":

    for single_board in boards:
        solution = SudokuSolver().solve(single_board)

        print()
        print("------------------Solution------------------")
        print()
        print(array(solution))
