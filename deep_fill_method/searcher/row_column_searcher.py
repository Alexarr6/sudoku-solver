from numpy import array
from math import floor


class DeepSearcher:

    @staticmethod
    def search(
            row_neighbours: set,
            keys: set,
            key: int,
            key_values: set,
            hash_map_intersection: dict,
            board: array
    ) -> array:

        intersection = row_neighbours & keys
        not_key_set = set()

        for value in intersection:

            if value == key:
                pass
            else:
                not_key_values = hash_map_intersection[value]
                not_key_set = not_key_set.union(set(not_key_values))

        difference = key_values.difference(not_key_set)

        if len(difference) == 1:

            difference = difference.pop()
            board[floor(key / 9)][key % 9] = difference

        return board
