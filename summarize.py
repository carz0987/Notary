# summarize.py

import os
from openai import OpenAI

# Use environment variable for API key (recommended)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def summarize_text(text):
    """
    Summarizes a given transcript using the latest OpenAI Responses API (gpt-4o or gpt-4o-mini).

    Args:
        text (str): The full transcript to summarize.

    Returns:
        str: A concise, structured bullet-point summary.
    """
    try:
        print("🧠 Summarizing transcript with GPT (responses API)...")

        response = client.responses.create(
            model="gpt-4o",
            instructions="You are a helpful assistant that generates clean bullet-point meeting notes from transcripts. Only provide the summary, no other text. Make them short and simple.",
            input=text
        )

        print("✅ Summarization complete.")
        return response.output_text

    except Exception as e:
        print(f"❌ Error during summarization: {e}")
        return "ERROR: Summarization failed."
