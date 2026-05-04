from fastapi import FastAPI
from agents import run_agent
from topics import generate_topics
from tracking import track_success, best_topics
from payments import create_payment

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI System Running"}

@app.get("/agent")
def agent(prompt: str):
    return {"response": run_agent(prompt)}

@app.get("/topics")
def topics():
    return {"topics": generate_topics()}

@app.post("/track")
def track(topic: str, score: int):
    track_success(topic, score)
    return {"status": "tracked"}

@app.get("/best")
def best():
    return best_topics()

@app.get("/pay")
def pay():
    return {"client_secret": create_payment()}
@app.get("/auto-post")
def auto_post(topic: str):
    result = run_agent(f"Create a viral Facebook post about: {topic}")
    return result
