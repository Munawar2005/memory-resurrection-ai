class PeopleDetectorAgent:

    def __init__(self, llm=None):
        self.llm = llm

    def detect_people(self, text: str):

        if self.llm:
            return self._llm_detect(text)

        return self._fallback(text)

    def _llm_detect(self, text):
        return {"people": [{"role": "Person", "character_id": 1, "face_provided": False}]}

    def _fallback(self, text):
        return {"people": [{"role": "Person", "character_id": 1, "face_provided": False}]}
