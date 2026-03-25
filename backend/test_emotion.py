from app.agents.emotion_agent import EmotionMappingAgent

agent = EmotionMappingAgent()

text = "we danced in the rain happily"

print(agent.map_emotions(text))
