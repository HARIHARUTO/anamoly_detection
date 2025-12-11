# 🔍 Anomaly Detection Project
# 📜 License
This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

![Python](https://img.shields.io/badge/python-3.13.2%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-learning-orange)
![ML](https://img.shields.io/badge/model-Isolation%20Forest-purple)

A hands‑on learning project focused on **detecting anomalies in log data** using machine learning.

---

## 📂 Workflow
1. **Log Generation** → `logs_generator.py`  
   Creates synthetic logs for experimentation.

2. **Model Training** → `model_train.py`  
   Trains an **Isolation Forest** model.

3. **Anomaly Detection**  
   Identifies unusual patterns after model fitting.

---

## 🧠 Why Isolation Forest?
- ✅ Unsupervised learning — no labels required  
- ✅ Efficient in high‑dimensional spaces  
- ✅ Specially designed to isolate outliers  

---

## ⚡ Quick Start
```bash
# Generate logs
python logs_generator.py

# Train model & detect anomalies
python model_train.py
