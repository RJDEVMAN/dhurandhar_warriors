from fastapi import FastAPI
from models import Telemetry

app = FastAPI(
    title="AlphaNet Telemetry FastAPI"
)

network_state = {}
latest_telemetry = {

    "status":"waiting",

    "message":"No telemetry received yet"

}



# NETWORK ---> FASTAPI
@app.post("/telemetry")
def receive_telemetry(data: Telemetry):

    global network_state
    
    network_state[data.device] = data.model_dump()

    print("\n")
    print("🚨 NETWORK TELEMETRY RECEIVED")

    print(f"Device      : {data.device}")
    print(f"CPU         : {data.cpu}%")
    print(f"Latency     : {data.latency} ms")
    print(f"Packet Loss : {data.packet_loss}%")
    print(f"Bandwidth   : {data.bandwidth}%")

    print("\n")

    return {

        "status":"received",

        "device":data.device

    }



# DASHBOARD / AI ---> FASTAPI

@app.get("/latest")
def get_latest_telemetry():

    return network_state



@app.get("/")
def home():

    return {

        "message":
        "AlphaNet Backend Running"

    }