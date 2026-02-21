from __future__ import annotations

import re
from datetime import date

import requests
from bs4 import BeautifulSoup

from sudoku_daily_bot.core.models import Board, DailySudoku


class SevenSudokuScraper:
    URL = "https://www.7sudoku.com/"

    def __init__(self, timeout_seconds: int = 15) -> None:
        self.timeout_seconds = timeout_seconds

    def fetch_daily_sudoku(self) -> DailySudoku:
        response = requests.get(self.URL, timeout=self.timeout_seconds)
        response.raise_for_status()
        board = self.parse_board(response.text)
        return DailySudoku(puzzle_date=date.today(), board=board)

    @staticmethod
    def parse_board(html: str) -> Board:
        soup = BeautifulSoup(html, "html.parser")

        values: list[str] = []

        # Primary: input values (common in sudoku UIs)
        for inp in soup.select("input"):
            v = inp.get("value")
            if v is None:
                continue
            v = str(v).strip()
            if re.fullmatch(r"[0-9.]", v):
                values.append("0" if v == "." else v)

        # Fallbacks: data-value attributes
        if len(values) < 81:
            values = []
            for node in soup.select("[data-value]"):
                v = str(node.get("data-value", "")).strip()
                if re.fullmatch(r"[0-9.]", v):
                    values.append("0" if v == "." else v)

        # Last resort: find 81-char sudoku sequence in scripts/html
        if len(values) < 81:
            text = soup.get_text(" ") + "\n".join(script.get_text() for script in soup.select("script"))
            match = re.search(r"(?<!\d)([0-9.]{81})(?!\d)", text)
            if match:
                values = ["0" if c == "." else c for c in match.group(1)]

        if len(values) != 81:
            raise ValueError(f"Expected 81 cells from 7sudoku, got {len(values)}")

        return [values[i : i + 9] for i in range(0, 81, 9)]
