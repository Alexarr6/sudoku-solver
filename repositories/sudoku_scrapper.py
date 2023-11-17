import requests
from bs4 import BeautifulSoup
from numpy import array


class SudokuScrapper:

    @staticmethod
    def scrap(sudoku_url: str) -> array:

        response = requests.get(sudoku_url)

        if response.status_code == 200:

            soup = BeautifulSoup(response.text, features='html.parser')
            board = soup.find('table', {'id': 'sudoku_main_board'})

            cell_values = board.find_all("input", {'class': 'i3'})

            board = []
            row = []
            counter = 0

            for cell in cell_values:
                counter += 1

                try:
                    value = cell['value']
                    row.append(value)
                except:
                    row.append('.')

                if counter == 9:
                    board.append(row)
                    row = []
                    counter = 0

            return board
