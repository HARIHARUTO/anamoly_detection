import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import numpy as np
import json

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
    