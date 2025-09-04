from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from pathlib import Path
import random

app = FastAPI()

# Allow frontend requests (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # replace "*" with your actual frontend URL when deployed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to text.txt
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEXT_FILE = os.path.join(BASE_DIR, "text.txt")

@app.get("/text", response_class=PlainTextResponse)
def get_text():
    """Return one random line from text.txt"""
    if not TEXT_FILE.exists():
        return "Error: text.txt not found"
    lines = TEXT_FILE.read_text(encoding="utf-8").splitlines()
    lines = [line.strip() for line in lines if line.strip()]
    return random.choice(lines) if lines else "Error: no text available"

@app.get("/health", response_class=PlainTextResponse)
def health():
    return "ok"
