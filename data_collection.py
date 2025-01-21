from modbus_tk import modbus_tcp
import paho.mqtt.client as mqtt
import time
import random

BROKER = "1"
TOPIC = "iot/sensor_data"

def mock_sensor_data():
    """Simulates sensor data for demonstration purposes."""
    return {
        "sensor_id": "sensor_001",
        "temperature": round(random.uniform(20.0, 30.0), 2),
        "humidity": round(random.uniform(40.0, 60.0), 2),
        "vibration": round(random.uniform(0.1, 1.0), 2),
    }

def publish_data():
    client = mqtt.Client()
    client.connect(BROKER, 1883, 60)
    while True:
        data = mock_sensor_data()
        client.publish(TOPIC, str(data))
        print(f"Published: {data}")
        time.sleep(5)

if __name__ == "__main__":
    publish_data()
