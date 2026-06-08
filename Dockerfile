FROM python:3.12-slim AS builder 

WORKDIR /app

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv


COPY pyproject.toml .
COPY uv.lock .

RUN uv sync --frozen --no-dev 

COPY . .

FROM python:3.12-slim AS runtime

WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    libgomp1 \
    tini \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app /app 

ENV PATH="/app/.venv/bin:$PATH"

#security layer
RUN groupadd --gid 1001 appuser && useradd --uid 1001 --gid appuser --no-create-home appuser
RUN chown -R appuser:appuser /app
USER appuser

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD python -c "import urllib.request ; urllib.request.urlopen('http://localhost:8000/docs')"


ENTRYPOINT ["/usr/bin/tini", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]