
# =========================
# memory.py (FINAL FIXED)
# =========================

from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import FileResponse
import os

from app.core.memory_orchestrator import MemoryOrchestrator

router = APIRouter()

# =========================
# REQUEST MODEL
# =========================
class MemoryRequest(BaseModel):
    text: str
    mode: str = "free"


# =========================
# MAIN API
# =========================
@router.post("/parse-memory")
def parse_memory(request: MemoryRequest):

    try:
        print("🧠 Processing memory...")

        orchestrator = MemoryOrchestrator()

        result = orchestrator.process(request.text)

        print("🔍 RESULT:", result)

        # ✅ CHECK IMAGE OUTPUT
        if result.get("type") == "image":

            image_path = result.get("image_path")

            if image_path and os.path.exists(image_path):
                return FileResponse(
                    image_path,
                    media_type="image/jpeg",
                    filename="output.jpg"
                )
            else:
                return {"error": "Image file not found"}

        return {"error": result.get("message", "Unknown error")}

    except Exception as e:
        print("❌ API ERROR:", str(e))
        return {"error": str(e)}

