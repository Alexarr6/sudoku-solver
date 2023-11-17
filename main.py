# import pickle
from typing import List
from numpy import array
import numpy as np

from sudoku_solver.basic_fill_method.possible_solutions_creator import PossibleSolutionsCreator
from sudoku_solver.deep_fill_method.deep_cell_filler import DeepCellFiller
from sudoku_solver.guess_fill_method.solution_roller_back import SolutionRollerBack
from sudoku_solver.situation.situation_computer import SituationComputer
from sudoku_solver.basic_fill_method.basic_cell_filler import BasicCellFiller
from sudoku_solver.guess_fill_method.decision_maker import DecisionMaker
# from sudoku_solver.repositories.sudoku_scrapper import SudokuScrapper
from sudoku_solver.valid_sudoku_checker import ValidSudokuChecker


class SudokuSolver:

    def __init__(self):
        self.backups_boards = []

    def solve(self, board: List[List[str]]) -> List[List[str]]:

        previous_board = [["."]]
        array_board = np.array(board)

        hash_map_situation_cell = SituationComputer.compute_cell_situation()
        hash_map_situation_row, hash_map_situation_column, hash_map_situation_square = \
            SituationComputer.compute_structure_situation()

        while (previous_board != array_board).any():

            array_board = np.array(board)
            previous_board = array_board[:]

            hash_map_row, hash_map_column, hash_map_square = \
                PossibleSolutionsCreator.possible_solutions_creator(array_board)

            board, hash_map_intersection = BasicCellFiller.fill(hash_map_row, hash_map_column, hash_map_square, board)

            array_board = np.array(board)

            if hash_map_intersection == {}:
                return board

            if (previous_board == array_board).all():
                board = DeepCellFiller.fill(
                    hash_map_intersection,
                    hash_map_situation_cell,
                    hash_map_situation_row,
                    hash_map_situation_column,
                    hash_map_situation_square,
                    board
                )

            array_board = np.array(board)

            if (previous_board == array_board).all():
                print("Guessing!")
                board = DecisionMaker.make(hash_map_intersection, board, self.backups_boards)

            if not ValidSudokuChecker.check(board):
                board = SolutionRollerBack.roll_back(self.backups_boards)

            array_board = np.array(board)


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

white = [[".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", ".", "."]]

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

symmetric = [["1", ".", ".", "2", ".", ".", "3", ".", "."],
             ["2", ".", ".", "3", ".", ".", "4", ".", "."],
             ["3", ".", ".", "4", ".", ".", "5", ".", "."],
             ["4", ".", ".", "5", ".", ".", "6", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", "3", ".", ".", "4", ".", ".", "5"],
             [".", ".", "4", ".", ".", "5", ".", ".", "6"],
             [".", ".", "5", ".", ".", "6", ".", ".", "7"],
             [".", ".", "6", ".", ".", "7", ".", ".", "8"]]

url = 'https://www.sudoku.name/index-es.php'

if __name__ == "__main__":
    solution = SudokuSolver().solve(master_1)

    print()
    print("------------------Solution------------------")
    print()
    print(array(solution))

    '''unresolved_boards = []
    resolved_boards = []
    for i in range(10000):

        try:
            url_board = SudokuScrapper.scrap(url)
            unresolved_boards.append(array(url_board))

            solution = SudokuSolver().solve(url_board)
            resolved_boards.append(array(solution))
        except:
            pass

        if i % 20 == 0:
            print("Iter:", i)

        if i % 200 == 0:
            with open('backup_data/unresolved_boards_10000.pkl', 'wb') as file:
                pickle.dump(unresolved_boards, file)

            with open('backup_data/resolved_boards_10000.pkl', 'wb') as file:
                pickle.dump(resolved_boards, file)'''
