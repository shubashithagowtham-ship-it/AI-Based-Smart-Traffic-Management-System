import sys
import os
import cv2
from ultralytics import YOLO

sys.path.append(os.path.abspath("../backend"))

from save_traffic import save_data
from congestion import congestion_level
from signal_logic import calculate_signal_time

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("traffic.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video finished")
        break

    results = model(frame)

    cars = 0
    motorcycles = 0
    buses = 0
    trucks = 0

    for result in results:
        for box in result.boxes:

            cls = int(box.cls[0])

            # YOLO COCO classes
            if cls == 2:      # car
                cars += 1

            elif cls == 3:    # motorcycle
                motorcycles += 1

            elif cls == 5:    # bus
                buses += 1

            elif cls == 7:    # truck
                trucks += 1

    vehicle_count = (
        cars +
        motorcycles +
        buses +
        trucks
    )

    congestion = congestion_level(vehicle_count)

    signal_time = calculate_signal_time(vehicle_count)

    print(
        f"Cars={cars} | "
        f"Bikes={motorcycles} | "
        f"Buses={buses} | "
        f"Trucks={trucks}"
    )

    print(
        f"Vehicles={vehicle_count} | "
        f"Congestion={congestion} | "
        f"Signal={signal_time}"
    )

    save_data(
    vehicle_count,
    congestion,
    signal_time,
    cars,
    motorcycles,
    buses,
    trucks
)
    

    annotated_frame = results[0].plot()

    cv2.putText(
        annotated_frame,
        f"Vehicles: {vehicle_count}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Cars:{cars} Bikes:{motorcycles}",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.putText(
        annotated_frame,
        f"Bus:{buses} Truck:{trucks}",
        (20, 130),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("Traffic Detection", annotated_frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()