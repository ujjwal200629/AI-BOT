from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Use your actual ElevenLabs API key here or load from .env
ELEVEN_API_KEY = os.getenv("ELEVEN_API_KEY")  # ✅ Make sure .env file has this line: ELEVEN_API_KEY=your_key_here

@app.post("/speak-text/")
def speak_text(text: str = Form(...), voice_id: str = Form(...)):
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": ELEVEN_API_KEY,
        "Content-Type": "application/json"
    }

    body = {
        "text": text,
        "model_id": "eleven_monolingual_v1",  # Default English model
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
        }
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        with open("output.mp3", "wb") as f:
            f.write(response.content)
        return FileResponse("output.mp3", media_type="audio/mpeg")
    else:
        return {"error": response.json()}
