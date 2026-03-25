
from app.services.llm_service import LLMService

llm = LLMService()

prompt = """
Break into scenes:
I celebrated my birthday with friends, we laughed, then it rained and we danced
"""

result = llm.generate_json(prompt)

print("LLM OUTPUT:")
print(result)

