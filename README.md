# AlphaNet - AI Driven Network Monitoring System

## Overview

AlphaNet is a Human-in-the-loop based network monitoring and incident analysis platform.

The current PoC consists of:

- GNS3 based MPLS network simulation
- Python telemetry collector
- FastAPI telemetry ingestion layer
- AI analysis pipeline

The objective is to monitor network health, detect failures, and provide automated root cause analysis.

---

# Current Network Architecture

The MPLS topology is implemented using Cisco Packet Tracer.

Network flow:
PC1
|
|
CE1
|
|
PE1
|
|
P1 (Core Router)
|
|
PE2
|
|
CE2
|
|
PC2

Communication has been verified successfully:

PC1 ↔ PC2

---

# Cisco Packet Tracer Configuration

## Devices Used

Routers:
- CE1 : Customer Edge Router 1
- PE1 : Provider Edge Router 1
- P1  : Provider Core Router
- PE2 : Provider Edge Router 2
- CE2 : Customer Edge Router 2

End Devices:

- PC1
- PC2

---

# IP Addressing Scheme
# These are sample values provided for understanding, actual production uses different values
## CE1

Interfaces:
G0/0:

IP:
10.10.1.1

Subnet:
255.255.255.0

G0/1:

IP:
192.168.12.1

Subnet:
255.255.255.252

Connected to:
PC1


PC1:


IP:
10.10.1.10

Gateway:
10.10.1.1


---

## PE1

Interfaces:


G0/0:

IP:
192.168.12.2

Subnet:
255.255.255.252

G0/1:

IP:
172.16.1.1

Subnet:
255.255.255.252


Connected between:


CE1 ↔ P1


---

## P1 Core Router

Interfaces:


G0/0:

IP:
172.16.1.2

Subnet:
255.255.255.252

G0/1:

IP:
172.16.2.1

Subnet:
255.255.255.252


Core MPLS forwarding router.

---

## PE2

Interfaces:


G0/0:

IP:
172.16.2.2

Subnet:
255.255.255.252

G0/1:

IP:
192.168.23.1

Subnet:
255.255.255.252


Connected between:


P1 ↔ CE2


---

## CE2

Interfaces:


G0/0:

IP:
10.20.1.1

Subnet:
255.255.255.0

G0/1:

IP:
192.168.23.2

Subnet:
255.255.255.252


Connected to:


PC2


PC2:


IP:
10.20.1.10

Gateway:
10.20.1.1


---

# Routing Validation

The following communication has been tested:


PC1 → PC2

PC2 → PC1


Successful bidirectional communication confirms:

- CE routing
- PE forwarding
- Core router forwarding
- End-to-end MPLS path availability

---

# Python Telemetry Pipeline

Current flow:


Network Simulator

    |

Python Collector

    |

FastAPI

    |

AI Analysis Layer


FastAPI endpoint:


POST /telemetry


Latest telemetry:


GET /latest


---

# Running the Project

## Clone Repository

```bash
git clone <repository-url>

Move inside:

cd dhurandhar_warriors_repo
Install Dependencies
pip install -r requirements.txt
Start FastAPI
uvicorn main:app --reload
Start Collector
python collector/mpls_collector.py
Current Development Status

Completed:

MPLS topology design
Router configuration
End-to-end communication testing
Telemetry API
Collector framework

In Progress:

Real router telemetry extraction
AI based fault detection
Root cause analysis agent
Automated recommendations
Note

Cisco Packet Tracer is currently used for MPLS topology validation.
For production-grade telemetry collection, integration with:
SNMP
GNS3/EVE-NG
Real network devices
can be added.

For RAG implementation
Important steps:-
Step 1. cd dhurandhar_warriors_repo
Step 2. cd agents
Step 3. cd rag_pipeline
Step 4. run all the scripts in the folder
Step 5. Update the Knowledge Agent by connecting PostGreSQL to the RAG pipeline
Step 6. Create your own chroma_db by running the scripts in rag_pipeline
Step 7. From the output of the JSON, test how the pipeline is working entirely
