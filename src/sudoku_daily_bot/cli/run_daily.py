import os

from sudoku_daily_bot.application.use_cases import RunDailySudokuUseCase
from sudoku_daily_bot.infrastructure.scraper_7sudoku import SevenSudokuScraper
from sudoku_daily_bot.infrastructure.solver_adapter import ExistingSolverAdapter
from sudoku_daily_bot.infrastructure.telegram_notifier import TelegramNotifier


def _required_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required env var: {name}")
    return value


def main() -> None:
    notifier = TelegramNotifier(
        bot_token=_required_env("TELEGRAM_BOT_TOKEN"),
        chat_id=_required_env("TELEGRAM_CHAT_ID"),
    )

    use_case = RunDailySudokuUseCase(
        provider=SevenSudokuScraper(),
        solver=ExistingSolverAdapter(),
        notifier=notifier,
    )
    use_case.execute()


if __name__ == "__main__":
    main()
