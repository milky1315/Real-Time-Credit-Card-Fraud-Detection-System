# Real-Time Credit Card Fraud Detection System

## Overview
This project is an end-to-end real-time credit card fraud detection system. It uses machine learning to detect fraudulent transactions and provides a live dashboard for monitoring predictions. The system leverages Kafka for streaming, FastAPI for serving predictions, and React for the dashboard UI.

---

## Architecture

- **Kafka Producer**: Simulates/sends transactions to a Kafka topic (`transactions`).
- **Kafka Consumer**: Listens to the topic, runs the ML model, and sends predictions to FastAPI.
- **FastAPI Backend**: Receives and stores predictions, serves them to the React dashboard.
- **React Dashboard**: Polls FastAPI for predictions and displays them in real time.

```
[Producer] → [Kafka] → [Consumer/Model] → [FastAPI] → [React Dashboard]
```

---

## Directory Structure

```
fraud-detection-system/
│
├── backend/                # Backend FastAPI app, Kafka consumer, Dockerfile
│   ├── app/
│   │   ├── main.py         # FastAPI app
│   │   ├── kafka_consumer.py # Kafka consumer
│   │   ├── send_test_transaction.py # Kafka producer script
│   │   └── wait-for-kafka.sh
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   └── dashboard/          # React dashboard app
│       ├── src/
│       ├── public/
│       ├── package.json
│       └── README.md
│
├── model/                  # Model training and reports
│   ├── train_model.ipynb   # Jupyter notebook for training
│   ├── models/
│   │   └── best_model.pkl  # Trained model
│   ├── reports/            # Evaluation reports, plots
│   └── data/
│       └── creditcard.csv  # Dataset
│
├── docker/                 # Docker Compose and Dockerfiles
│   ├── docker-compose.yml
│   ├── Dockerfile.backend
│   └── Dockerfile.frontend
│
├── data/                   # (Optional) For additional data
│
└── README.md
```

---

## Quick Start (with Docker Compose)

### 1. Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed
- [Docker Compose](https://docs.docker.com/compose/)

### 2. Build and Start All Services
```sh
cd fraud-detection-system/docker
# Build and start Kafka, Zookeeper, backend (FastAPI + consumer)
docker-compose up --build
```
- This will start:
  - Zookeeper
  - Kafka
  - Backend (FastAPI + Kafka consumer)

### 3. Start the React Dashboard
In a new terminal:
```sh
cd ../frontend/dashboard
npm install
npm start
```
- The dashboard will be available at [http://localhost:3000](http://localhost:3000)

### 4. Start the Kafka Producer (Simulate Transactions)
In a new terminal:
```sh
cd ../backend/app
# (Optional) Activate your Python environment
python send_test_transaction.py
```
- This will send random transactions to Kafka, triggering predictions.

---

## Manual Setup (Without Docker)

1. **Start Zookeeper and Kafka** (install locally or use Docker)
2. **Start FastAPI backend**
   ```sh
   cd backend/app
   pip install -r ../../requirements.txt
   uvicorn main:app --reload
   ```
3. **Start Kafka consumer**
   ```sh
   python kafka_consumer.py
   ```
4. **Start React dashboard** (see above)
5. **Run the producer** (see above)

---

## Model Training
- The model is trained in `model/train_model.ipynb` using the [Kaggle ULB Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud).
- The trained model is saved as `model/models/best_model.pkl`.
- Reports and evaluation plots are in `model/reports/`.

---

## Backend API Endpoints
- `POST /predict` — Predict fraud for a single transaction
- `POST /predictions` — Store a prediction (used by consumer)
- `GET /predictions` — Get recent predictions (for dashboard)

---

## Troubleshooting
- **Model file not found in Docker**: Ensure `model/models/best_model.pkl` exists before building the Docker image.
- **Kafka connection errors**: Make sure Kafka and Zookeeper are running and accessible.
- **Dashboard shows 'Failed to fetch'**: Ensure FastAPI backend is running and CORS is enabled.
- **Producer/Consumer connection**: Use `localhost:9092` for local, `kafka:9093` for Docker.

---

## Results & Reports
- Model performance summary: `model/reports/model_performance_summary.csv`
- Evaluation report: `model/reports/evaluation_report.pdf`
- Feature importance: `model/reports/feature_importance_rf.png`
- ROC curve: `model/reports/roc_curve_comparison.png`

---

## References
- [Kaggle ULB Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
- [FastAPI](https://fastapi.tiangolo.com/)
- [confluent-kafka Python](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/)
- [React](https://react.dev/)

---

## License
This project is for educational purposes.
