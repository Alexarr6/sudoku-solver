import abc
from numpy import array


class CellFiller(abc.ABC):

    @abc.abstractmethod
    def fill(self, board: array, cell_solutions: dict) -> dict:
        pass
