import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8000))
ENV = os.getenv("ENV", "development")

GROQ_MODEL = os.environ.get("GROQ_MODEL")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")