from sudoku_daily_bot.infrastructure.scraper_7sudoku import SevenSudokuScraper


def test_parse_board_from_inputs() -> None:
    digits = "530070000" * 9
    html = "".join(f'<input value="{d}" />' for d in digits)

    board = SevenSudokuScraper.parse_board(html)

    assert len(board) == 9
    assert all(len(row) == 9 for row in board)
    assert board[0] == list("530070000")


def test_parse_board_raises_if_not_81_cells() -> None:
    html = "".join('<input value="0" />' for _ in range(80))
    try:
        SevenSudokuScraper.parse_board(html)
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert "Expected 81 cells" in str(exc)
