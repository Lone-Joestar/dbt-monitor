dbt-monitor
A  FastAPI service that monitors and drives a dbt project over HTTP. Trigger dbt runs, fetch run history, check test results, and list models — all via a clean REST API.


Stack

FastAPI — HTTP layer with automatic docs at /docs
dbt-core + dbt-duckdb — transformation engine
DuckDB — embedded database (no server needed)
SQLAlchemy — ORM for storing run history
Docker — multi-stage build, non-root user, tini, HEALTHCHECK
Docker Compose — single-command local dev


Endpoints
MethodRouteDescriptionPOST/runs/Trigger a dbt run and store the resultGET/runs/Fetch full run historyGET/tests/Trigger dbt test and return resultsGET/models/List all models via dbt ls

Quickstart
With Docker Compose (recommended):
bashdocker compose up --build
Without Docker:
bashuv sync
uv run uvicorn app.main:app --reload
API live at http://localhost:8000
Docs at http://localhost:8000/docs

Project Structure
dbt-monitor/
├── app/
│   ├── main.py              # App factory
│   ├── routers/             # HTTP routes
│   ├── services/            # dbt subprocess runner
│   ├── db/                  # SQLAlchemy models + session
│   └── schemas/             # Pydantic response shapes
├── dbt_project/             # Real dbt project (DuckDB adapter)
├── Dockerfile               # Multi-stage build
├── docker-compose.yml       # Local dev setup
└── pyproject.toml           # uv dependencies

Docker
The image uses:

Multi-stage build — lean runtime image, no build tools
Non-root user — runs as UID 1001
tini — proper PID 1 signal handling
HEALTHCHECK — liveness probe on /docs every 30s

Build and run manually:
bashdocker build -t dbt-monitor:latest .
docker run -p 8000:8000 dbt-monitor:latest

Package manager
Always use uv:
bashuv add <package>      # install
uv run <command>      # run in venv
