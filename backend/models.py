from pydantic import BaseModel


class Telemetry(BaseModel):

    device: str

    role: str | None = None

    cpu: float

    latency: float

    packet_loss: float

    bandwidth: float

    status: str | None = None