import subprocess
import json 
from pathlib import Path 
import re

DBT_PROJECT_DIR = Path("dbt_project")


def run_dbt_command(command: list[str]) -> dict:

    result= subprocess.run(
        command,
        capture_output=True,
        text=True,
        cwd=DBT_PROJECT_DIR
    )
   
    return{
        "success": result.returncode==0,
        "stdout": re.sub(r'\x1b\[[0-9;]*m', '',result.stdout),
        "stderr": result.stderr
    }

#wrapper functions
def dbt_run() -> dict:
    return run_dbt_command(["dbt","run","--profiles-dir","."])

def dbt_test() -> dict:
    return run_dbt_command(["dbt","test","--profiles-dir","."])

def dbt_ls() -> dict:
    return run_dbt_command(["dbt","ls","--profiles-dir","."])