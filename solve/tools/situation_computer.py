from typing import Tuple
import numpy as np
from math import floor


class SituationComputer:

    @staticmethod
    def compute_cell_situation() -> dict:
        cell_situation = {}
        for row in range(9):
            for column in range(9):
                key = row * 9 + column
                class_box = 3 * floor(row / 3) + floor(column / 3)
                cell_situation[key] = [row, column, class_box]

        return cell_situation

    @staticmethod
    def compute_structure_situation() -> Tuple:
        matriz_9x9 = np.arange(81).reshape(9, 9)
        row_situation = {}
        column_situation = {}
        box_situation = {}

        for i in range(9):
            row_situation[i] = matriz_9x9[i, :]
            column_situation[i] = matriz_9x9[:, i]

        for i in range(3):
            for j in range(3):
                nine_box_cells = matriz_9x9[i * 3: (i + 1) * 3, j * 3: (j + 1) * 3]
                flattened_list = [item for sublist in nine_box_cells.tolist() for item in sublist]
                box_situation[i * 3 + j] = flattened_list

        return row_situation, column_situation, box_situation
