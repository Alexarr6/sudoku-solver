from math import floor

from numpy import array

from solve.board.board import Board
from solve.fillers.basic_fill_method.possible_solutions_creator import PossibleSolutionsCreator


class CellSolutionComputer:

    @staticmethod
    def compute(board: array) -> dict:

        cell_solutions = {}
        row_possible_solutions, column_possible_solutions, square_possible_solutions = \
            PossibleSolutionsCreator.create(board)

        for row in range(9):
            row_solutions_set = row_possible_solutions[row]
            for column in range(9):
                if Board.is_empty_cell(board, row, column):
                    square = 3 * floor(row / 3) + floor(column / 3)
                    column_solutions_set = column_possible_solutions[column]
                    square_solutions_set = square_possible_solutions[square]

                    intersection = row_solutions_set & column_solutions_set & square_solutions_set
                    cell_solutions[row * 9 + column] = intersection

        return cell_solutions
