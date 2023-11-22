# Sudoku solver project

This repository contains the code necessary to solve any Sudoku. The `example_boards.py` file includes some example 
Sudoku puzzles along with the input format, although it is possible to modify these Sudoku puzzles if you want to solve 
a specific one.

To do this, you would only need to modify the corresponding board and run the `main.py` file.

## Test data

Additionally, the code also includes two files for testing purposes. The first one is `sudoku_reformatter.py`, which is
responsible for accessing a CSV file with 9 million Sudoku puzzles and formatting them appropriately for the Sudoku 
solver. The CSV with the Sudoku puzzles can be found at [Kaggle](https://www.kaggle.com/datasets/rohanrao/sudoku/), and it's only
necessary to add it to the path `repositories/data/` for it to work.

The second file would be `sudoku_tester.py`, which is responsible for taking the Sudoku puzzles and solving them. This 
file also serves to check if the Sudokus are solved correctly and the time it takes to solve them