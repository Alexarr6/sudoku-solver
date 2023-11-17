from numpy import array
from typing import Tuple
from math import floor


class BasicCellFiller:

    @staticmethod
    def fill(hash_map_row: dict, hash_map_column: dict, hash_map_square: dict, board: array) -> Tuple[array, dict]:

        hash_map_intersection = {}

        for i in range(9):
            possible_solutions_row = hash_map_row[i]
            for j in range(9):
                if board[i][j] == ".":
                    possible_solutions_column = hash_map_column[j]
                    square_index = 3 * floor(i / 3) + floor(j / 3)
                    possible_solutions_square = hash_map_square[square_index]
                    intersection = \
                        possible_solutions_row.intersection(possible_solutions_column, possible_solutions_square)

                    hash_map_intersection[i * 9 + j] = intersection

                    if len(intersection) == 1:

                        value = list(intersection)[0]
                        board[i][j] = value

        return board, hash_map_intersection
