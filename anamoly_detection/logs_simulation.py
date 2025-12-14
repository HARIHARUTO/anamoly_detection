import os
import random
import time 
import json
from datetime import datetime

def simulate_logs():
    log_dir='logs'
    log_file=os.path.join(log_dir,'app.log')
    if not os.path.exists(log_dir):
       os.makedirs(log_dir)
    
    ROUTES=['/Home','/login','/search','/page','/checkout']
    anamoly_probabiltiy=0.03
    max_logs=1000
    count=0
    while count<max_logs:
        
        is_anamoly=random.random()<anamoly_probabiltiy
        if is_anamoly:
             latency=random.randint(5000,10000)
             status_code=500
             route=random.choice(ROUTES)
        else:
             latency=200
             status_code=random.randint(100,300)
             route=random.choice(ROUTES)
        log_entry={
            'timestamp':datetime.now().isoformat(),
            'latency_ms':latency,
            'status_code':status_code,
            'route':route
        }
        with open(log_file,'a')as f:
            f.write(json.dumps(log_entry)+'\n')
        count+=1
        
        time.sleep(random.uniform(0.1,0.5))
if __name__=="__main__":
    simulate_logs()
                 