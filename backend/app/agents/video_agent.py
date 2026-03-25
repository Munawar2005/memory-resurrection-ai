
# =========================
# video_agent.py (FINAL FIXED VERSION)
# =========================

import os
import subprocess


class VideoAgent:

    def __init__(self):
        pass

    def generate_video(self, image_path, emotion="neutral"):

        try:
            if not image_path or not os.path.exists(image_path):
                print("❌ Image not found")
                return None

            os.makedirs("generated", exist_ok=True)

            # ✅ FIXED PATH HANDLING
            filename = os.path.basename(image_path).replace(".png", ".mp4")
            video_path = os.path.join("generated", filename)

            # Create temporary file list
            list_file = "generated/list.txt"

            with open(list_file, "w") as f:
                for _ in range(30):  # 3 sec video (30 frames)
                    f.write(f"file '{image_path}'\n")

            # FFmpeg command
            cmd = [
                "ffmpeg",
                "-y",
                "-f", "concat",
                "-safe", "0",
                "-i", list_file,
                "-vf", "fps=10,format=yuv420p",
                video_path
            ]

            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            print("✅ Video created:", video_path)

            return video_path

        except Exception as e:
            print("❌ Video Error:", str(e))
            return None

