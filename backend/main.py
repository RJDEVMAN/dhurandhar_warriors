from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime


app = FastAPI(
    title="AlphaNet Telemetry FastAPI structure"
)


class Telemetry(BaseModel):
    device: str
    cpu: float
    latency: float
    packet_loss: float
    bandwidth: float



# stores latest network state
latest_telemetry = {
    "status": "waiting",
    "message": "No telemetry received yet"
}



# NETWORK ---> FASTAPI
@app.post("/telemetry", description="Receive telemetry data from network devices and store it in the DB of AlphaNet")
def receive_telemetry(data: Telemetry):

    global latest_telemetry


    latest_telemetry = {

        "status": "active",

        "timestamp": datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        ),

        "device": data.device,

        "cpu": data.cpu,

        "latency": data.latency,

        "packet_loss": data.packet_loss,

        "bandwidth": data.bandwidth
    }



    print("🚨 NETWORK TELEMETRY RECEIVED")
    print(f"Device      : {data.device}")
    print(f"CPU         : {data.cpu}%")
    print(f"Latency     : {data.latency} ms")
    print(f"Packet Loss : {data.packet_loss}%")
    print(f"Bandwidth   : {data.bandwidth}%")

    return latest_telemetry



# DASHBOARD / AI ---> FASTAPI
@app.get("/latest", description="Get the latest telemetry data and show it on the dashboard")
def get_latest_telemetry():

    return latest_telemetry

@app.get("/")
def home():

    return {
        "message":
        "backend running"
    }