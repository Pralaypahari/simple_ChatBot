from fastapi import FastAPI
import uvicorn
from src.routes.chat_router import router as chat_router
from contextlib import asynccontextmanager
from src.services.database_services import db_manager
from dotenv import load_dotenv
import os

load_dotenv(overrride = True)

@asynccontextmanager
async def lifespan(app: FastAPI):
    db_manager.initialize(os.getenv("DB_URI"))
    print("database initialised")

    yield
    db_manager.close()
    print("Databse closed")

app = FastAPI(lifespan = lifespan)

app.include_router(chat_router)

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port = 8000)

