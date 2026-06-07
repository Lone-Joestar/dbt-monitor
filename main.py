from fastapi import FastAPI

app=FastAPI(
    title="dbt Pipeline monitor",
    description="monitor your dbt project with APIs ",
    version="0.1.0"
)

@app.get("/health")
def health():
    return {"status":"alive","service":"dbt-monitor"}

