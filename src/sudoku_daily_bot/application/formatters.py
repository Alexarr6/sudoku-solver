from sudoku_daily_bot.core.models import Board


def board_to_pretty_text(board: Board) -> str:
    return "\n".join(" ".join(row) for row in board)


def success_message(date_text: str, original: Board, solution: Board) -> str:
    return (
        f"✅ Sudoku diario 7sudoku ({date_text})\n\n"
        "🧩 Tablero original:\n"
        f"{board_to_pretty_text(original)}\n\n"
        "🏁 Solución:\n"
        f"{board_to_pretty_text(solution)}"
    )


def error_message(error: Exception) -> str:
    return f"🚨 Error en sudoku diario: {type(error).__name__}: {error}"
