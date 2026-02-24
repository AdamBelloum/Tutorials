
# Cassava Federated Learning Workshop
A hands-on workshop designed to teach Federated Learning (FL) concepts using the Cassava Leaf Disease dataset. Participants learn to train collaborative AI models while keeping sensitive agricultural data private on local nodes.

#  Overview
This repository contains a complete framework for running a federated learning simulation.

- Goal: Improve a global model's ability to detect Cassava Mosaic and Brown Streak diseases without sharing raw images.

- Tech Stack: Flower (flwr.dev), Scikit-learn, Pandas, and JupyterHub.

- Scenario: Each participant group acts as a "Siloed Farm" with a unique, biased dataset.

- Repository Structure
```text
.
├── docs/
│   ├── organizer-guide.md     # Infrastructure & server setup
│   └── participant-guide.md   # Workshop exercises & reflection
├── server/
│   └── server.py              # Central aggregation hub
├── client/
│   ├── client.py              # Federated Flower client
├── data/
└── requirements.txt           # Python dependencies
```

# Quick Start
## 1. For Organizers (The Hub)
If you are hosting the workshop, you need to set up the central server.

- Setup: Provision an Ubuntu 22.04+ server and open port 8080.

- Guide: Follow the Organizer Infrastructure Guide.

- Run:

```Bash
python server/server.py
```

## 2. For Participants (The Nodes)
If you are attending the workshop, you will train a model on your local "farm" data.

- Environment: Ensure Python 3.9+ is installed.

- Guide: Follow the Participant Workshop Guide.

- Install Dependencies:

```Bash
pip install -r requirements.txt
```

Run Client:

```Bash
# Replace with the IP provided by your instructor
python client/client.py
```

# Core Concepts Explored
- Data Silos: Participants observe that their local models fail on diseases they haven't seen (Non-IID data).

- Federated Averaging (FedAvg): The server averages model weights to create a "Global Model".

= Privacy: No raw images are ever transmitted to the server; only mathematical weights.

# Troubleshooting
- Connection Refused: Check if the instructor's server is running and port 8080 is open.

- Low Accuracy: Federated learning often requires multiple rounds to outperform local training.

- Module Not Found: Ensure you have activated your virtual environment and ran pip install -r requirements.txt.

# Acknowledgments
- Dataset: Based on the Kaggle Cassava Leaf Disease Classification.
- Framework: Powered by Flower.
