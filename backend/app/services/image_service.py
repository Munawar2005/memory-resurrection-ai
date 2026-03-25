import os
import time
import shutil
import random


class ImageService:

    def __init__(self):
        print("✅ Using Local Images with Variation")

        self.assets_dir = "assets"

    def generate(self, prompt):

        print("⚡ Selecting image based on keyword...")

        try:
            os.makedirs("generated", exist_ok=True)

            prompt = prompt.lower()

            # 🔥 find matching images
            matching_files = []

            for file in os.listdir(self.assets_dir):
                filename = file.lower()

                # match keyword in filename
                if any(word in filename for word in prompt.split()):
                    matching_files.append(os.path.join(self.assets_dir, file))

            # 🔥 if nothing matched → fallback
            if not matching_files:
                matching_files = [
                    os.path.join(self.assets_dir, f)
                    for f in os.listdir(self.assets_dir)
                ]

            # 🔥 RANDOM PICK
            selected_image = random.choice(matching_files)

            file_path = f"generated/frame_{int(time.time())}.jpg"

            shutil.copy(selected_image, file_path)

            print("✅ Selected:", selected_image)

            return file_path

        except Exception as e:
            print("❌ Error:", str(e))
            return None