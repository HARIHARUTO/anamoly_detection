import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import numpy as np
import json
import os


print("model_training.py started")

logs = []

with open("logs/app.log", "r") as f:
    for line in f:
        line = line.strip()
        if line:
            log = json.loads(line)
            logs.append(log)

print("Number of logs loaded:", len(logs))
print("First 3 logs:")
print(logs[:3])

route_map = {
    "/Home": 0,
    "/login": 1,
    "/search": 2,
    "/page": 3,
    "/checkout": 4
}

X = []

for log in logs:
    latency = log["latency_ms"]
    status = log["status_code"]
    route_id = route_map[log["route"]]
    X.append([latency, status, route_id])

print("First 5 feature rows:")
print(X[:5])
print("END OF FILE REACHED")

model=IsolationForest(
    n_estimators=100,
    max_samples='auto',
    contamination=0.05,
    random_state=42 
)
model.fit(X)
print("Model training completed")
predictions = model.predict(X)

# -1 = anomaly, 1 = normal
anomaly_count = sum(p == -1 for p in predictions)

print("Total anomalies detected:", anomaly_count)
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/isolation_forest_model.joblib")
print("Model saved to models/isolation_forest_model.joblib")
