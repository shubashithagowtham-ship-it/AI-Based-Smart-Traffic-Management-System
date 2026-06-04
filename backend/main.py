from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="smart_traffic_db",
        user="postgres",
        password="chincyistopper",
        port="5432"
    )

@app.get("/")
def home():
    return {"message": "Traffic Backend Running"}

@app.get("/latest-traffic")
def latest_traffic():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT vehicle_count,
       congestion_level,
       signal_time,
       cars,
       bikes,
       buses,
       trucks,
       created_at
        FROM traffic_logs
        ORDER BY id DESC
        LIMIT 1
    """)

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row:
        return {
    "vehicle_count": row[0],
    "congestion": row[1],
    "signal_time": row[2],
    "cars": row[3],
    "bikes": row[4],
    "buses": row[5],
    "trucks": row[6],
    "timestamp": str(row[7])
}
        

    return {"message": "No data found"}

@app.get("/traffic-history")
def traffic_history():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT vehicle_count
        FROM traffic_logs
        ORDER BY id DESC
        LIMIT 10
    """)

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [row[0] for row in rows]