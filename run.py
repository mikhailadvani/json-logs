import json
import time
import datetime
import random

def main():
    epoch = datetime.datetime(1970,1,1)
    random.seed()
    while(True):
        d = datetime.datetime.utcnow()
        t = (d - epoch).total_seconds()
        obj = {
            "time": t,
            "data": random.randrange(1, 100)
        }
        print(json.dumps(obj))
        time.sleep(1)

if __name__ == '__main__':
    main()
