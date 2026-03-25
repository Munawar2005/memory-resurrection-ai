
# =========================
# memory_orchestrator.py (FINAL STABLE VERSION)
# =========================

from app.agents.visual_agent import VisualReconstructionAgent


class MemoryOrchestrator:

    def __init__(self):
        # Initialize visual agent
        self.visual_agent = VisualReconstructionAgent()

    # =========================
    # MAIN PIPELINE FUNCTION
    # =========================
    def process(self, text):

        print("🧠 Processing memory...")

        # 🔥 SIMPLE PARSING (NO LLM NEEDED)
        scene_data = self._parse_text(text)

        print("📦 Scene Data:", scene_data)

        # 🔥 GENERATE VISUAL OUTPUT
        result = self.visual_agent.generate(scene_data)

        print("🎯 Final Output:", result)

        return result

    # =========================
    # BASIC TEXT PARSER
    # =========================
    def _parse_text(self, text):

        text_lower = text.lower()

        # 🎯 Detect emotion
        if any(word in text_lower for word in ["happy", "laugh", "celebrate", "birthday", "fun"]):
            emotion = "joy"
        elif any(word in text_lower for word in ["sad", "cry", "goodbye", "alone"]):
            emotion = "sadness"
        elif any(word in text_lower for word in ["angry", "fight"]):
            emotion = "anger"
        elif any(word in text_lower for word in ["fear", "dark", "scared"]):
            emotion = "fear"
        else:
            emotion = "neutral"

        # 🎯 Scene = full text
        scene = text

        # 🎯 No people (simplified for demo)
        people = []

        return {
            "scene": scene,
            "emotion": emotion,
            "people": people
        }

