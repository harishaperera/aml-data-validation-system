
from fastapi import FastAPI

app = FastAPI(
    title="AML Data Profiling API",
    description="API for AML transaction data profiling",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AML Data Profiling API",
        "status": "Running"
    }

@app.get("/profile")
def get_profile():
    import json

    with open("profiling_report.json", "r") as file:
        return json.load(file)
