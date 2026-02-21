from sudoku_daily_bot.application.formatters import board_to_pretty_text, success_message


def test_board_to_pretty_text() -> None:
    board = [["1", "2"], ["3", "4"]]
    assert board_to_pretty_text(board) == "1 2\n3 4"


def test_success_message_contains_sections() -> None:
    board = [["0"] * 9 for _ in range(9)]
    msg = success_message("2026-02-21", board, board)
    assert "Sudoku diario" in msg
    assert "Tablero original" in msg
    assert "Solución" in msg
