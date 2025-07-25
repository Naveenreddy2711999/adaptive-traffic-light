import cv2
import pandas as pd
import os
from ultralytics import YOLO
from datetime import datetime

# ✅ Ensure logs folder exists
os.makedirs("logs", exist_ok=True)

# ✅ Load YOLOv8 model (pretrained on COCO, detects 80 classes including emergency vehicles)
model = YOLO("models/yolov8n.pt")

# ✅ Class names for COCO dataset
class_names = model.names

# ✅ Emergency vehicle keywords
emergency_keywords = ["ambulance", "fire", "police", "rescue"]

# ✅ Open video (replace with 0 for live webcam)
video_path = "data/test_video.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"❌ Could not open video: {video_path}")
    exit()

# ✅ CSV log setup
csv_path = "logs/vehicle_counts.csv"
if not os.path.exists(csv_path):
    pd.DataFrame(columns=["timestamp", "vehicle", "count", "emergency"]).to_csv(csv_path, index=False)

print("✅ Vehicle Detection Started... Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("✅ Video Finished.")
        break

    # ✅ Detect objects
    results = model(frame, stream=True)

    vehicle_count = {}
    emergency_detected = False

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = class_names[cls_id]
            conf = float(box.conf[0])

            if conf < 0.4:  # Ignore low-confidence detections
                continue

            # ✅ Count vehicles
            vehicle_count[label] = vehicle_count.get(label, 0) + 1

            # ✅ Emergency detection
            if any(e in label.lower() for e in emergency_keywords):
                emergency_detected = True

            # ✅ Draw boxes
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            color = (0, 0, 255) if emergency_detected else (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # ✅ Display on screen
    cv2.imshow("Vehicle Detection", frame)

    # ✅ Log vehicle count
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    for vehicle, count in vehicle_count.items():
        df = pd.read_csv(csv_path)
        new_row = pd.DataFrame([{
            "timestamp": timestamp,
            "vehicle": vehicle,
            "count": count,
            "emergency": emergency_detected
        }])
        df = pd.concat([df, new_row], ignore_index=True)
        df.to_csv(csv_path, index=False)

    # ✅ Quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
print("✅ Detection Completed. Logs saved in logs/vehicle_counts.csv")
