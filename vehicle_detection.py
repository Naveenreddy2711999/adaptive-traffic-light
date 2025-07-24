from ultralytics import YOLO
import cv2

# Load YOLOv8 pre-trained model (nano version for speed)
model = YOLO("yolov8n.pt")

# Load traffic video (replace with your own later)
video_path = "data/sample_traffic.mp4"
cap = cv2.VideoCapture(video_path)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    annotated_frame = results[0].plot()

    # Show the detection
    cv2.imshow("Traffic Vehicle Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
