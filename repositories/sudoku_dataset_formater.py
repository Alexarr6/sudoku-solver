import pandas as pd
import numpy as np
import pickle

sudoku = pd.read_csv('../data/sudoku.csv')
sudoku_sample = sudoku[:10000]

solutions = list(sudoku_sample.loc[:, 'solution'])
puzzles = list(sudoku_sample.loc[:, 'puzzle'])

unresolved_boards = []
for puzzle in puzzles:
    board = []
    counter = 0
    row = []
    for value in puzzle:

        counter += 1
        if value == '0':
            row.append('.')
        else:
            row.append(value)

        if counter == 9:
            counter = 0
            board.append(row)
            row = []

    unresolved_boards.append(np.array(board))

resolved_boards = []
for solution in solutions:
    board = []
    counter = 0
    row = []
    for value in solution:

        counter += 1
        if value == '0':
            row.append('.')
        else:
            row.append(value)

        if counter == 9:
            counter = 0
            board.append(row)
            row = []

    resolved_boards.append(np.array(board))


with open('../data/unresolved_boards_dataset_10000.pkl', 'wb') as file:
    pickle.dump(unresolved_boards, file)

with open('../data/resolved_boards_dataset_10000.pkl', 'wb') as file:
    pickle.dump(resolved_boards, file)
