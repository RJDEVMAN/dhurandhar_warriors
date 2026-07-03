from typing import TypedDict,Dict, List
from dotenv import load_dotenv
from langgraph.graph import StateGraph, START, END
from groq_client import ask_groq
from rag_pipeline.retriever import retrieve_context
# Establishing Groq client
load_dotenv()

# Establishing the receiving point for telemetry data from the network devices
class DeviceTelemetry(TypedDict):

    role: str
    cpu: float
    latency: float
    packet_loss: float
    bandwidth: float
    status: str

# Establishing the LangGraph class
class AlphaNetState(TypedDict):
    network_state: Dict[str, DeviceTelemetry]
    current_agent: str
    diagnosis: Dict
    impact_analysis: Dict
    prediction: Dict
    recommendations: List
    final_decision: str

# Establishing Supervisor agent
def Supervisor_agent(state: AlphaNetState):
    network = state["network_state"]
    critical_devices = []
    for device,data in network.items():
        latency = data.get(
            "latency",
            0
        )
        packet_loss = data.get(
            "packet_loss",
            0
        )
        status = data.get(
            "status",
            "unknown"
        )
        if (
            latency > 200
            or packet_loss > 10
            or status=="CRITICAL"
        ):

            critical_devices.append(device)

    if critical_devices:
        print(
        f"Anomaly detected in {critical_devices}"
        )
        state["current_agent"] = (
            "diagnosis_agent"
        )
    else:
        print(
        "Network healthy"
        )
        state["current_agent"] = (
            "monitoring"
        )
    return state

# Establishing Diagnosis agent
def diagnosis_agent(
    state:AlphaNetState
):
    network = state["network_state"]
    incidents = []
    for device,data in network.items():
        latency = data.get(
            "latency",
            0
        )

        packet_loss = data.get(
            "packet_loss",
            0
        )

        cpu = data.get(
            "cpu",
            0
        )
        status = data.get(
            "status",
            "healthy"
        )
# Initially, Rule-based detection is established.
        if (
            latency > 200
            or packet_loss > 10
            or status=="CRITICAL"
        ):
            print(f"Incident detected: {device}")

# Reasoning Layer is our 1st step towards building a productive analytic AI network in AlphaNet.
            prompt=f"""
            Network Incident is detected as follows:
            Device:-
            {device}

            Role:
            {data.get("role")}

            Metrics:

            CPU:
            {cpu}%

            Latency:
            {latency} ms

            Packet Loss:
            {packet_loss}%

            Status:
            {status}

            Analyze:-
            1. Root cause
            2. Affected network layer
            3. Possible propagation
            4. Severity
            5. Confidence percentage
            Return a structured technical explanation.
            """
            ai_response = ask_groq(prompt)
            incidents.append(

            {
            "device":device,
            "metrics":
            {
            "cpu":cpu,
            "latency":latency,
            "packet_loss":packet_loss
            },
            "severity":
            "CRITICAL",
            "AI_analysis":
            ai_response
            }
            )

    if incidents:
        state["diagnosis"]={
            "incident_detected":True,
            "incidents":incidents
        }

        state["current_agent"]="knowledge_agent"

    else:
        state["diagnosis"]={

            "incident_detected":False,

            "message":
            "Network operating normally"

        }

        state["current_agent"]="monitoring"

    return state

# Establishing the Knowledge agent
# We are moving forward with a Hybrid structure:- RAG + PostGreSQL pipeline for the KB Agent.
def knowledge_agent(state: AlphaNetState):
    diagnosis = state["diagnosis"]
    incidents = diagnosis.get(
        "incidents",
        []
    )
    knowledge_output = []
    for incident in incidents:
        query = f"""

        Device: {incident['device']}

        Severity: {incident['severity']}

        Analysis:

        {incident['AI_analysis']}

        """
        context = retrieve_context(query)

        prompt = f"""
        You are AlphaNet's Knowledge Agent.
        Your main task revolves around analyzing the network incident provided, using the context from the knowledge base.
        Use ONLY the provided documentation.
        Context:
        {context}
        Current Incident:
        {incident}

        Tasks:
        1. Explain the protocol involved.
        2. Explain possible propagation.
        3. Explain historical engineering practices.
        4. Estimate operational impact.
        Return JSON only.

"""

        response = ask_groq(prompt)

        knowledge_output.append(response)

    state["impact_analysis"] = {

        "analysis_completed": True,

        "knowledge": knowledge_output

    }

    state["current_agent"] = "prediction_agent"

    return state
# Here, add the connection between the RAG pipeline and PostGreSQL DB for the knowledge agent. 
# The RAG pipeline will retrieve relevant information from the knowledge base, and the PostGreSQL DB 
# will store and manage the structured data for further analysis and decision-making.