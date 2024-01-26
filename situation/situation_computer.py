from typing import Tuple
import numpy as np
from math import floor


class SituationComputer:

    @staticmethod
    def compute_cell_situation() -> dict:
        hash_map_situation_cell = {}
        for i in range(9):
            for j in range(9):
                key = i * 9 + j
                class_square = 3 * floor(i / 3) + floor(j / 3)
                hash_map_situation_cell[key] = [i, j, class_square]

        return hash_map_situation_cell

    @staticmethod
    def compute_structure_situation() -> Tuple:
        matriz_9x9 = np.arange(81).reshape(9, 9)
        hash_map_situation_row = {}
        hash_map_situation_column = {}
        hash_map_situation_square = {}

        for i in range(9):
            hash_map_situation_row[i] = matriz_9x9[i, :]
            hash_map_situation_column[i] = matriz_9x9[:, i]

        for i in range(3):
            for j in range(3):
                nine_square_cells = matriz_9x9[i * 3: (i + 1) * 3, j * 3: (j + 1) * 3]
                flattened_list = [item for sublist in nine_square_cells.tolist() for item in sublist]
                hash_map_situation_square[i * 3 + j] = flattened_list

        return hash_map_situation_row, hash_map_situation_column, hash_map_situation_square
