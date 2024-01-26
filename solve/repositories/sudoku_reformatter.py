import pandas as pd
import numpy as np
import pickle
from typing import List

sudoku_dataset = pd.read_csv('../sudoku_solver/repositories/data/sudoku.csv')
sudoku_sample = sudoku_dataset[:100000]

solutions = list(sudoku_sample.loc[:, 'solution'])
puzzles = list(sudoku_sample.loc[:, 'puzzle'])


class SudokuReformatter:

    @staticmethod
    def reformat(sudokus: List[str]) -> List[np.array]:

        formatted_sudokus = []
        for sudoku in sudokus:
            board = []
            counter = 0
            row = []
            for value in sudoku:

                counter += 1
                if value == '0':
                    row.append('.')
                else:
                    row.append(value)

                if counter == 9:
                    counter = 0
                    board.append(row)
                    row = []

            formatted_sudokus.append(np.array(board))

        return formatted_sudokus


unresolved_boards = SudokuReformatter().reformat(puzzles)
resolved_boards = SudokuReformatter().reformat(solutions)

with open('../sudoku_solver/repositories/data/unresolved_boards_dataset_100000.pkl', 'wb') as file:
    pickle.dump(unresolved_boards, file)

with open('../sudoku_solver/repositories/data/resolved_boards_dataset_100000.pkl', 'wb') as file:
    pickle.dump(resolved_boards, file)
