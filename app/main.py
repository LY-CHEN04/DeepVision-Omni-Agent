
from fastapi import FastAPI
from app.workflow import execute_workflow

app = FastAPI(title="DeepVision Omni-Agent")

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/campaign")
def campaign(topic: str):
    return execute_workflow(topic)
