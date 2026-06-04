from db_connection import cursor, conn

def save_data(
    vehicle_count,
    congestion,
    signal_time,
    cars,
    bikes,
    buses,
    trucks
):
    cursor.execute(
        """
        INSERT INTO traffic_logs
        (
            vehicle_count,
            congestion_level,
            signal_time,
            cars,
            bikes,
            buses,
            trucks
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """,
        (
            vehicle_count,
            congestion,
            signal_time,
            cars,
            bikes,
            buses,
            trucks
        )
    )

    conn.commit()

    print("Data Saved")