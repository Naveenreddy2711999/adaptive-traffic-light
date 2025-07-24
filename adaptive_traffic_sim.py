import cv2
from ultralytics import YOLO
import time
import matplotlib.pyplot as plt

# Load YOLO model
model = YOLO("yolov8n.pt")

# Load traffic video
video_path = "data/sample_traffic.mp4"  # ✅ Make sure this file exists
cap = cv2.VideoCapture(video_path)

# Traffic light timing variables
min_time, max_time = 5, 20  # Green light between 5s and 20s

# Data for graph
vehicle_data = []
green_light_data = []

print("Adaptive traffic light simulation started... Press 'q' to quit.")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Detect vehicles
    results = model(frame)
    vehicle_count = 0
    for r in results:
        for c in r.boxes.cls:
            # COCO class IDs for cars, buses, trucks, motorbikes
            if int(c) in [2, 3, 5, 7]:
                vehicle_count += 1

    # Adjust green light duration based on vehicle count
    green_light_time = max(min_time, min(max_time, int(vehicle_count * 1.5)))

    # Store data for graph
    vehicle_data.append(vehicle_count)
    green_light_data.append(green_light_time)

    # Display simulation info
    annotated_frame = results[0].plot()
    cv2.putText(annotated_frame, f"Vehicles: {vehicle_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(annotated_frame, f"Green Light: {green_light_time}s", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    cv2.imshow("Adaptive Traffic Light Simulation", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Print for debugging
    print(f"Vehicles detected: {vehicle_count} → Green Light: {green_light_time}s")
    time.sleep(0.1)

cap.release()
cv2.destroyAllWindows()

# Plot graph after simulation ends
plt.figure(figsize=(6, 4))
plt.plot(vehicle_data, green_light_data, marker='o', color='b')
plt.title("Vehicle Count vs Green Light Time")
plt.xlabel("Vehicle Count")
plt.ylabel("Green Light Time (s)")
plt.grid(True)
plt.savefig("adaptive_graph.png")  # ✅ Saved for report
plt.show()

print("✅ Graph saved as 'adaptive_graph.png'")
