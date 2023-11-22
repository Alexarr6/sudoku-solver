from typing import List, Dict
from numpy import array
from basic_fill_method.checkers.possible_values_checker import PossibleValuesChecker


class PossibleSolutionsCreator:

    @staticmethod
    def possible_solutions_creator(array_board: array) -> List[Dict[int, set]]:

        hash_map_row = {}
        hash_map_column = {}
        hash_map_square = {}

        for i in range(9):
            hash_map_row[i] = PossibleValuesChecker.check_column_row(array_board[i, :])
            hash_map_column[i] = PossibleValuesChecker.check_column_row(array_board[:, i])

        for i in range(3):
            for j in range(3):
                nine_square_cells = array_board[i * 3: (i + 1) * 3, j * 3: (j + 1) * 3]
                hash_map_square[3 * i + j] = PossibleValuesChecker.check_square(nine_square_cells)

        return [hash_map_row, hash_map_column, hash_map_square]
