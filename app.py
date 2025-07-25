from flask import Flask, render_template
import pandas as pd
import os

app = Flask(__name__)
CSV_PATH = "logs/vehicle_counts.csv"

@app.route("/")
def index():
    if os.path.exists(CSV_PATH):
        try:
            df = pd.read_csv(CSV_PATH)
            if not df.empty:
                last_row = df.iloc[-1]
                vehicle = last_row["vehicle"]
                count = int(last_row["count"])
                emergency = last_row["emergency"]
                timestamp = last_row["timestamp"]

                light_status = "GREEN" if emergency or count > 5 else "RED"

                return render_template(
                    "index.html",
                    vehicle=vehicle,
                    count=count,
                    emergency=emergency,
                    light_status=light_status,
                    timestamp=timestamp
                )
        except:
            pass
    return render_template("index.html", vehicle="N/A", count=0, emergency=False, light_status="RED", timestamp="N/A")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)

