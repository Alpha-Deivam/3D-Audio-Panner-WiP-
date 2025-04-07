from pydub import AudioSegment
import pickle
import numpy as np

# Load the audio from the original video
audio = AudioSegment.from_file("assets/test_clip.mp4", format="mp4")

# Load object positions
with open("outputs/object_positions.pkl", "rb") as f:
    positions = pickle.load(f)

duration_ms = len(audio)
frame_rate = 30
frame_duration = 1000 / frame_rate

pan_audio = AudioSegment.empty()
for frame in range(int(duration_ms // frame_duration)):
    start = int(frame * frame_duration)
    end = int(start + frame_duration)
    segment = audio[start:end]

    frame_objects = [p for p in positions if p[0] == frame]
    if frame_objects:
        avg_x = np.mean([x[2] for x in frame_objects])
        pan = (avg_x - 320) / 320  # Normalize x to [-1, 1] for 640px width
    else:
        pan = 0

    panned = segment.pan(pan)
    pan_audio += panned

# Export the processed audio
pan_audio.export("outputs/processed_audio.wav", format="wav")
print("✅ Audio panning complete.")
