from typing import List, Dict
from numpy import array
from sudoku_solver.basic_fill_method.checkers.possible_values_checker import PossibleValuesChecker


class PossibleSolutionsCreator:

    @staticmethod
    def possible_solutions_creator(array_board: array) -> List[Dict[int, set]]:

        hash_map_row = {}
        hash_map_column = {}
        hash_map_square = {}

        for i in range(9):
            row = array_board[i, :]
            possible_solutions_row = PossibleValuesChecker.check_column_row(row)
            hash_map_row[i] = possible_solutions_row

        for j in range(9):
            column = array_board[:, j]
            possible_solutions_column = PossibleValuesChecker.check_column_row(column)
            hash_map_column[j] = possible_solutions_column

        for i in range(3):
            for j in range(3):
                nine_square_cells = array_board[i * 3: (i + 1) * 3, j * 3: (j + 1) * 3]
                possible_solutions_square = PossibleValuesChecker.check_square(nine_square_cells)
                hash_map_square[3 * i + j] = possible_solutions_square

        return [hash_map_row, hash_map_column, hash_map_square]
