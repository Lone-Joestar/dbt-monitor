from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import RunLog
from app.services.dbt_runner import dbt_run 


#creating router instance

router= APIRouter(prefix="/runs",tags=["runs"])

@router.post("/")
def trigger_run(db: Session=Depends(get_db)):
    result = dbt_run()
    log= RunLog(
        status="success" if result["success"] else "error",
        duration=None,
        output=result["stdout"]
    )
    db.add(log)
    db.commit()
    db.refresh(log)
    return {"message":"dbt run triggered", "status": log.status,"id":log.id}

@router.get("/")
def get_runs(db:Session=Depends(get_db)):
    runs=db.query(RunLog).all()
    return runs 