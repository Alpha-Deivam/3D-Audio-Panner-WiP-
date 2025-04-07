import cv2
import os
from natsort import natsorted

frame_dir = "outputs/detected_frames"
output_video_path = "outputs/detected_video.mp4"

# Get sorted frame paths
frame_files = natsorted([f for f in os.listdir(frame_dir) if f.endswith(".jpg")])
if not frame_files:
    raise Exception("No frames found in output directory!")

# Read first frame to get size
first_frame = cv2.imread(os.path.join(frame_dir, frame_files[0]))
height, width, _ = first_frame.shape

# Create video writer
out = cv2.VideoWriter(output_video_path, cv2.VideoWriter_fourcc(*"mp4v"), 30, (width, height))

# Write frames to video
for frame_file in frame_files:
    frame_path = os.path.join(frame_dir, frame_file)
    frame = cv2.imread(frame_path)
    out.write(frame)

out.release()
print("✅ Video created at:", output_video_path)
