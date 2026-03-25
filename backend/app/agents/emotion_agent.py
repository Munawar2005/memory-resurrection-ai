
# =========================
# emotion_agent.py (ULTIMATE FINAL VERSION)
# =========================

from typing import List, Dict
from app.services.llm_service import LLMService


class EmotionMappingAgent:

    def __init__(self, llm: LLMService = None):
        self.llm = llm or LLMService()

    # =========================
    # MAIN ENTRY
    # =========================
    def map_emotions(self, text: str) -> List[Dict]:

        try:
            print("💙 Using LLM emotion detection...")
            return self._llm_emotion(text)

        except Exception as e:
            print("⚠️ LLM failed, using fallback:", e)
            return self._fallback(text)

    # =========================
    # LLM EMOTION DETECTION
    # =========================
    def _llm_emotion(self, text: str) -> List[Dict]:

        prompt = f"""
You are an emotion analysis AI.

TASK:
Detect emotions from the given scene.

RULES:
- Return ONLY a JSON array
- Each item must contain:
  - "emotion": string
  - "intensity": float (0 to 1)
- Use real human emotions (joy, sadness, excitement, nostalgia, etc.)
- Max 2 emotions
- No explanation

Scene:
{text}
"""

        result = self.llm.generate_json(prompt)

        # -------------------------
        # SAFETY HANDLING
        # -------------------------

        if isinstance(result, dict):
            result = list(result.values())

        if not isinstance(result, list):
            raise ValueError("Invalid LLM emotion format")

        emotions = []

        for item in result:

            if isinstance(item, dict):

                # normalize keys
                item_lower = {k.lower(): v for k, v in item.items()}

                emotion = item_lower.get("emotion", "neutral")
                intensity = item_lower.get("intensity", 0.5)

                # type safety
                emotion = str(emotion)

                try:
                    intensity = float(intensity)
                except:
                    intensity = 0.5

                # clamp between 0–1
                intensity = max(0.0, min(1.0, intensity))

                emotions.append({
                    "emotion": emotion,
                    "intensity": intensity
                })

        if not emotions:
            raise ValueError("No emotions detected")

        # -------------------------
        # NORMALIZATION + DEDUPLICATION
        # -------------------------

        emotion_map = { "happiness": "joy", "happy": "joy", "playfulness": "joy", "fun": "joy", "excited": "excitement", "fearful": "fear", "scared": "fear", "angry": "anger", "sad": "sadness", "depressed": "sadness" }

        unique = {}

        for e in emotions:
            name = e["emotion"].lower()

            # normalize
            name = emotion_map.get(name, name)

            # keep highest intensity
            if name not in unique or e["intensity"] > unique[name]["intensity"]:
                unique[name] = {
                    "emotion": name,
                    "intensity": e["intensity"]
                }

        emotions = list(unique.values())

        return emotions

    # =========================
    # FALLBACK METHOD
    # =========================
    def _fallback(self, text: str) -> List[Dict]:

        text = text.lower()

        if "happy" in text or "laugh" in text:
            return [{"emotion": "joy", "intensity": 0.8}]

        elif "sad" in text or "cry" in text:
            return [{"emotion": "sadness", "intensity": 0.7}]

        elif "angry" in text:
            return [{"emotion": "anger", "intensity": 0.8}]

        elif "love" in text:
            return [{"emotion": "affection", "intensity": 0.9}]

        return [{"emotion": "neutral", "intensity": 0.5}]

