from sudoku_daily_bot.application.formatters import error_message, success_message
from sudoku_daily_bot.core.interfaces import DailySudokuProvider, Notifier, SudokuSolverPort


class RunDailySudokuUseCase:
    def __init__(
        self,
        provider: DailySudokuProvider,
        solver: SudokuSolverPort,
        notifier: Notifier,
    ) -> None:
        self.provider = provider
        self.solver = solver
        self.notifier = notifier

    def execute(self) -> None:
        try:
            daily = self.provider.fetch_daily_sudoku()
            solved = self.solver.solve(daily.board)
            self.notifier.send(
                success_message(
                    date_text=daily.puzzle_date.isoformat(),
                    original=daily.board,
                    solution=solved,
                )
            )
        except Exception as exc:
            self.notifier.send(error_message(exc))
            raise
