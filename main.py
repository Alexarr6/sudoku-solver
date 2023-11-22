from typing import List
from numpy import array
import numpy as np

from deep_fill_method.deep_cell_filler import DeepCellFiller
from guess_fill_method.solution_roller_back import SolutionRollerBack
from basic_fill_method.basic_cell_filler import BasicCellFiller
from guess_fill_method.decision_maker import DecisionMaker
from valid_sudoku_checker import ValidSudokuChecker


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


board_1 = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
           ["6", ".", ".", "1", "9", "5", ".", ".", "."],
           [".", "9", "8", ".", ".", ".", ".", "6", "."],
           ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
           ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
           ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
           [".", "6", ".", ".", ".", ".", "2", "8", "."],
           [".", ".", ".", "4", "1", "9", ".", ".", "5"],
           [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

board_2 = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
           ["7", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", "2", ".", "1", ".", "9", ".", ".", "."],
           [".", ".", "7", ".", ".", ".", "2", "4", "."],
           [".", "6", "4", ".", "1", ".", "5", "9", "."],
           [".", "9", "8", ".", ".", ".", "3", ".", "."],
           [".", ".", ".", "8", ".", "3", ".", "2", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "6"],
           [".", ".", ".", "2", "7", "5", "9", ".", "."]]

board_3 = [["2", "6", ".", ".", "7", ".", ".", ".", "."],
           [".", ".", "9", "6", ".", "2", ".", "1", "."],
           ["4", ".", ".", "3", ".", ".", ".", ".", "."],
           [".", ".", "3", ".", ".", ".", ".", ".", "8"],
           ["8", ".", "7", "9", ".", "4", "5", ".", "2"],
           ["9", ".", ".", ".", ".", ".", "7", ".", "."],
           [".", ".", ".", ".", ".", "7", ".", ".", "5"],
           [".", "4", ".", "2", ".", "6", "1", ".", "."],
           [".", ".", ".", ".", "3", ".", ".", "8", "6"]]

board_4 = [[".", ".", ".", ".", ".", "7", ".", ".", "9"],
           [".", "4", ".", ".", "8", "1", "2", ".", "."],
           [".", ".", ".", "9", ".", ".", ".", "1", "."],
           [".", ".", "5", "3", ".", ".", ".", "7", "2"],
           ["2", "9", "3", ".", ".", ".", ".", "5", "."],
           [".", ".", ".", ".", ".", "5", "3", ".", "."],
           ["8", ".", ".", ".", "2", "3", ".", ".", "."],
           ["7", ".", ".", ".", "5", ".", ".", "4", "."],
           ["5", "3", "1", ".", "7", ".", ".", ".", "."]]

board_5 = [[".", ".", "9", "7", "4", "8", ".", ".", "."],
           ["7", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", "2", ".", "1", ".", "9", ".", ".", "."],
           [".", ".", "7", ".", ".", ".", "2", "4", "."],
           [".", "6", "4", ".", "1", ".", "5", "9", "."],
           [".", "9", "8", ".", ".", ".", "3", ".", "."],
           [".", ".", ".", "8", ".", "3", ".", "2", "."],
           [".", ".", ".", ".", ".", ".", ".", ".", "6"],
           [".", ".", ".", "2", "7", "5", "9", ".", "."]]

board_6 = [[".", ".", ".", "2", ".", ".", ".", "6", "3"],
           ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
           [".", ".", "1", ".", ".", "3", "9", "8", "."],
           [".", ".", ".", ".", ".", ".", ".", "9", "."],
           [".", ".", ".", "5", "3", "8", ".", ".", "."],
           [".", "3", ".", ".", ".", ".", ".", ".", "."],
           [".", "2", "6", "3", ".", ".", "5", ".", "."],
           ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
           ["4", "7", ".", ".", ".", "1", ".", ".", "."]]

everest = [["8", ".", ".", ".", ".", ".", ".", ".", "."],
           [".", ".", "3", "6", ".", ".", ".", ".", "."],
           [".", "7", ".", ".", "9", ".", "2", ".", "."],
           [".", "5", ".", ".", ".", "7", ".", ".", "."],
           [".", ".", ".", ".", "4", "5", "7", ".", "."],
           [".", ".", ".", "1", ".", ".", ".", "3", "."],
           [".", ".", "1", ".", ".", ".", ".", "6", "8"],
           [".", ".", "8", "5", ".", ".", ".", "1", "."],
           [".", "9", ".", ".", ".", ".", "4", ".", "."]]

master_1 = [["8", ".", ".", ".", ".", "7", ".", "9", "."],
            [".", "2", "9", ".", ".", "4", ".", ".", "6"],
            ["3", ".", ".", "2", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "6", "5", ".", "."],
            [".", "1", "7", "4", ".", ".", ".", "3", "."],
            ["2", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "9", "4", "1", ".", ".", ".", "7", "."],
            [".", ".", "8", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "7", ".", ".", ".", "3"]]

master_2 = [["8", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "2", "9", ".", ".", "4", ".", ".", "6"],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", "6", ".", ".", "."],
            [".", "1", ".", "4", ".", ".", ".", "3", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", "9", ".", "1", ".", ".", ".", "7", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]

master_3 = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."]]

symmetric = [["1", ".", ".", "2", ".", ".", "3", ".", "."],
             ["2", ".", ".", "3", ".", ".", "4", ".", "."],
             ["3", ".", ".", "4", ".", ".", "5", ".", "."],
             ["4", ".", ".", "5", ".", ".", "6", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", "3", ".", ".", "4", ".", ".", "5"],
             [".", ".", "4", ".", ".", "5", ".", ".", "6"],
             [".", ".", "5", ".", ".", "6", ".", ".", "7"],
             [".", ".", "6", ".", ".", "7", ".", ".", "8"]]

boards = [board_1, board_2, board_3, board_4, board_5, board_6, master_1, master_2, master_3, everest, symmetric]

if __name__ == "__main__":

    for single_board in boards:
        solution = SudokuSolver().solve(single_board)

        print()
        print("------------------Solution------------------")
        print()
        print(array(solution))
