import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="smart_traffic_db",
        user="postgres",
        password="chincyistopper",
        port="5432"
    )

    print("Connected successfully!")

    conn.close()

except Exception as e:
    print("Error:", e)