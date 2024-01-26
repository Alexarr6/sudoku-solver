from math import floor

from numpy import array

from solve.board.board import Board
from solve.fillers.basic_fill_method.possible_solutions_creator import PossibleSolutionsCreator


class CellSolutionComputer:

    @staticmethod
    def compute(board: array) -> dict:

        cell_solutions = {}
        row_mapping, column_mapping, square_mapping = PossibleSolutionsCreator.possible_solutions_creator(board)

        for i in range(9):
            row_solutions_set = row_mapping[i]
            for j in range(9):
                if Board.is_empty_cell(board, i, j):
                    column_solutions_set = column_mapping[j]
                    square_solutions_set = square_mapping[3 * floor(i / 3) + floor(j / 3)]

                    intersection = row_solutions_set & column_solutions_set & square_solutions_set
                    cell_solutions[i * 9 + j] = intersection

        return cell_solutions
