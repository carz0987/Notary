# main.py

import os
from audio_input import record_audio
from transcribe_api import transcribe_audio_with_api
from summarize import summarize_text

SUPPORTED_FORMATS = ('.wav', '.mp3', '.m4a', '.mp4', '.webm')

def main():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("❌ Error: OPENAI_API_KEY environment variable is not set.")
        return

    print("🎙️ Welcome to the AI Note Assistant")
    print("1. Record new audio")
    print("2. Upload existing audio file")
    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "1":
        # Manual stop recording
        audio_file = record_audio()
    elif choice == "2":
        file_path = input("Enter path to your audio file (.wav, .mp3, etc.): ").strip()
        if not os.path.isfile(file_path):
            print("❌ Error: File does not exist.")
            return
        if not file_path.lower().endswith(SUPPORTED_FORMATS):
            print("❌ Error: Unsupported file type.")
            return
        audio_file = file_path
    else:
        print("❌ Invalid option.")
        return

    # Transcribe
    transcript = transcribe_audio_with_api(audio_file, model="whisper-1")  # or gpt-4o-transcribe
    print("\n📝 Transcript:\n")
    print(transcript)

    # Summarize
    summary = summarize_text(transcript)
    print("\n📌 Summary:\n")
    print(summary)

if __name__ == "__main__":
    main()
