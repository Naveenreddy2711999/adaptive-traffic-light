# 🚦 AI-Powered Adaptive Traffic Light System with Real-Time Dashboard

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)  
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Object_Detection-green?logo=opencv)](https://github.com/ultralytics/ultralytics)  
[![SUMO](https://img.shields.io/badge/SUMO-Traffic_Simulation-orange?logo=linux)](https://www.eclipse.org/sumo/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-lightgrey?logo=open-source-initiative)](LICENSE)

An intelligent traffic management system that dynamically adjusts traffic light timings based on real-time vehicle density using YOLOv8 for object detection and SUMO TraCI for traffic simulation, now integrated with a Flask-based dashboard for real-time monitoring.


---

## ✨ Features

Problem Statement

❌ Long waiting times during low traffic

❌ Traffic jams during peak hours

❌ No priority for emergency vehicles

❌ No centralized monitoring

---


✅ Solution

This AI-powered system:

Detects vehicles in real-time (CCTV / video feeds)

Optimizes traffic light timings to reduce congestion

Gives priority clearance to emergency vehicles

Provides a real-time dashboard for monitoring


---

🔥 Features

✔ Real-time vehicle detection using YOLOv8 + OpenCV

✔ Adaptive traffic signal timing based on vehicle density

✔ Emergency vehicle detection & priority clearance

✔ Integrated with SUMO TraCI for traffic simulation

✔ Flask-based dashboard for live monitoring

✔ Graph visualization of traffic flow improvements

✔ Scalable for smart city deployment

---
🛠 Tech Stack


| Category               | Technology                                     |
| ---------------------- | ---------------------------------------------- |
| **Language**           | Python 3.13                                    |
| **Computer Vision**    | OpenCV, YOLOv8 (Ultralytics)                   |
| **Traffic Simulation** | SUMO (Simulation of Urban MObility) with TraCI |
| **Data Visualization** | Matplotlib, Plotly                             |
| **Dashboard**          | Flask + Bootstrap                              |
| **Version Control**    | Git & GitHub                                   |


---

## 📂 Project Structure

adaptive-traffic-light/

│
├── adaptive_traffic_sim.py      
├── vehicle_detection.py         
├── traffic_light.sumocfg         
├── yolov8n.pt                   
├── app.py                       
├── requirements.txt              
├── LICENSE                       
├── README.md                   
│
├── static/                      
│   └── style.css                
│
├── templates/                    
│   └── dashboard.html            
│
├── data/                        
│
└── adaptive_graph.png         

---


⚙️ Installation

1️⃣ Clone the Repository

git clone https://github.com/Naveenreddy2711999/adaptive-traffic-light.git
cd adaptive-traffic-light


2️⃣ Create & Activate Virtual Environment

python3 -m venv traffic_ai_env
source traffic_ai_env/bin/activate    # MacOS/Linux


3️⃣ Install Dependencies

pip install -r requirements.txt


4️⃣ Install SUMO

brew install sumo

---



🚀 Running the Project

1. Start Adaptive Traffic Light Simulation

    python adaptive_traffic_sim.py

2. Start Flask Dashboard
   
    python app.py

4. Access Dashboard
   
    Open in your browser:
        http://127.0.0.1:5000


You will see:

Live vehicle detection video

Real-time traffic count & signal status

Emergency vehicle alerts

---



📊 How It Works (Step by Step)

YOLOv8 detects vehicles & emergency vehicles from video or live webcam.

Vehicle counts are analyzed to determine green light duration dynamically.

Emergency vehicles get priority, forcing immediate green signal on their lane.

Traffic data is saved in vehicle_counts.csv.

Graphs are generated for traffic trends (generate_graphs.py).

Flask dashboard displays live signal timing & vehicle statistics.

---


📈 Results

The system dynamically changes traffic light timing based on real-time vehicle count.
Below is an example graph of traffic optimization:

(adaptive_graph.png)

---


🔮Future Scope

✅ Integration with IoT-based traffic signals

✅ Use of Reinforcement Learning for improved predictions

✅ Cloud dashboard for city-wide traffic monitoring

✅ Integration with Google Maps API for route suggestions

---


📜 License

This project is licensed under the MIT License.

See the LICENSE file for details.



    
