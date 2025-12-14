import json
import time 
import joblib

route_map={
    "/Home":0,
    "/login":1,
    "/search":2,
    "/page":3,
    "/checkout":4
}
model=joblib.load("models/isolation_forest_model.joblib")
print("model waiting for logs...")
with open("logs/app.log","r")as f:
    f.seek(0.2)
    while True:
        line=f.readline()
        if not line:
            time.sleep(0.2)
            continue
        log=json.loads(line)
        latency=log["latency_ms"]
        status=log["status_code"]
        route_id=route_map[log["route"]]
        x=[[latency,status,route_id]]
        prediction=model.predict(x)[0]
        if prediction==-1 and (
            log["latency_ms"]>400 or log["status_code"]>400
        ):
            print(f"anamoly detected:{log}")
        else:
            print("normal:",log)
                
        