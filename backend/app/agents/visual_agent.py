
# =========================
# visual_agent.py (FINAL IMAGE VERSION)
# =========================

from app.services.image_service import ImageService


class VisualReconstructionAgent:

    def __init__(self):
        self.image_service = ImageService()

        print("🔥 VISUAL AGENT LOADED")
        print("METHODS:", dir(self))

    # =========================
    # MAIN GENERATE FUNCTION
    # =========================
    def generate(self, scene_data):

        prompt = self._build_prompt(scene_data)

        # 🔥 SAFETY: fallback prompt
        if not prompt or prompt.strip() == "":
            print("⚠ Empty prompt, using fallback")
            prompt = "friends celebrating, happy scene"

        print("🎬 Prompt:", prompt)

        # Generate image
        image = self.image_service.generate(prompt)

        print("🖼 IMAGE PATH:", image)

        if not image:
            print("❌ Image generation failed")
            return {
                "type": "error",
                "message": "Image generation failed"
            }

        # 🔥 RETURN IMAGE ONLY
        return {
            "type": "image",
            "image_path": image
        }

    # =========================
    # PROMPT BUILDER
    # =========================
    def _build_prompt(self, data):

        # Safety extraction
        scene = data.get("scene") or "people interacting"
        emotion = data.get("emotion") or "neutral"
        people = data.get("people") or []

        # Emotion → visual style
        emotion_style = {
            "joy": "warm lighting, golden tones, bright atmosphere, smiling faces",
            "sadness": "cool tones, dim lighting, soft shadows, emotional mood",
            "fear": "dark environment, high contrast shadows, suspenseful lighting",
            "anger": "harsh lighting, intense contrast, dramatic shadows",
            "neutral": "balanced lighting, natural colors"
        }

        style = emotion_style.get(emotion, emotion_style["neutral"])

        # People description
        people_text = ""
        if isinstance(people, list) and people:
            roles = ", ".join([p.get("role", "person") for p in people])
            people_text = f"featuring {roles}, "

        # FINAL PROMPT
        prompt = f"""
{scene},
{people_text}
emotion: {emotion},

{style},

cinematic composition,
ultra realistic,
4k resolution,
highly detailed,
sharp focus,

lighting: soft cinematic lighting, volumetric light, natural shadows,
camera: medium shot, depth of field, professional lens, bokeh background,

details: realistic skin texture, natural colors, expressive faces, dynamic pose,
style: film still, hollywood photography, dramatic storytelling,

masterpiece, best quality
"""

        return prompt.strip()

