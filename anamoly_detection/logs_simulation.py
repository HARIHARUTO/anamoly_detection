import os
import random
import time 
import json

def simulate_logs():
    log_dir='logs'
    log_file=os.path.join(log_dir,'app.log')
    if not os.path.exists(log_dir):
               os.makedirs(log_dir)
    
    ROUTES=['/Home','/login','/search','/page','/checkout']
    anamoly_probabiltiy=0.03
    while True:
        
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
            'timestamp'
            'latency_ms'"latency",
            'status_code':status_code,
            'route':route
        }
        with open(log_file,'a')as f
        
        time.sleep(random.uniform(0.1,0.5))
if __name__=="__main__":
    simulate_logs()
                 