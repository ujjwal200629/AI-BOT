from pydub import AudioSegment
import speech_recognition as sr
import os

def transcribe_audio(file_path):
    recognizer = sr.Recognizer()

    # Step 1: Convert mp3 to wav if needed
    if file_path.endswith(".mp3"):
        sound = AudioSegment.from_mp3(file_path)
        file_path_wav = file_path.replace(".mp3", ".wav")
        sound.export(file_path_wav, format="wav")
        file_path = file_path_wav

    # Step 2: Transcribe audio
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I couldn't understand the audio."
    except sr.RequestError:
        return "Error connecting to the speech recognition service."
