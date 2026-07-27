import os
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("GEMINI_API_KEY"))
class Setting:
    GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")

settings = Setting()