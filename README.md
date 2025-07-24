# 🚦 AI-Powered Adaptive Traffic Light System

An intelligent traffic management system that **dynamically adjusts traffic light timings** based on real-time vehicle density using **YOLOv8** for object detection and **SUMO TraCI** for traffic simulation.

---

## 📌 **Features**

✅ Real-time vehicle detection using **YOLOv8**  
✅ Adaptive traffic signal timing based on **vehicle density**  
✅ Integrated with **SUMO TraCI** for traffic simulation  
✅ Graph visualization of **traffic flow improvement**  
✅ Scalable for real-world smart city implementation  

---

## 🖥️ **Tech Stack**

- **Language:** Python 3.13  
- **Computer Vision:** OpenCV, YOLOv8 (Ultralytics)  
- **Traffic Simulation:** SUMO (Simulation of Urban MObility) with TraCI  
- **Data Visualization:** Matplotlib  

---

## 📂 **Project Structure**

adaptive-traffic-light/
│
├── adaptive_traffic_sim.py # Main simulation code
├── vehicle_detection.py # Vehicle detection using YOLOv8
├── traffic_light.sumocfg # SUMO traffic simulation configuration
├── adaptive_graph.png # Graph of traffic optimization results
├── yolov8n.pt # Pre-trained YOLOv8 model
├── requirements.txt # Python dependencies
├── .gitignore # Ignored files (large video, env files)
└── data/
└── sample_traffic.mp4 (Not uploaded due to large file size)

## ⚙️ **Installation**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/Naveenreddy2711999/adaptive-traffic-light.git
cd adaptive-traffic-light
2️⃣ Create a Virtual Environment
python3 -m venv traffic_ai_env
source traffic_ai_env/bin/activate   # For macOS/Linux
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Install SUMO
brew install sumo
Running the Simulation
1.Place a sample traffic video in the data/ folder (e.g., sample_traffic.mp4).
2.Run the adaptive traffic simulation:
python adaptive_traffic_sim.py
3.Press q to stop the simulation.
Results
The system dynamically changes traffic light timing based on real-time vehicle count.
Below is an example graph of traffic flow optimization:

Future Scope
1.Integration with real-time CCTV traffic cameras
2.Deployment in smart cities (e.g., Bangalore Traffic Management)
3.Cloud-based control with IoT integration

Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Author
Naveen Reddy
B.Tech CSE (Data Science) | AI & Computer Vision Enthusiast
