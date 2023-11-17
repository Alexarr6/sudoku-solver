from numpy import array

from sudoku_solver.deep_fill_method.searcher.row_column_searcher import DeepSearcher


class DeepCellFiller:

    @staticmethod
    def fill(
            hash_map_intersection: dict,
            hash_map_situation_cell: dict,
            hash_map_situation_row: dict,
            hash_map_situation_column: dict,
            hash_map_situation_square: dict,
            board: array
    ) -> array:

        keys = set(hash_map_intersection.keys())

        for key in keys:
            key_values = hash_map_intersection[key]

            row, column, square = hash_map_situation_cell[key]

            row_neighbours = set(hash_map_situation_row[row])
            column_neighbours = set(hash_map_situation_column[column])
            square_neighbours = set(hash_map_situation_square[square])

            board = DeepSearcher.search(row_neighbours, keys, key, key_values, hash_map_intersection, board)
            board = DeepSearcher.search(column_neighbours, keys, key, key_values, hash_map_intersection, board)
            board = DeepSearcher.search(square_neighbours, keys, key, key_values, hash_map_intersection, board)

        return board
