#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

uv run python -m sudoku_daily_bot.cli.run_daily
