
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import uuid


# =========================
# SCENE MODEL
# =========================
class Scene(BaseModel):
    scene_id: int
    title: str
    description: str

    # AI-generated attributes
    emotions: List[Dict[str, Any]] = Field(default_factory=list)
    sensory_details: Dict[str, Any] = Field(default_factory=dict)

    # People involved in this scene
    people: List[Dict[str, Any]] = Field(default_factory=list)

    # Cinematic controls
    duration: float = 3.0  # seconds
    camera: str = "medium shot"  # wide, close-up, aerial, etc.

    # Visual output metadata
    image: Dict[str, Any] = Field(default_factory=dict)
    video_clip: Optional[str] = None


# =========================
# MEMORY MODEL
# =========================
class Memory(BaseModel):
    memory_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    original_text: str

    # Extracted structured scenes
    scenes: List[Scene]

    # Global people involved
    people: List[Dict[str, Any]] = Field(default_factory=list)

    # Optional metadata
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())

    # Mode (free / real)
    mode: str = "free"

