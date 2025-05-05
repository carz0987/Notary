# transcribe_api.py

from openai import OpenAI

def transcribe_audio_with_api(file_path, model="whisper-1"):
    """
    Transcribes an audio file using OpenAI's updated transcription API.

    Args:
        file_path (str): Path to the audio file.
        model (str): Model to use for transcription. Options include:
                     - "whisper-1"
                     - "gpt-4o-transcribe"
                     - "gpt-4o-mini-transcribe"

    Returns:
        str: The transcribed text.
    """
    client = OpenAI()

    try:
        print(f"🧠 Transcribing using model: whisper-1...")
        with open(file_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"  # you can also use "json" if needed
            )
        print("✅ Transcription complete.")
        return transcription

    except Exception as e:
        print(f"❌ Error during transcription: {e}")
        return "ERROR: Transcription failed."
