import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Load data
data = pd.read_csv("vehicle_counts.csv")

# Create folder if not exists
output_folder = "adaptive_graphs"
os.makedirs(output_folder, exist_ok=True)

# Unique timestamp for graph naming
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# -------------------------
# Graph 1: Vehicles Detected Over Time
# -------------------------
plt.figure(figsize=(8, 5))
plt.plot(data['Time'], data['Vehicles'], color='blue', marker='o')
plt.title("Vehicles Detected Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Vehicles Detected")
plt.grid(True)
plt.savefig(f"{output_folder}/vehicles_over_time_{timestamp}.png")
plt.close()

# -------------------------
# Graph 2: Green Light Duration Over Time
# -------------------------
plt.figure(figsize=(8, 5))
plt.plot(data['Time'], data['GreenLightDuration'], color='green', marker='o')
plt.title("Green Light Duration Over Time")
plt.xlabel("Time (s)")
plt.ylabel("Green Light Duration (s)")
plt.grid(True)
plt.savefig(f"{output_folder}/green_light_duration_{timestamp}.png")
plt.close()

# -------------------------
# Graph 3: Vehicles vs Green Light Duration
# -------------------------
plt.figure(figsize=(8, 5))
plt.scatter(data['Vehicles'], data['GreenLightDuration'], color='red')
plt.title("Vehicles vs Green Light Duration")
plt.xlabel("Vehicles Detected")
plt.ylabel("Green Light Duration (s)")
plt.grid(True)
plt.savefig(f"{output_folder}/vehicles_vs_green_light_{timestamp}.png")
plt.close()

print(f"✅ Graphs saved in '{output_folder}' folder with timestamp: {timestamp}")
