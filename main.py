from typing import List
from numpy import array
import numpy as np

from deep_fill_method.deep_cell_filler import DeepCellFiller
from guess_fill_method.solution_roller_back import SolutionRollerBack
from basic_fill_method.basic_cell_filler import BasicCellFiller
from guess_fill_method.decision_maker import DecisionMaker
from valid_sudoku_checker import ValidSudokuChecker
from example_boards import boards


class SudokuSolver:

    def __init__(self):
        self.backups_boards = []

    def solve(self, board: List[List[str]]) -> List[List[str]]:

        board = np.array(board)

        while True:

            previous_board = board.copy()
            board, hash_map_intersection = BasicCellFiller.fill(board)

            if hash_map_intersection == {} and ValidSudokuChecker().check(board):
                return board

            if (previous_board == board).all():
                board = DeepCellFiller.fill(hash_map_intersection, board)

            if (previous_board == board).all():
                board = DecisionMaker.make(hash_map_intersection, board, self.backups_boards)

            if not ValidSudokuChecker().check(board):
                board = SolutionRollerBack.roll_back(self.backups_boards)


if __name__ == "__main__":

    for single_board in boards:
        solution = SudokuSolver().solve(single_board)

        print()
        print("------------------Solution------------------")
        print()
        print(array(solution))
