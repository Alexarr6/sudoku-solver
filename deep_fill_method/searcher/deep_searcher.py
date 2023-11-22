from numpy import array
from math import floor


class DeepSearcher:

    @staticmethod
    def search(row_neighbours: set, keys: set, key: int, hash_map_intersection: dict, board: array) -> array:

        not_key_set = set()
        key_values = hash_map_intersection[key]

        for value in row_neighbours & keys:
            if value == key:
                continue

            not_key_set = not_key_set.union(set(hash_map_intersection[value]))

        difference = key_values.difference(not_key_set)

        if len(difference) == 1:

            difference = difference.pop()
            board[floor(key / 9), key % 9] = difference

        return board
