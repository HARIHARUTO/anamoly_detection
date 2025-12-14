md
# 🔍 Real-Time Anomaly Detection Using Isolation Forest

![Python](https://img.shields.io/badge/python-3.13%2B-blue)
![ML](https://img.shields.io/badge/model-Isolation%20Forest-purple)
![Status](https://img.shields.io/badge/status-working-success)
![License](https://img.shields.io/badge/license-MIT-green)

A hands-on machine learning project that performs **real-time anomaly detection on application logs** using an **unsupervised Isolation Forest model**.

This project simulates live log generation, trains a machine learning model to learn normal behavior, and detects abnormal patterns as logs stream in.

---

## 🚀 Features

- ✅ Real-time log simulation
- ✅ Unsupervised anomaly detection (no labeled data)
- ✅ Isolation Forest model
- ✅ Feature extraction from logs
- ✅ Real-time anomaly monitoring
- ✅ Model persistence using Joblib
- ✅ Rule-based alert filtering to reduce false positives

---

## 📂 Project Structure

```

anamoly_detection/
│
├── logs/
│   └── app.log                      # Generated application logs
│
├── models/
│   └── isolation_forest_model.joblib
│
├── logs_simulation.py               # Generates synthetic logs
├── model_training.py                # Trains the Isolation Forest model
├── realtime_detection.py            # Detects anomalies in real time
├── README.md
└── LICENSE

````

---

## ⚙️ Workflow Overview

### 1️⃣ Log Simulation
`logs_simulation.py` continuously generates synthetic logs containing:
- timestamp
- request latency
- HTTP status code
- application route

A small percentage of logs are intentionally abnormal (high latency or server errors).

---

### 2️⃣ Model Training
`model_training.py`:
- loads generated logs
- extracts numerical features
- trains an **Isolation Forest** model
- saves the trained model for reuse

---

### 3️⃣ Real-Time Detection
`realtime_detection.py`:
- loads the trained model
- monitors the log file continuously
- predicts anomalies as new logs appear
- applies rule-based filtering for meaningful alerts

---

## ▶️ How to Run

### Step 1: Generate Logs
```bash
python logs_simulation.py
````

### Step 2: Train the Model

```bash
python model_training.py
```

### Step 3: Detect Anomalies in Real Time

```bash
python realtime_detection.py
```

---

## 🚨 Example Output

```
normal: {'latency_ms': 200, 'status_code': 173, 'route': '/checkout'}

🚨 anomaly detected:
{'latency_ms': 8427, 'status_code': 500, 'route': '/checkout'}
```

---

## 🧠 Why Isolation Forest?

* Designed specifically for anomaly detection
* Works without labeled data
* Efficient on large datasets
* Widely used in production monitoring systems

---

## 📌 Notes

* Rare but valid events may be flagged as anomalies
* Rule-based logic helps reduce alert noise
* This design mirrors real-world anomaly detection pipelines

---

## 🔮 Future Improvements

* Add anomaly severity scoring
* Auto-retrain model periodically
* Add visualization dashboard
* Extend to gaming or telemetry data

---

## 📜 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for details.
