FROM ghcr.io/astral-sh/uv:python3.14-bookworm-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY bot/pyproject.toml ./bot/pyproject.toml

RUN uv sync --frozen --no-dev --project bot

COPY bot/ ./bot/

WORKDIR /app/bot

CMD ["uv", "run", "bot.py"]
