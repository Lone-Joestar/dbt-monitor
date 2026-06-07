from fastapi import APIRouter
from app.services.dbt_runner import dbt_test

router=APIRouter(prefix="/tests",tags=["tests"])

@router.get("/")
def run_tests():
    result =dbt_test()
    return result


