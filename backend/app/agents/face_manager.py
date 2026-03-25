import json
import os

class FaceManager:

    def __init__(self):
        self.file = "app/data/face_map.json"
        self.faces = self._load()

    def _load(self):
        if not os.path.exists(self.file):
            return {}
        return json.load(open(self.file))

    def get_face(self, character_id):
        return self.faces.get(str(character_id))
