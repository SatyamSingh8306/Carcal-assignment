from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.wimbledon import router as wimbledon_router

app = FastAPI(
    title="Wimbledon API",
    version="0.1.0",
    servers=[{"url": "/v1", "description": "Version 1"}],
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Welcome to the Wimbledon Tournament Service"}

app.include_router(wimbledon_router)


