from confluent_kafka import Producer
import json
import time
import random

conf = {'bootstrap.servers': 'localhost:9092'}  # Use 'kafka:9092' if running inside Docker
producer = Producer(conf)
topic = "transactions"

def generate_transaction():
    # Replace with your actual feature names and ranges
    return {
        "V1": random.uniform(-2, 2),
        "V2": random.uniform(-2, 2),
        "V3": random.uniform(-2, 2),
        "V4": random.uniform(-2, 2),
        "V5": random.uniform(-2, 2),
        "V6": random.uniform(-2, 2),
        "V7": random.uniform(-2, 2),
        "V8": random.uniform(-2, 2),
        "V9": random.uniform(-2, 2),
        "V10": random.uniform(-2, 2),
        "V11": random.uniform(-2, 2),
        "V12": random.uniform(-2, 2),
        "V13": random.uniform(-2, 2),
        "V14": random.uniform(-2, 2),
        "V15": random.uniform(-2, 2),
        "V16": random.uniform(-2, 2),
        "V17": random.uniform(-2, 2),
        "V18": random.uniform(-2, 2),
        "V19": random.uniform(-2, 2),
        "V20": random.uniform(-2, 2),
        "V21": random.uniform(-2, 2),
        "V22": random.uniform(-2, 2),
        "V23": random.uniform(-2, 2),
        "V24": random.uniform(-2, 2),
        "V25": random.uniform(-2, 2),
        "V26": random.uniform(-2, 2),
        "V27": random.uniform(-2, 2),
        "V28": random.uniform(-2, 2),
        "Amount_scaled": random.uniform(0, 1)
    }

def delivery_report(err, msg):
    if err is not None:
        print(f"Delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

if __name__ == "__main__":
    while True:
        transaction = generate_transaction()
        producer.produce(topic, value=json.dumps(transaction), callback=delivery_report)
        producer.flush()
        time.sleep(2)  # Send a transaction every 2 seconds