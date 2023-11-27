import pickle
import time
from main import SudokuSolver

with open('../repositories/data/unresolved_boards_dataset_100000.pkl', 'rb') as file:
    unresolved_boards = pickle.load(file)

with open('../repositories/data/resolved_boards_dataset_100000.pkl', 'rb') as file:
    resolved_boards = pickle.load(file)


n_sample = 100000
total_solved = 0
unsuccessfully_solved = 0
inicio = time.time()
for i in range(n_sample):

    unresolved_board = unresolved_boards[i]
    resolved_board = resolved_boards[i]

    try:
        solution = SudokuSolver().solve(unresolved_board)
        total_solved += (solution == resolved_board).all()
    except:
        unsuccessfully_solved += 1

    if i % 5000 == 0:
        print('Iter:', i)

final = time.time()

print()
print("--------Results--------")
print()
print("Total solved:", total_solved)
print("Total fails:", unsuccessfully_solved)
print('Total time:', final - inicio)
