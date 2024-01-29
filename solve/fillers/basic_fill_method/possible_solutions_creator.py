from typing import List, Dict
from numpy import array
from solve.fillers.basic_fill_method.checkers.possible_values_checker import PossibleValuesChecker


class PossibleSolutionsCreator:

    @staticmethod
    def create(board: array) -> List[Dict[int, set]]:
        row_possible_solutions = {}
        column_possible_solutions = {}
        square_possible_solutions = {}
        for i in range(9):
            row_possible_solutions[i] = PossibleValuesChecker.check_column_row(board[i, :])
            column_possible_solutions[i] = PossibleValuesChecker.check_column_row(board[:, i])

        for i in range(3):
            for j in range(3):
                nine_square_cells = board[i * 3: (i + 1) * 3, j * 3: (j + 1) * 3]
                square_possible_solutions[3 * i + j] = PossibleValuesChecker.check_square(nine_square_cells)

        return [row_possible_solutions, column_possible_solutions, square_possible_solutions]
