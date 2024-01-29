from math import floor
from numpy import array

from solve.situation.situation import cell_situation, row_situation, column_situation, \
    box_situation


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

        for key, value in cell_situation.items():
            neighbour_row = row_situation[value[0]]
            neighbour_column = column_situation[value[1]]
            neighbour_box = box_situation[value[2]]

            cell_value = board[floor(key / 9), key % 9]

            row_values = self._set_values_getter(board, neighbour_row, key)
            column_values = self._set_values_getter(board, neighbour_column, key)
            box_values = self._set_values_getter(board, neighbour_box, key)

            union = row_values | column_values | box_values

            if cell_value in union:
                return False

        return True
