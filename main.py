from fastapi import FastAPI
from pydantic import BaseModel
from agent_coordinator import agent
from database import init_db
from database import engine
from sqlalchemy import text

app = FastAPI()

init_db()

class Request(BaseModel):
    input: str

@app.get("/")
def home():
    return {"message": "Multi-Agent Assistant Running"}

@app.post("/run")
def run(req: Request):
    result = agent.run(req.input)
    return {
        "input": req.input,
        "actions_executed": result,
        "status": "success"
    }

@app.get("/tasks")
def get_tasks():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM tasks"))
        return [dict(row._mapping) for row in result]

@app.get("/events")
def get_events():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM events"))
        return [dict(row._mapping) for row in result]

@app.get("/notes")
def get_notes():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM notes"))
        return [dict(row._mapping) for row in result]
