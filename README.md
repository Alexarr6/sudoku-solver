# Sudoku Daily Telegram Bot (7sudoku)

Proyecto para obtener el Sudoku diario de [7sudoku.com](https://www.7sudoku.com/), resolverlo con el solver existente del repositorio y enviar por Telegram el tablero original y su solución.

## Arquitectura

Estructura en capas bajo `src/sudoku_daily_bot`:

- `core/`
  - modelos de dominio (`DailySudoku`, `Board`)
  - interfaces/puertos (`DailySudokuProvider`, `SudokuSolverPort`, `Notifier`)
- `application/`
  - casos de uso (`RunDailySudokuUseCase`)
  - formateadores de mensaje para Telegram
- `infrastructure/`
  - scraper de 7sudoku
  - adapter para reutilizar el solver existente (`solve.main.main.SudokuSolver`)
  - notifier de Telegram
- `cli/`
  - entrypoint para ejecución manual/programada

El solver original **no se reescribe**: se integra mediante adapter en `infrastructure/solver_adapter.py`.

## Instalación con uv

```bash
uv sync --extra dev
```

> Si no tienes `uv`: https://docs.astral.sh/uv/

## Configuración de variables de entorno

1. Copia el ejemplo:

```bash
cp .env.example .env
```

2. Define:

- `TELEGRAM_BOT_TOKEN`: token del bot
- `TELEGRAM_CHAT_ID`: chat o canal de destino

## Ejecución manual

```bash
export TELEGRAM_BOT_TOKEN="..."
export TELEGRAM_CHAT_ID="..."
uv run python -m sudoku_daily_bot.cli.run_daily
```

O usando script:

```bash
./scripts/run_daily.sh
```

## Ejecución programada (09:30 Europe/Madrid)

No se aplica cron del sistema en este PR (depende del entorno), pero el comando queda listo.

Cron recomendado:

```cron
CRON_TZ=Europe/Madrid
30 9 * * * cd /ruta/al/repo && /usr/bin/env bash scripts/run_daily.sh >> /var/log/sudoku-daily.log 2>&1
```

## pre-commit

Configurado en `.pre-commit-config.yaml` con hooks:

- `ruff`
- `black`
- `end-of-file-fixer`
- `trailing-whitespace`

Instalación y uso:

```bash
uv run pre-commit install
uv run pre-commit run --all-files
```

## Tests

```bash
uv run pytest
```

Cobertura clave:

- parsing robusto de tablero (81 celdas)
- formato de mensajes
- flujo feliz y de error del caso de uso con mocks/stubs

## Troubleshooting

- **Error: `Expected 81 cells`**
  - El HTML de 7sudoku puede cambiar. El scraper implementa fallback (`input[value]`, `data-value`, secuencia de 81 chars). Revisar selectores si vuelve a cambiar.

- **Telegram 401/403**
  - Validar `TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID` y permisos del bot en el chat.

- **No module named `sudoku_daily_bot`**
  - Ejecuta comandos con `uv run ...` desde la raíz del proyecto.

- **No se encuentra solución**
  - El adapter lanza excepción y el caso de uso envía alerta por Telegram.
