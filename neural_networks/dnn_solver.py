import pickle
import numpy as np
from tensorflow import keras

from sudoku_solver.valid_sudoku_checker import ValidSudokuChecker

with open('../data/unresolved_boards_dataset.pkl', 'rb') as file:
    unresolved_boards = pickle.load(file)

with open('../data/resolved_boards_dataset.pkl', 'rb') as file:
    resolved_boards = pickle.load(file)

X = np.array(unresolved_boards)
Y = np.array(resolved_boards)

has_map = {'.': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
int_to_string = {-2: '1', -1: '1', 0: '1', 1: '1', 2: '2', 3: '3', 4: '4',
                 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '9', 11: '9', 12: '9', 13: '9'}

for i in range(len(X)):
    image = X[i]
    for j in range(len(image)):
        row = X[i][j]
        for k in range(len(row)):
            number = X[i][j][k]
            X[i][j][k] = int(has_map[number])

for i in range(len(Y)):
    image = Y[i]
    for j in range(len(image)):
        row = Y[i][j]
        for k in range(len(row)):
            number = Y[i][j][k]
            Y[i][j][k] = int(has_map[number])

X = X.astype(int)
Y = Y.astype(int)

X, Y = X / 9, Y / 9
x_train, x_test = X[:180000], X[180000:]
y_train, y_test = Y[:180000], Y[180000:]

model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(9, 9)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(512, activation='relu'),
    keras.layers.Dense(256, activation='relu'),
    keras.layers.Dense(128, activation='relu'),
    # keras.layers.Dense(9 * 9, activation='linear'),
    keras.layers.Dense(9 * 9, activation='sigmoid'),
    keras.layers.Reshape((9, 9))
])

model.compile(optimizer='adam', loss='mean_squared_error', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
model.evaluate(x_test,  y_test, verbose=2)

solutions = model.predict(x_test)
solutions = solutions * 9

for i in range(len(solutions)):
    image = solutions[i]
    for j in range(len(image)):
        row = solutions[i][j]
        for k in range(len(row)):
            number = solutions[i][j][k]
            solutions[i][j][k] = int_to_string[int(round(number))]

print(solutions[0])
print(solutions[1])

good_solutions = 0
bad_solutions = 0
for board in solutions:
    if ValidSudokuChecker.check(board):
        good_solutions += 1
    else:
        bad_solutions += 1

print('Good:', good_solutions)
print('Bad:', bad_solutions)
