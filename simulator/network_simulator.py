import requests
import random
import time


API="http://127.0.0.1:8000/telemetry"


devices=[
    "CE1",
    "PE1",
    "P1",
    "PE2",
    "CE2"
]


while True:

    device=random.choice(devices)


    data={

        "device":device,

        "cpu":random.randint(20,90),

        "latency":random.randint(10,200),

        "packet_loss":random.randint(0,5),

        "bandwidth":random.randint(20,90)

    }


    response=requests.post(
        API,
        json=data
    )

    print("FastAPI Response:")
    print(response.json())
    print(data)


    time.sleep(5)
