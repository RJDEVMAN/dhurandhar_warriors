import random
import time
import requests
# This is a simulated telemetry network, this is NOT going to be used in production, it is just for testing purposes.
# Kindly remove this code after the telemetry network is implemented in production. 

FASTAPI_URL = "http://127.0.0.1:8000/telemetry"


devices = {

    "CE1": {
        "role":"Customer Edge",
        "base_latency":20
    },

    "PE1": {
        "role":"Provider Edge",
        "base_latency":30
    },

    "P1": {
        "role":"Core Router",
        "base_latency":25
    },

    "PE2": {
        "role":"Provider Edge",
        "base_latency":35
    },

    "CE2": {
        "role":"Customer Edge",
        "base_latency":20
    }

}


def generate_network_state(device):


    info = devices[device]


    latency = random.randint(
        info["base_latency"]-5,
        info["base_latency"]+15
    )


    packet_loss = random.choice(
        [0,0,0,1,2]
    )


    cpu = random.randint(
        30,70
    )


    bandwidth = random.randint(
        40,80
    )
    if random.random() < 0.1:

        return {

        "device":device,

        "role":devices[device]["role"],

        "cpu":95,

        "latency":999,

        "packet_loss":100,

        "bandwidth":5,

        "status":"CRITICAL"

    }


    return {
        "device":device,

        "role":info["role"],

        "cpu":cpu,

        "latency":latency,

        "packet_loss":packet_loss,

        "bandwidth":bandwidth,

        "status":"healthy"

    }

while True:
    for device in devices:
        telemetry = generate_network_state(device)
        requests.post(
            FASTAPI_URL,
            json=telemetry
        )


    time.sleep(5)