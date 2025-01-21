import psycopg2

def setup_database():
    connection = psycopg2.connect(
        dbname="1",
        user="2",
        password="3",
        host="4",
        port=5432
    )
    cursor = connection.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sensor_data (
        id SERIAL PRIMARY KEY,
        sensor_id VARCHAR(50),
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        temperature FLOAT,
        humidity FLOAT,
        vibration FLOAT
    );
    """)
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    setup_database()
