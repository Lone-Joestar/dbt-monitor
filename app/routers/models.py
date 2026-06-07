from fastapi import APIRouter
from app.services.dbt_runner import dbt_ls

router=APIRouter(prefix="/models",tags=["models"])

@router.get("/")
def list_models():
    result=dbt_ls()
    return result 