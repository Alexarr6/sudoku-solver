from numpy import array
from math import floor

from solve.board.board import Board


class DeepSearcher:

    @staticmethod
    def search(neighbours: set, keys: set, key: int, cell_solutions: dict, board: array) -> array:

        not_key_set = set()
        key_values = cell_solutions[key]

        for value in neighbours & keys:
            if value == key:
                continue
            not_key_set = not_key_set.union(set(cell_solutions[value]))

        difference = key_values.difference(not_key_set)

        if len(difference) == 1:
            difference = difference.pop()
            board = Board.fill_cell(board, floor(key / 9), key % 9, difference)

        return board
