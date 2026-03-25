from app.agents.people_detector import PeopleDetectorAgent
from app.agents.scene_parser import SceneParserAgent
from app.agents.emotion_agent import EmotionAgent
from app.agents.visual_agent import VisualAgent

class MemoryPipeline:
    def __init__(self):
        self.people_agent = PeopleDetectorAgent()
        self.scene_agent = SceneParserAgent()
        self.emotion_agent = EmotionAgent()
        self.visual_agent = VisualAgent()

    def process(self, text: str):
        people = self.people_agent.detect_people(text)
        scene = self.scene_agent.parse_scene(text)
        emotion = self.emotion_agent.detect_emotion(text)

        memory = {
            "text": text,
            "people": people["people"],
            "scene": scene,
            "emotion": emotion
        }

        output = self.visual_agent.generate(memory)

        return {
            "memory": memory,
            "output": output
        }