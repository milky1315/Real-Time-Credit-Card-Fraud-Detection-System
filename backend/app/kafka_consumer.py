from confluent_kafka import Consumer
import json
import joblib
import numpy as np
import os
import requests

MODEL_PATH = os.path.join(os.path.dirname(__file__), '../../model/models/best_model.pkl')
model = joblib.load(MODEL_PATH)

conf = {
    'bootstrap.servers': 'kafka:9093',  # Use 'kafka:9093' if running in Docker, 'localhost:9092' if local
    'group.id': 'fraud-detector-group',
    'auto.offset.reset': 'earliest'
}

consumer = Consumer(conf)
topic = "transactions"
transaction_id = 0

def process_transaction(transaction_dict):
    global transaction_id
    input_data = np.array([list(transaction_dict.values())])
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data)[0][1] if hasattr(model, 'predict_proba') else None
    print(f"Prediction: {prediction}, Probability: {proba}")

    # POST to FastAPI
    result = {
        "transaction_id": transaction_id,
        "prediction": int(prediction),
        "probability": float(proba) if proba is not None else 0.0
    }
    try:
        # Use 'fastapi:8000' if running in Docker Compose, 'localhost:8000' if local
        requests.post("http://fastapi:8000/predictions", json=result)
    except Exception as e:
        print("Failed to POST to FastAPI:", e)
    transaction_id += 1

def consume_messages():
    consumer.subscribe([topic])
    print(f"Listening for messages on topic '{topic}'...")
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue
            transaction_data = json.loads(msg.value().decode('utf-8'))
            process_transaction(transaction_data)
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    consume_messages() 