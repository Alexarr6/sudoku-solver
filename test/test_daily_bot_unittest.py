import unittest

from sudoku_daily_bot.application.formatters import board_to_pretty_text, success_message
from sudoku_daily_bot.infrastructure.scraper_7sudoku import SevenSudokuScraper


class DailyBotSmokeTests(unittest.TestCase):
    def test_parse_board_from_81_digits_script(self):
        digits = "0" * 81
        html = f"<html><body><script>const puzzle='{digits}'</script></body></html>"
        board = SevenSudokuScraper.parse_board(html)
        self.assertEqual(len(board), 9)
        self.assertTrue(all(len(row) == 9 for row in board))

    def test_board_to_pretty_text_shape(self):
        board = [["1"] * 9 for _ in range(9)]
        text = board_to_pretty_text(board)
        self.assertEqual(len(text.splitlines()), 9)

    def test_success_message_contains_sections(self):
        board = [["1"] * 9 for _ in range(9)]
        msg = success_message("2026-02-21", board, board)
        self.assertIn("Sudoku diario 7sudoku", msg)
        self.assertIn("Tablero original", msg)
        self.assertIn("Solución", msg)


if __name__ == "__main__":
    unittest.main()
