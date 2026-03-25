
# =========================
# scene_parser.py (ULTIMATE FINAL VERSION)
# =========================

from typing import List
from app.models.memory import Scene
from app.services.llm_service import LLMService
import re


class SceneParserAgent:

    def __init__(self, llm: LLMService = None):
        self.llm = llm or LLMService()

    # =========================
    # MAIN ENTRY
    # =========================
    def parse(self, memory_text: str) -> List[Scene]:

        try:
            print("🧠 Using LLM scene parsing...")
            return self._llm_parse(memory_text)

        except Exception as e:
            print("⚠️ LLM failed, using fallback:", e)
            return self._fallback(memory_text)

    # =========================
    # LLM PARSING
    # =========================
    def _llm_parse(self, text: str) -> List[Scene]:

        prompt = f"""
You are a strict JSON generator.

TASK:
Convert the given memory into a list of short visual scenes.

RULES:
- Output ONLY a JSON array []
- Each item should represent ONE scene
- Prefer format: {{"description": "..."}}
- Maintain chronological order
- Keep scenes short and visual
- DO NOT explain anything

Memory:
{text}
"""

        result = self.llm.generate_json(prompt)

        # -------------------------
        # SAFETY HANDLING
        # -------------------------

        # Case 1: dict → convert to list
        if isinstance(result, dict):
            result = list(result.values())

        # Case 2: invalid
        if not isinstance(result, list):
            raise ValueError("Invalid LLM output format")

        scenes = []

        for i, item in enumerate(result):

            description = ""

            # -------------------------
            # SMART EXTRACTION LOGIC (ULTIMATE)
            # -------------------------

            # Case 1: dict
            if isinstance(item, dict):

                # Normalize keys → lowercase
                item_lower = {k.lower(): v for k, v in item.items()}

                if "description" in item_lower:
                    description = str(item_lower["description"]).strip()

                elif "scene" in item_lower:
                    description = str(item_lower["scene"]).strip()

                elif "text" in item_lower:
                    description = str(item_lower["text"]).strip()

                else:
                    values = [
                        str(v) for v in item.values()
                        if isinstance(v, (str, int))
                    ]
                    description = " ".join(values).strip()

            # Case 2: list (🔥 handles your current issue)
            elif isinstance(item, list):
                description = " ".join([str(x) for x in item]).strip()

            # Case 3: string
            elif isinstance(item, str):
                description = item.strip()

            # Skip empty
            if not description:
                continue

            scenes.append(
                Scene(
                    scene_id=i + 1,
                    title=f"Scene {i + 1}",
                    description=description,
                    emotions=[],
                    sensory_details={},
                    people=[]
                )
            )

        # If nothing valid → fallback
        if not scenes:
            raise ValueError("No valid scenes generated")

        return scenes

    # =========================
    # FALLBACK METHOD
    # =========================
    def _fallback(self, text: str) -> List[Scene]:

        sentences = re.split(r'[.!?]+', text)

        scenes = []

        for i, s in enumerate(sentences):
            s = s.strip()

            if not s:
                continue

            scenes.append(
                Scene(
                    scene_id=i + 1,
                    title=f"Scene {i + 1}",
                    description=s,
                    emotions=[],
                    sensory_details={},
                    people=[]
                )
            )

        return scenes

