import requests
from ping3 import ping
import time


FASTAPI_URL = (
"http://127.0.0.1:8000/telemetry"
)

# Replace the IP addresses with the actual IPs of the routers you provided while building the MPLS network in GNS3.
# This would be used for production and deployment.
devices = {


"CE1":
"10.10.1.1",


"PE1":
"192.168.12.2",


"P1":
"172.16.1.2",


"PE2":
"172.16.2.2",


"CE2":
"10.20.1.1"

}



while True:


    for device,ip in devices.items():


        result = ping(
            ip,
            timeout=2
        )


        if result is None:


            data={

            "device":device,

            "latency":999,

            "packet_loss":100,

            "status":"DOWN"

            }


        else:


            data={

            "device":device,

            "latency":
            round(result*1000,2),

            "packet_loss":0,

            "status":"ACTIVE"

            }



        requests.post(
            FASTAPI_URL,
            json=data
        )


    time.sleep(5)