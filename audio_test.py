from pydub import AudioSegment
from pydub.utils import which
import os
print("ffmpeg path:", which("ffmpeg"))
print("Current working directory:", os.getcwd())
print("Input file exists:", os.path.exists("test1.mp3"))
print("Script started")
# Load an audio file (can be mp3, wav, etc.)
audio = AudioSegment.from_file("test1.mp3")  # or "input.wav", etc.

# Set frame rate (sample rate) and sample width (bit depth)
audio = audio.set_frame_rate(44100)
audio = audio.set_sample_width(2)  # 2 bytes = 16 bits

# Export as 16-bit, 44.1kHz WAV
audio.export("outtest1.wav", format="wav")

