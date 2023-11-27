from math import floor

from numpy import array


class SolutionRollerBack:

    @staticmethod
    def roll_back(backups_boards: list) -> array:

        board_configuration = backups_boards.pop()
        min_key, min_values, board = board_configuration
        current_guess = min_values.pop()
        board[floor(min_key / 9), min_key % 9] = current_guess

        return board
