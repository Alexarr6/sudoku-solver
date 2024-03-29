from numpy import array

from solve.fillers.cell_filler import CellFiller
from solve.fillers.deep_fill_method.searcher.deep_searcher import DeepSearcher
from solve.tools.situation_computer import SituationComputer


class DeepCellFiller(CellFiller):

    def __init__(self):

        cell_situation = SituationComputer.compute_cell_situation()
        row_situation, column_situation, box_situation = SituationComputer.compute_structure_situation()

        self.cell_situation = cell_situation
        self.row_situation = row_situation
        self.column_situation = column_situation
        self.box_situation = box_situation

    def fill(self, board: array, cell_solutions: dict) -> array:

        keys = set(cell_solutions.keys())

        for key in keys:

            row, column, box = self.cell_situation[key]

            row_neighbours = set(self.row_situation[row])
            column_neighbours = set(self.column_situation[column])
            box_neighbours = set(self.box_situation[box])

            board = DeepSearcher.search(row_neighbours, keys, key, cell_solutions, board)
            board = DeepSearcher.search(column_neighbours, keys, key, cell_solutions, board)
            board = DeepSearcher.search(box_neighbours, keys, key, cell_solutions, board)

        return board
