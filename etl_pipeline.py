import psycopg2
import paho.mqtt.client as mqtt
import json

DB_PARAMS = {
    "dbname": "1",
    "user": "2",
    "password": "3",
    "host": "4",
    "port": 5432
}

def on_message(client, userdata, message):
    data = json.loads(message.payload.decode("utf-8"))
    insert_data(data)

def insert_data(data):
    try:
        connection = psycopg2.connect(**DB_PARAMS)
        cursor = connection.cursor()
        cursor.execute("""
        INSERT INTO sensor_data (sensor_id, temperature, humidity, vibration)
        VALUES (%s, %s, %s, %s);
        """, (data["sensor_id"], data["temperature"], data["humidity"], data["vibration"]))
        connection.commit()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_message = on_message
    client.connect("localhost", 1883, 60)
    client.subscribe("iot/sensor_data")
    client.loop_forever()
