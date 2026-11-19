FROM python:3.12-slim

WORKDIR /app

COPY backend/app/ ./app/
COPY model/models/best_model.pkl ./model/models/best_model.pkl
COPY backend/app/wait-for-kafka.sh /wait-for-kafka.sh
RUN chmod +x /wait-for-kafka.sh

# Install netcat for wait script
RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir confluent-kafka joblib numpy scikit-learn xgboost requests

CMD ["/wait-for-kafka.sh", "kafka", "python", "app/kafka_consumer.py"]