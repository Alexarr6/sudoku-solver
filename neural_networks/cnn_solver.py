import pickle
import numpy as np
from tensorflow import keras

from sudoku_solver.valid_sudoku_checker import ValidSudokuChecker


with open('../data/unresolved_boards_dataset.pkl', 'rb') as file:
    unresolved_boards = pickle.load(file)

with open('../data/resolved_boards_dataset.pkl', 'rb') as file:
    resolved_boards = pickle.load(file)

n = len(unresolved_boards)
print("Number of observation:", n)
unresolved_boards = unresolved_boards[:n]
resolved_boards = resolved_boards[:n]

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

X = np.array(X).reshape(-1, 9, 9, 1)
Y = np.array(Y).reshape(-1, 9, 9)

X = X / 9

X -= 0.5
Y -= 1

m = int(n * 0.8)

x_train, x_test = X[:m], X[m:]
y_train, y_test = Y[:m], Y[m:]

model = keras.models.Sequential([
    keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu', padding='same', input_shape=(9, 9, 1)),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu', padding='same'),
    keras.layers.BatchNormalization(),
    keras.layers.Conv2D(512, kernel_size=(3, 3), activation='relu', padding='same'),
    keras.layers.Flatten(),
    keras.layers.Dense(81 * 9, activation='relu'),
    keras.layers.LayerNormalization(axis=-1),
    keras.layers.Reshape((9, 9, 9)),
    keras.layers.Activation('softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

history1 = model.fit(x_train, y_train, batch_size=32, epochs=10, validation_data=(x_test, y_test))

model.evaluate(x_test,  y_test, verbose=2)

solutions = model.predict(x_test).argmax(-1)+1
y_test = y_test + 1

solutions = solutions.astype(int)

good_solutions = 0
bad_solutions = 0
for board in solutions:
    if ValidSudokuChecker.check(board):
        good_solutions += 1
    else:
        bad_solutions += 1

print('Good:', good_solutions)
print('Bad:', bad_solutions)

print('End!')
