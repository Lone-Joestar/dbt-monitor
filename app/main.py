from fastapi import FastAPI 
from app.db.database import init_db

def create_app() -> FastAPI:

    app =FastAPI(title="dbt-monitor",version="0.1.0")
    init_db()
    return app

app = create_app()
