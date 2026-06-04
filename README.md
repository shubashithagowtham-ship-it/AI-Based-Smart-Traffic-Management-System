# AI-Based Smart Traffic Management System

## Project Description

This project is an AI-powered traffic management system developed using YOLOv8, OpenCV, FastAPI, PostgreSQL, and React.js.

The system detects vehicles from traffic videos, classifies them into different categories such as cars, bikes, buses, and trucks, calculates the traffic congestion level, recommends signal timings, stores the data in a PostgreSQL database, and displays the results on a real-time dashboard.

---

## Features

- Vehicle Detection using YOLOv8
- Vehicle Classification (Cars, Bikes, Buses, Trucks)
- Traffic Congestion Analysis
- Dynamic Signal Time Recommendation
- PostgreSQL Database Integration
- FastAPI Backend APIs
- React Dashboard
- Traffic Analytics Visualization

---

## Technologies Used

### AI & Computer Vision
- YOLOv8
- OpenCV

### Backend
- Python
- FastAPI

### Database
- PostgreSQL

### Frontend
- React.js
- Axios
- Chart.js

---

## How It Works

1. A traffic video is provided as input.
2. YOLOv8 detects vehicles in each frame.
3. Vehicles are classified into cars, bikes, buses, and trucks.
4. The total vehicle count is calculated.
5. Congestion level is determined based on vehicle count.
6. Signal timing is recommended according to congestion.
7. Results are stored in PostgreSQL.
8. FastAPI provides APIs for the frontend.
9. React dashboard displays real-time traffic analytics.

---

## Project Structure

```text
smart-traffic-system

├── ai-engine
│   ├── vehicle_detection.py
│   ├── congestion.py
│   ├── signal_logic.py
│   ├── traffic.mp4
│   └── yolov8n.pt
│
├── backend
│   ├── main.py
│   ├── save_traffic.py
│   └── db_connection.py
│
├── frontend
│   ├── src
│   │   ├── App.js
│   │   └── TrafficChart.js
│
└── README.md
```

---

## Sample Output

```text
Cars = 29
Bikes = 0
Buses = 2
Trucks = 1

Vehicle Count = 32
Congestion = HIGH
Signal Time = 60 seconds
```

---

## Future Improvements

- Live CCTV Camera Integration
- Multi-road Traffic Monitoring
- Traffic Prediction using Machine Learning
- Cloud Deployment
- Mobile Dashboard

---

## What I Learned

- Object Detection using YOLOv8
- Computer Vision with OpenCV
- FastAPI Backend Development
- PostgreSQL Database Integration
- React Dashboard Development
- End-to-End Full Stack AI Application Development

---

## Author

**[Your Name]**

B.E. Computer Science Engineering Student

PES University
