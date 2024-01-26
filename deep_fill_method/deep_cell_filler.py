from numpy import array

from deep_fill_method.searcher.deep_searcher import DeepSearcher


class DeepCellFiller:

    def __init__(
            self,
            hash_map_situation_cell: dict,
            hash_map_situation_row: dict,
            hash_map_situation_column: dict,
            hash_map_situation_square: dict
    ):

        self.hash_map_situation_cell = hash_map_situation_cell
        self.hash_map_situation_row = hash_map_situation_row
        self.hash_map_situation_column = hash_map_situation_column
        self.hash_map_situation_square = hash_map_situation_square

    def fill(self, hash_map_intersection: dict, board: array) -> array:

        keys = set(hash_map_intersection.keys())

        for key in keys:

            row, column, square = self.hash_map_situation_cell[key]

            row_neighbours = set(self.hash_map_situation_row[row])
            column_neighbours = set(self.hash_map_situation_column[column])
            square_neighbours = set(self.hash_map_situation_square[square])

            board = DeepSearcher.search(row_neighbours, keys, key, hash_map_intersection, board)
            board = DeepSearcher.search(column_neighbours, keys, key, hash_map_intersection, board)
            board = DeepSearcher.search(square_neighbours, keys, key, hash_map_intersection, board)

        return board
