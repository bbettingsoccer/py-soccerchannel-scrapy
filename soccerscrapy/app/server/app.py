from fastapi import FastAPI
from .routes import soccerscrapy_router as SoccerScrapyRouter

app = FastAPI()
app.include_router(SoccerScrapyRouter.router, tags=["SoccerScrapyPlanner"], prefix="/soccerscrapy")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this SheduleMatch domain !"}

