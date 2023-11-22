from numpy import array
from math import floor

from guess_fill_method.solution_roller_back import SolutionRollerBack


class DecisionMaker:

    @staticmethod
    def make(hash_map_intersection: dict, board: array, backups_boards: list) -> array:

        min_len = 10
        min_key, min_values = 0, 0

        for key, value in hash_map_intersection.items():
            if len(value) == 2:
                min_key, min_values = key, value
                break

            if len(value) < min_len:
                min_len = len(value)
                min_key, min_values = key, value

        try:
            current_guess = min_values.pop()
            backups_boards.append([min_key, min_values, array(board)])
            board[floor(min_key / 9)][min_key % 9] = current_guess
        except:
            board = SolutionRollerBack.roll_back(backups_boards)

        return board
