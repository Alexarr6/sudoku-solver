import pickle
import time
from solve.main.main import SudokuSolver

with open('data/unresolved_boards_dataset_100000.pkl', 'rb') as file:
    unresolved_boards = pickle.load(file)

with open('data/resolved_boards_dataset_100000.pkl', 'rb') as file:
    resolved_boards = pickle.load(file)


n_sample = 100000
total_solved = 0
unsuccessfully_solved = 0
inicio = time.time()
for index in range(n_sample):

    unresolved_board = unresolved_boards[index]
    resolved_board = resolved_boards[index]

    try:
        solution = SudokuSolver().solve(unresolved_board)
        total_solved += (solution == resolved_board).all()
    except:
        unsuccessfully_solved += 1

    if index % 5000 == 0:
        print('Iter:', index)

final = time.time()

print()
print("--------Results--------")
print()
print("Total solved:", total_solved)
print("Total fails:", unsuccessfully_solved)
print('Total time:', final - inicio)
