from datetime import date

from sudoku_daily_bot.application.use_cases import RunDailySudokuUseCase
from sudoku_daily_bot.core.models import DailySudoku


class DummyProvider:
    def fetch_daily_sudoku(self) -> DailySudoku:
        return DailySudoku(puzzle_date=date(2026, 2, 21), board=[["0"] * 9 for _ in range(9)])


class DummySolver:
    def solve(self, board):
        return [["1"] * 9 for _ in range(9)]


class SpyNotifier:
    def __init__(self) -> None:
        self.messages = []

    def send(self, message: str) -> None:
        self.messages.append(message)


def test_use_case_happy_path() -> None:
    notifier = SpyNotifier()
    use_case = RunDailySudokuUseCase(DummyProvider(), DummySolver(), notifier)

    use_case.execute()

    assert len(notifier.messages) == 1
    assert "Solución" in notifier.messages[0]


def test_use_case_error_sends_alert() -> None:
    class FailingProvider:
        def fetch_daily_sudoku(self):
            raise RuntimeError("boom")

    notifier = SpyNotifier()
    use_case = RunDailySudokuUseCase(FailingProvider(), DummySolver(), notifier)

    try:
        use_case.execute()
        assert False, "Expected RuntimeError"
    except RuntimeError:
        pass

    assert len(notifier.messages) == 1
    assert "Error" in notifier.messages[0]
