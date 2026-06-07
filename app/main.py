from app.routers import runs
from fastapi import FastAPI 
from app.db.database import init_db
from app.routers import tests
from app.routers import models 


def create_app() -> FastAPI:

    app =FastAPI(title="dbt-monitor",version="0.1.0")
    init_db()
    app.include_router(tests.router)
    app.include_router(models.router)
    
    app.include_router(runs.router)
    return app

app = create_app()
