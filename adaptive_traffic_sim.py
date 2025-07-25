import pandas as pd
import time
import os

CSV_PATH = "logs/vehicle_counts.csv"

# ✅ Default green light time in seconds
DEFAULT_GREEN = 20
MAX_GREEN = 60
MIN_GREEN = 10

print("✅ Adaptive Traffic Light Simulation Started... Press Ctrl+C to stop.")

def calculate_green_time(vehicle_count):
    """
    Adaptive logic:
    - Base time = DEFAULT_GREEN
    - +1 second for every 2 extra vehicles
    - Emergency vehicles -> Max green time immediately
    """
    green_time = DEFAULT_GREEN + (vehicle_count // 2)
    return min(max(green_time, MIN_GREEN), MAX_GREEN)

try:
    while True:
        if os.path.exists(CSV_PATH):
            df = pd.read_csv(CSV_PATH)

            if not df.empty:
                # ✅ Get latest entry
                last_row = df.iloc[-1]
                vehicle = last_row["vehicle"]
                count = int(last_row["count"])
                emergency = last_row["emergency"]

                if emergency:
                    print(f"🚨 Emergency detected ({vehicle})! Switching to GREEN immediately.")
                    green_time = MAX_GREEN
                else:
                    green_time = calculate_green_time(count)

                print(f"🟢 Green Light ON for {vehicle} | Vehicles: {count} | Duration: {green_time} sec")
                time.sleep(green_time)

                print(f"🔴 Red Light ON for {vehicle} | Duration: 5 sec")
                time.sleep(5)
            else:
                print("⚠️ No data in CSV yet. Waiting...")
                time.sleep(2)
        else:
            print("❌ CSV file not found. Run vehicle_detection.py first!")
            break

except KeyboardInterrupt:
    print("\n✅ Adaptive Traffic Simulation Stopped.")
