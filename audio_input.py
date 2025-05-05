# audio_input.py

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write
import threading
import sys

recording = True

def _stop_recording_listener():
    global recording
    input("⏹️ Press ENTER to stop recording...\n")
    recording = False

def record_audio(filename="audio_input.wav", fs=44100):
    """
    Records audio until the user manually stops by pressing ENTER.
    Saves it to a .wav file.
    """
    global recording
    recording = True

    print("🎙️ Recording...")

    # Start a thread to wait for user input
    listener_thread = threading.Thread(target=_stop_recording_listener)
    listener_thread.start()

    audio_data = []

    def callback(indata, frames, time, status):
        if recording:
            audio_data.append(indata.copy())
        else:
            raise sd.CallbackStop()

    try:
        with sd.InputStream(samplerate=fs, channels=1, callback=callback):
            while recording:
                sd.sleep(100)  # Wait a bit while streaming
    except sd.CallbackStop:
        pass

    print("✅ Recording stopped.")
    audio_array = np.concatenate(audio_data, axis=0)
    write(filename, fs, audio_array)
    print(f"🎧 Audio saved to: {filename}")
    return filename
