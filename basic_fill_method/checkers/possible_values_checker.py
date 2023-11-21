from numpy import array


class PossibleValuesChecker:

    @staticmethod
    def check_column_row(row: array) -> set:

        possible_solutions = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

        for value in row:
            if value != ".":
                try:
                    possible_solutions.remove(value)
                except:
                    pass

        return possible_solutions

    @staticmethod
    def check_square(square: array) -> set:

        possible_solutions = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

        for row in square:
            for value in row:
                if value != ".":
                    try:
                        possible_solutions.remove(value)
                    except:
                        pass

        return possible_solutions
