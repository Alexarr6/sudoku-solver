from math import floor
from numpy import array

from situation.situation import hash_map_situation_cell, hash_map_situation_row, hash_map_situation_column, \
    hash_map_situation_square


class ValidSudokuChecker:

    @staticmethod
    def _set_values_getter(board: array, neighbours: set, key: int) -> set:
        values = set()
        for key in neighbours - {key}:
            value = board[floor(key / 9), key % 9]
            if value != '.':
                values.add(value)
        return values

    def check(self, board: array) -> bool:

        for key, value in hash_map_situation_cell.items():
            neighbour_row = hash_map_situation_row[value[0]]
            neighbour_column = hash_map_situation_column[value[1]]
            neighbour_square = hash_map_situation_square[value[2]]

            cell_value = board[floor(key / 9), key % 9]

            row_values = self._set_values_getter(board, neighbour_row, key)
            column_values = self._set_values_getter(board, neighbour_column, key)
            square_values = self._set_values_getter(board, neighbour_square, key)

            union = row_values | column_values | square_values

            if cell_value in union:
                return False

        return True
