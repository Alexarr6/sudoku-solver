from numpy import array
from typing import Tuple
from math import floor

from sudoku_solver.basic_fill_method.possible_solutions_creator import PossibleSolutionsCreator


class BasicCellFiller:

    @staticmethod
    def fill(board: array) -> Tuple[array, dict]:

        hash_map_intersection = {}

        hash_map_row, hash_map_column, hash_map_square = \
            PossibleSolutionsCreator.possible_solutions_creator(board)

        for i in range(9):
            possible_solutions_row = hash_map_row[i]
            for j in range(9):
                if board[i, j] == ".":
                    possible_solutions_column = hash_map_column[j]
                    possible_solutions_square = hash_map_square[3 * floor(i / 3) + floor(j / 3)]

                    intersection = possible_solutions_row & possible_solutions_column & possible_solutions_square
                    hash_map_intersection[i * 9 + j] = intersection

                    if len(intersection) == 1:
                        board[i, j] = list(intersection)[0]

        return board, hash_map_intersection
