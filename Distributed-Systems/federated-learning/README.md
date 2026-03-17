# Cassava Federated Learning Workshop
A hands-on workshop to learn Federated Learning (FL) with Flower.

## Overview
This tutorial now supports real multi-VM deployment with:
- 1 server VM (aggregation)
- 2 client VMs (local training)

Default server settings are aligned to this setup:
- `MIN_FIT_CLIENTS=2`
- `MIN_AVAILABLE_CLIENTS=2`
- `MIN_EVALUATE_CLIENTS=2`

## Repository Structure
```text
.
├── docs/
│   ├── organizer-guide.md
│   └── participant-guide.md
├── server/
│   └── server.py
├── client/
│   ├── client.py
│   ├── client_A.py
│   ├── client_B.py
│   └── client_C.py
├── data/
└── requirements.txt
```

## Quick Start
### 1. Server VM
Install dependencies:
```bash
pip install -r requirements.txt
```

Run server (defaults are already for 2 clients):
```bash
python server/server.py
```

Optional explicit config:
```bash
export FLOWER_SERVER_HOST=0.0.0.0
export FLOWER_SERVER_PORT=8080
export MIN_FIT_CLIENTS=2
export MIN_AVAILABLE_CLIENTS=2
export MIN_EVALUATE_CLIENTS=2
export NUM_ROUNDS=5
python server/server.py
```

### 2. Client VMs
Install dependencies:
```bash
pip install -r requirements.txt
```

Run client with environment variables:
```bash
export FLOWER_SERVER_ADDRESS=<SERVER_IP>:8080
export GROUP_ID=Group_A   # or Group_B / Group_C
export DATA_PATH=data/Group_A/train.csv  # optional; auto-resolved if omitted
python client/client.py
```

Alternative wrappers:
```bash
python client/client_A.py
python client/client_B.py
python client/client_C.py
```

## Environment Variables
Server:
- `FLOWER_SERVER_HOST` (default `0.0.0.0`)
- `FLOWER_SERVER_PORT` (default `8080`)
- `MIN_FIT_CLIENTS` (default `2`)
- `MIN_AVAILABLE_CLIENTS` (default `2`)
- `MIN_EVALUATE_CLIENTS` (default `2`)
- `NUM_ROUNDS` (default `5`)

Client:
- `FLOWER_SERVER_ADDRESS` (default `localhost:8080`)
- `GROUP_ID` (default `Group_A`)
- `DATA_PATH` (optional)
- `RANDOM_SEED` (default `42`)

## Troubleshooting
- Round does not start: make sure at least 2 clients are connected.
- Connection refused: check server process, firewall, and port 8080.
- Client data error: ensure CSV exists and includes a `label` column.
