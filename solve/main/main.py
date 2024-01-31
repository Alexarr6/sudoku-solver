from typing import List, Optional
from numpy import array
import numpy as np

from solve.board.board import Board
from solve.fillers.deep_fill_method.deep_cell_filler import DeepCellFiller
from solve.fillers.basic_fill_method.basic_cell_filler import BasicCellFiller
from solve.fillers.guess_fill_method.guess_cell_filler import GuessCellFiller
from solve.repositories.example_boards import boards
from solve.tools.cell_solution_computer import CellSolutionComputer


class SudokuSolver:

    def __init__(self):
        self.backups_boards = []

    def solve(self, board: List[List[str]]) -> Optional[List[List[str]]]:

        board = np.array(board)
        deep_cell_filler = DeepCellFiller()
        cell_solutions = CellSolutionComputer.compute(board)

        while not Board.find_solution(board, cell_solutions):

            previous_board = board.copy()

            if Board.has_no_solution(board, self.backups_boards):
                return None

            board = BasicCellFiller().fill(board, cell_solutions)

            if (previous_board == board).all():
                board = deep_cell_filler.fill(board, cell_solutions)

            if (previous_board == board).all():
                board = GuessCellFiller(self.backups_boards).fill(board, cell_solutions)

            cell_solutions = CellSolutionComputer.compute(board)

        return board


if __name__ == "__main__":

    for single_board in boards:
        solution = SudokuSolver().solve(single_board)

        print()
        print("------------------Solution------------------")
        print()
        print(array(solution))
