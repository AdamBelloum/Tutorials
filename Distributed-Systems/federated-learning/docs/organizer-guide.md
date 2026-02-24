# Federated Learning Workshop

## Infrastructure Setup Guide for Organizers

- Target audience: Technical organizers / IT support
- Difficulty: Moderate
- Architecture: Flower-based FL system

 ## 1. Architecture Overview
### System Components

| Component | Role| Runs Where | 
| -------- | -------- | -------- | 
| Flower Server| Aggregation (FedAvg) | Central Hub | 
| JupyterHub (optional) | Browser-based coding | Hub or local lab |
| Dataset Storage | Siloed datasets | Client nodes |
| Flower Client |  Local training | Participant machines |
| Monitoring (optional) | Logs & metrics | Hub |

## 2. Recommended Deployment Model (Most Stable for Workshop)
###  Recommended Setup
- 1 Cloud VM (Hub)
- Participants connect remotely
- Clients run locally on laptops
- No Kubernetes required for beginner workshop

### Tier-2 Hub (Central Server) Setup
#### Minimum Hardware Requirements
- 8 CPU cores
- 16GB RAM
- 100GB storage
- Ubuntu 22.04 LTS
- Public IP address
- Cloud providers: AWS EC2 / Azure VM / DigitalOcean …
- **On-premise Linux server**

#### Step 1 — Prepare Ubuntu Server
SSH into server:
```bash
ssh ubuntu@YOUR_SERVER_IP
```

Update system:
```bash
sudo apt update && sudo apt upgrade -y
```
Install Python:
```bash
sudo apt install python3 python3-pip python3-venv -y
```
#### Step 2 — Create Virtual Environment

```bash
python3 -m venv fl_env
source fl_env/bin/activate
```
Install dependencies:
```bash
pip install flwr numpy scikit-learn pandas
```
#### Step 3 — Configure Firewall
Allow Flower port (default 8080):
```bash
sudo apt update && sudo apt install ufw

sudo ufw allow 8080
sudo ufw enable

# if cancelled, run:
sudo ufw allow 8080
sudo ufw enable
```
Verify:
```bash
sudo ufw status
```
Step 4 — Create Server Script
Create file:
```bash
nano server.py
```
Paste:
```python
import flwr as fl

strategy = fl.server.strategy.FedAvg(
    min_fit_clients=3,
    min_available_clients=3,
)

print("Federated Server Starting...")

fl.server.start_server(
    server_address="0.0.0.0:8080",
    config=fl.server.ServerConfig(num_rounds=5),
    strategy=strategy,
)
```
Save and exit.

#### Step 5 — Start Server
```bash
python server.py
```
You should see:
```bash
Starting Flower server...
```
NOTE: Leave this terminal running during workshop.
### 4.  Dataset Preparation (Before Workshop)
#### Step 1 — Download Dataset (Organizer)

We recommend the Kaggle Cassava Leaf Disease dataset as the source for this workshop. Organizer should download once, partition into per-group slices, and distribute only each group's subset to participants.

- Kaggle link: https://www.kaggle.com/competitions/cassava-leaf-disease-classification/data

Required on the organizer machine:

1. Python 3.9+ and `pip` available.

Download and unzip example (organizer machine):

```bash
group_a/
group_b/
group_c/
```
Each group must have:
```bash
train.csv
```
Step 2 — Create Group Files
Use the provided full dataset to create 3 non-IID partitions (one per group). 


###  Client-Side Setup Options
You have 3 deployment models.

#### OPTION A (Recommended): Local Python on Participant Laptops
Requirements for Participants
Python 3.9+
Internet
VSCode or terminal

Client Installation Instructions (To Send Before Workshop)
Participants run:
```bash
pip install flwr numpy pandas scikit-learn
```
Then place:
```bash
client.py
data/
```
In same folder.
Then update and run:
```bash
python client/client_{X}.py
```
#### OPTION B: JupyterHub (Centralized Browser Environment)
Best when:
- Participants lack Python setup
- IT lab environment

Install JupyterHub on Hub
On server:
```bash
pip install jupyterhub notebook
```
Install configurable HTTP proxy:
```bash
sudo npm install -g configurable-http-proxy
```
Start:
```
jupyterhub
```
Participants access:
```bash
http://SERVER_IP:8000
```
NOTE:You must configure authentication separately for production use.

#### OPTION C: Google Colab (Zero Local Setup)
Participants:
Open shared notebook
Install Flower in notebook:
```bash
!pip install flwr
```
Run client code
NOTE:  Ensure server IP is public.

### 6. Network Validation Checklist (Before Workshop)
On server:
```bash
sudo lsof -i :8080
```
From another machine test:
```bash
telnet SERVER_IP 8080
```
If connection fails:
- Check firewall
- Check cloud security group
= Confirm server running
### 7.  Workshop Day Operational Checklist
Before Participants Arrive
- Server running- Dataset links working- IP address written on board- Backup hotspot available- Assistant assigned for debugging

### 8. Monitoring During Workshop
Server terminal will display:
```bash
Round 1
Round 2
```
If stuck:
- Ensure minimum clients connected
- Check client logs
-  Restart server if needed

### 9..Optional: Enable Logging for Demonstration
Modify server:
```bash
import logging
logging.basicConfig(level=logging.INFO)
```
This shows aggregation details.
### 10.  Optional Advanced Setup (If You Want Professional Infrastructure)
-  Not required for beginner workshop, but scalable:
	- Docker containers
	- Kubernetes (K3s)
	- MLflow for model tracking
	-  Prometheus + Grafana monitoring
	-  Keycloak for identity management
	-  For a one-day workshop, avoid over-engineering.

### 11. Common Failure Points
| Problem | Cause |  Fix | 
| --- | --- |---|
| Clients not connecting |  Firewall |  Open port 8080 | 
| Round never starts | Not enough clients | Reduce min_fit_clients | 
| Accuracy stuck | Data imbalance | Use weighted loss | 
| Server crashes | Memory limit | Increase RAM|

### 12. Security Notes (Important)
For workshop simplicity:
- Communication is unencrypted (default Flower)
- For production:
   - Enable TLS
   - Use secure aggregation
Use authentication
  - Add differential privacy

### 13. Final Infrastructure Flow
1. Organizer starts server
2.  Participants launch clients
3.  Server waits for minimum clients
4.  Training rounds execute
5.  Global model improves
6.  Logs show aggregation


### 14. Time Planning for Organizers

| Task | Time Needed |
| --- |--- |
| Server provisioning | 1-2 hours |
| Dataset partitioning | 2-3 hours |
| Dry run test | 1 hour| 
| Workshop execution |1 day |

### 15. Final Organizer Checklist
- [ ] Cloud server provisioned
- [ ] Port 8080 open
- [ ] Flower installed
- [ ] Server script tested
- [ ] Dataset partitioned
- [ ] Client skeleton tested
- [ ] Dry run with 2 test clients completed
- [ ] Backup internet ready








