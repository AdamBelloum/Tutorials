# Federated Learning Workshop

## Infrastructure Setup Guide for Organizers

This guide is updated for a real distributed deployment with **3 VMs**:
- 1 VM as Flower server (aggregation)
- 2 VMs as Flower clients (local training)

## 1. Architecture
| Component | Role | Runs Where |
| --- | --- | --- |
| Flower Server | FedAvg aggregation and round coordination | Server VM |
| Flower Client A | Local training on private shard | Client VM 1 |
| Flower Client B | Local training on private shard | Client VM 2 |

## 2. Minimum Setup
- Ubuntu 22.04+
- Python 3.9+
- Port `8080/tcp` reachable from both client VMs to server VM

## 3. Server VM Setup
### 3.1 Install dependencies
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv ufw
```

```bash
python3 -m venv fl_env
source fl_env/bin/activate
pip install -r requirements.txt
```

### 3.2 Open port 8080
```bash
sudo ufw allow 8080/tcp
sudo ufw enable
sudo ufw status
```

### 3.3 Start server (defaults already match 2 clients)
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

## 4. Client VM Setup (run on each client VM)
### 4.1 Install dependencies
```bash
python3 -m venv fl_env
source fl_env/bin/activate
pip install -r requirements.txt
```

### 4.2 Copy only local shard to each VM
Recommended:
- Client VM 1 keeps only `data/Group_A/train.csv`
- Client VM 2 keeps only `data/Group_B/train.csv`

### 4.3 Start each client
Client VM 1 example:
```bash
export FLOWER_SERVER_ADDRESS=<SERVER_VM_IP>:8080
export GROUP_ID=Group_A
export DATA_PATH=data/Group_A/train.csv
python client/client.py
```

Client VM 2 example:
```bash
export FLOWER_SERVER_ADDRESS=<SERVER_VM_IP>:8080
export GROUP_ID=Group_B
export DATA_PATH=data/Group_B/train.csv
python client/client.py
```

## 5. Validation Checklist
- Server logs show `Federated Server Starting...`
- Both clients connect successfully
- Training rounds advance (`Round 1`, `Round 2`, ...)
- No raw dataset is sent to server, only model parameters

## 6. Common Issues
| Problem | Cause | Fix |
| --- | --- | --- |
| Round never starts | Not enough clients connected | Ensure both clients are online and `MIN_*_CLIENTS=2` |
| Client cannot connect | Firewall/security group issue | Open server `8080/tcp` |
| Client crashes on CSV | Missing `label` column or wrong path | Check `DATA_PATH` and CSV schema |

## 7. Security Reminder
If this is beyond classroom use:
- Enable TLS in Flower
- Avoid storing plaintext credentials in docs/scripts
- Consider secure aggregation and differential privacy
