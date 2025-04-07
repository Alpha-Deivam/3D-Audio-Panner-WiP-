from ultralytics import YOLO
import cv2
import os
import pickle

model = YOLO("yolov8n.pt")

video_path = "assets/test_clip.mp4"
output_dir = "outputs/detected_frames"
os.makedirs(output_dir, exist_ok=True)


cap = cv2.VideoCapture(video_path)
frame_num = 0
positions = []

print("Opened video:", cap.isOpened())

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for r in results:
        for box in r.boxes:
            cls = int(box.cls.item())
            x_center = int((box.xyxy[0][0] + box.xyxy[0][2]) / 2)
            positions.append((frame_num, cls, x_center))

    annotated = results[0].plot()
    cv2.imwrite(f"{output_dir}/frame_{frame_num:04d}.jpg", annotated)
    frame_num += 1

# Release the video
cap.release()

# Print the number of positions collected
print(f"Total objects detected across all frames: {len(positions)}")

# Absolute path for saving the pickle
output_pickle_path = os.path.abspath(os.path.join(output_dir, "object_positions.pkl"))
print(f"Attempting to save pickle to: {output_pickle_path}")

try:
    with open(output_pickle_path, "wb") as f:
        pickle.dump(positions, f)
    print("✅ Pickle saved successfully.")
except Exception as e:
    print("❌ Error saving pickle:", e)