import os
from dotenv import load_dotenv

load_dotenv()

print("FAL KEY:", os.getenv("FAL_API_KEY"))