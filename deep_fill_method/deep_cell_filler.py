from numpy import array

from sudoku_solver.deep_fill_method.searcher.row_column_searcher import DeepSearcher
from sudoku_solver.situation.situation import hash_map_situation_cell, hash_map_situation_row,\
    hash_map_situation_column, hash_map_situation_square


class DeepCellFiller:

    @staticmethod
    def fill(hash_map_intersection: dict, board: array) -> array:

        keys = set(hash_map_intersection.keys())

        for key in keys:

            row, column, square = hash_map_situation_cell[key]

            row_neighbours = set(hash_map_situation_row[row])
            column_neighbours = set(hash_map_situation_column[column])
            square_neighbours = set(hash_map_situation_square[square])

            board = DeepSearcher.search(row_neighbours, keys, key, hash_map_intersection, board)
            board = DeepSearcher.search(column_neighbours, keys, key, hash_map_intersection, board)
            board = DeepSearcher.search(square_neighbours, keys, key, hash_map_intersection, board)

        return board
