import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="smart_traffic_db",
    user="postgres",
    password="chincyistopper",
    port="5432"
)

cursor = conn.cursor()

print("Database Connected")