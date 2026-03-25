from fastapi import FastAPI
from app.api.memory import router as memory_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(
    title="Memory Resurrection Engine",
    version="1.0.0"
)

@app.get("/")
def health_check():
    return {
        "status": "running",
        "message": "Memory Resurrection Engine backend is live"
    }

# Register Scene Parser Endpoint
app.include_router(memory_router, prefix="/memory", tags=["Memory"])



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
