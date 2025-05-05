# ui/app.py

import os
import shutil
import tempfile
import gradio as gr
from pydub import AudioSegment
from openai import OpenAI
from summarize import summarize_text

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
SUPPORTED_EXTENSIONS = (".mp3", ".wav", ".mp4", ".m4a", ".webm")
NOTES_FILE = "./output/note_summary.txt"

# 🔧 Convert any input file to .mp3 using pydub
def convert_to_mp3(original_path):
    audio = AudioSegment.from_file(original_path)
    temp_dir = tempfile.mkdtemp()
    mp3_path = os.path.join(temp_dir, "converted.mp3")
    audio.export(mp3_path, format="mp3")
    return mp3_path, temp_dir

def process_mic_input(mic_file):
    if not mic_file:
        return "❌ Please record some audio.", None
    return process_transcription(mic_file)

def process_file_upload(upload_file):
    if not upload_file:
        return "❌ Please upload a valid file.", None
    if not upload_file.lower().endswith(SUPPORTED_EXTENSIONS):
        return f"❌ Unsupported file type. Supported: {', '.join(SUPPORTED_EXTENSIONS)}", None
    return process_transcription(upload_file)

def process_transcription(file_path):
    try:
        # Convert to mp3
        mp3_path, temp_dir = convert_to_mp3(file_path)

        with open(mp3_path, "rb") as audio_file:
            transcription = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )

        transcript = transcription
        summary = summarize_text(transcript)

        os.makedirs("output", exist_ok=True)
        with open(NOTES_FILE, "w", encoding="utf-8") as f:
            f.write("📝 Transcript:\n" + transcript + "\n\n")
            f.write("📌 Summary:\n" + summary)

        shutil.rmtree(temp_dir)
        return summary, NOTES_FILE

    except Exception as e:
        return f"❌ Error: {e}", None

def ask_notes(question):
    if not os.path.exists(NOTES_FILE):
        return "⚠️ Please transcribe a note first."

    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        notes_text = f.read()

    prompt = f"""
You are an AI assistant. Only use the information from the following notes to answer questions. 
If the answer is not clearly in the notes, say: "That information is not available in the notes."

### Notes:
{notes_text}

### Question:
{question}
"""

    try:
        response = client.responses.create(
            model="gpt-4o",
            instructions="Answer only based on the notes provided. Do not invent or guess.",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        return f"❌ Error during question answering: {e}"

# 🌐 Gradio Web Interface
with gr.Blocks(title="Notary") as app:
    gr.Markdown("# 📝 Notary")
    gr.Markdown("Record, upload, summarize — and ask questions based on your notes.")

    with gr.Tabs():
        with gr.TabItem("🎤 Record Audio"):
            mic_input = gr.Audio(sources=["microphone"], type="filepath", label="Record from your microphone")
            mic_summary = gr.Textbox(label="📌 Summary (Transcript is in downloadable file)")
            mic_file = gr.File(label="⬇️ Download Transcript + Summary")
            mic_button = gr.Button("Transcribe & Summarize")
            mic_button.click(fn=process_mic_input, inputs=[mic_input], outputs=[mic_summary, mic_file])

        with gr.TabItem("📁 Upload File"):
            file_input = gr.File(file_types=list(SUPPORTED_EXTENSIONS), type="filepath", label="Upload audio or video")
            file_summary = gr.Textbox(label="📌 Summary (Transcript is in downloadable file)")
            file_output = gr.File(label="⬇️ Download Transcript + Summary")
            file_button = gr.Button("Transcribe & Summarize")
            file_button.click(fn=process_file_upload, inputs=[file_input], outputs=[file_summary, file_output])

        with gr.TabItem("💬 Ask Your Notes"):
            question = gr.Textbox(label="❓ Ask a question about your notes")
            answer = gr.Textbox(label="🧠 AI Answer", lines=6)
            ask_button = gr.Button("Ask")
            ask_button.click(fn=ask_notes, inputs=[question], outputs=[answer])

app.launch(inbrowser=True)
