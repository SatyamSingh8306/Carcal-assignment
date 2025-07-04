# Config is now loaded from environment variables or .env via app/__init__.py
from app.routes import wimbledon
from app import HOST, PORT, ENV
from fastapi import FastAPI
import uvicorn 

app = FastAPI(title="Wimbledon Result Provider")

app.include_router(wimbledon.router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host=HOST, port=PORT, reload=ENV == "development")