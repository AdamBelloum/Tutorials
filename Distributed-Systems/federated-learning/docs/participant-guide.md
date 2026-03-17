
# Federated Learning Workshop
## Collaborative Intelligence Without Sharing Data
- Level: Beginner
- Format: Group-Based, Hands-On
- Duration: Full Day
 
## 1. Welcome & Orientation
### Workshop Goal
By the end of this workshop, you will:
- Understand the core concepts of Federated Learning (FL)
- Train a local AI model on private data
- Participate in federated rounds
- Observe how a global model improves without sharing raw data
- Reflect on privacy, fairness, and collaborative intelligence
 
## 2. Pre-Workshop Checklist
Before we begin, ensure:
-  Hardware
   - Laptop
   - Stable Wi-Fi
   - Chrome or Firefox
- Skills
   - Basic Python (loops, functions, running scripts)
   -Basic ML understanding (training vs testing)
- Access
   - JupyterHub login credentials
   - Assigned Group ID
 
## 3. Morning Session - The "Why" and the "What"
 
### Session 1: Understanding the Problem
#### Goal
Understand why Federated Learning exists.
Key Concepts
- Concept	Meaning
- Data Silo	Data locked in one institution
- Centralized AI	All data sent to one server
- Federated Learning	Model moves, data stays
- Aggregation	Combining model updates
- Model Weights	Mathematical parameters
The Cookbook Analogy
- 	Traditional AI --> Send recipes to one chef
- 	Federated Learning --> Chef sends blank book, you send back notes
#### Reflection (Write 3-5 sentences)
- 	Why is centralized AI risky?
- 	What problem does FL solve?
- 	Where could FL be useful in your field?
 
### Session 2: Technical Environment Check
### Goal
Ensure all participants can connect and run code.
#### Step 1: Log Into JupyterHub
Open the provided URL and log in.
#### Step 2: Run the Test Cell
print("Hello Federated Learning!")
If successful --> environment works.
#### Step 3: Library Check
```python
import flwr
import sklearn
import numpy
```
No errors? - Ready.
If You See Errors:
- 	Check internet
- 	Refresh browser
- 	Ask technical mentor
#### Reflection
- 	What component is acting as your "Node"?
- 	What will act as the "Hub"?
 
#### 4. Module 1 - Your Local AI (11:00-12:30)
**Scenario**: You Are an Isolated Farm
Each group receives a private dataset slice.
Example:
- 	Group A --> Mostly Healthy leaves
- 	Group B --> Brown Streak Disease
- 	Group C --> Mosaic Disease
No group sees the full dataset.
 
#### Goal
- 	Train a model using only your local data
- 	Observe limitations of isolated AI
 
#### Step 1: Explore Your Data
Open your dataset folder.
Questions:
- 	Which disease is dominant?
- 	What is missing?
 
#### Step 2: Complete Local Training
Fill in the missing line in the skeleton:
model.fit(X_train, y_train)
Run the script.
 
#### Step 3: Evaluate Your Model
Check accuracy:
model.score(X_train, y_train)
You will notice:
- 	High performance on your local disease
- 	Very poor generalization
 
#### Expected Limitation
Your model is blind to diseases it has never seen.
This is called:
Non-IID Data (Non-Identically Distributed Data)
 
#### Reflection
Discuss in your group:
- 	Why does your model fail on unseen diseases?
- 	Is your data biased?
- 	What risks exist in deploying this model nationally?
 
#### 5. Afternoon Session - The "How"
 
Module 2 - Joining the Federation (13:30-15:00)
Now we collaborate.
 
#### Goal
- 	Connect to the Hub
- 	Participate in federated rounds
- 	Share weights, not data
 
####  Step 1: Enter Server Address
Replace:
SERVER_ADDRESS = "<INSTRUCTOR_SERVER_IP>:8080"
With instructor-provided IP.
 
#### Step 2: Start the Client
Run:
```python
fl.client.start_numpy_client(...)
```
You should see:
```bash 
Round 1 starting...
```
What Is Happening Behind the Scenes?
1.	Hub sends Global Model
2.	You train locally
3.	You send updated weights back
4.	Hub averages all weights (FedAvg)
5.	Repeat for several rounds
 
Important Concept
You are transmitting:
- [ ] Model weights
- [X] NOT raw images
- [X] NOT private data
 
 Reflection
- 	What information is being shared?
- 	Why is this privacy-preserving?
- 	Could model weights leak information?
 
Module 3 - The Aha! Moment (15:00-15:45)
 
#### Goal
Observe performance improvement after collaboration.
 
#### Step 1: Download Final Global Model
After final round completes, evaluate:
evaluate_global_model()
 
#### Step 2: Compare Results
- Model Type	Accuracy
- Local Model	?
- Global Model	?
You should see significant improvement.
 
Why?
You gained:
Collective intelligence without data sharing
 
Group Exercise
Test:
- 	Group A model on Group C data (fails initially)
- 	Global model on Group C data (succeeds)
 
#### Reflection
Discuss:
- Why did accuracy improve?
- Did your data ever leave your node?
- What are trade-offs of FL?
- When might centralized training still be better?
 
6. Key Technical Takeaways
You experienced:
- Data remains local
- Model travels
- FedAvg aggregation
- Non-IID challenges
- Communication efficiency
- Collaborative fairness
 
7. Architecture Overview
Tier 1 - Edge Nodes (You)
- Local training
- Private datasets
- Lightweight models
Tier 2 - Hub
- Aggregation server
- Coordinates rounds
- Produces global model
 
8. Troubleshooting Guide
Connection Timeout
- 	Check Wi-Fi
- 	Confirm server IP
- 	Ask instructor if server busy
Accuracy is 0
- 	Check dataset path
- 	Confirm labels loaded correctly
Import Error
- 	Restart kernel
- 	Re-run setup cell
 
9. Final Reflection Exercise (15 minutes)
Individually answer:
1.	What problem does Federated Learning solve?
2.	What are its limitations?
3.	Where could you apply this?
4.	What ethical issues remain?
5.	What surprised you most today?
 
10. Beyond Today
If you want to go further:
- Try PyTorch instead of Scikit-learn
- Compare FedAvg vs FedProx
- Experiment with imbalanced datasets
- Add differential privacy
- Simulate 50+ clients
 
#### Final Message
Today you built:
 - A distributed AI system
 - A privacy-preserving training workflow
 - A collaborative intelligence network
Without sharing a single raw image.
That is Federated Learning.
 
Dataset Setup Instructions
We will use a lightweight Cassava Leaf subset prepared for this workshop.
Option A (Recommended for Workshop)
Instructor provides:
data.zip
Inside:
```bash
data/
│
├── group_a/
│   ├── train.csv
│
├── group_b/
│   ├── train.csv
│
├── group_c/
│   ├── train.csv
│
└── train.csv
```
Each group downloads ONLY their folder.

### Option A (Recommended for Workshop — instructor-provided)

The organizer will distribute a per-group archive (e.g. `group_a.zip`). Participants should only download their assigned archive and extract it into the working folder.

Example (participant machine):

```bash
# assuming you received group_a.zip
unzip group_a.zip -d workspace
cd workspace/group_a
ls
# should show train.csv and images/
```

Required structure for participant run (in your working folder):

```bash
workspace/
├── data/
│   ├── train.csv        # metadata: image_id,label (or similar)
│   └── images/          # optional for this tutorial; required for real-image runs
├── client.py
└── local_training.py
```

### Option B (Public Dataset - Kaggle)

If you prefer to download the full dataset yourself (not recommended for workshop attendees because of size and partitioning work), use the Kaggle competition page:

[Cassava Leaf Disease Dataset](https://www.kaggle.com/competitions/cassava-leaf-disease-classification/data)

Download example (participant machine):

```bash
pip install kaggle
# Make sure ~/.kaggle/kaggle.json has your API key
kaggle competitions download -c cassava-leaf-disease-classification -p .
unzip cassava-leaf-disease-classification.zip -d cassava_full
```

**NOTE:** If you download the full dataset yourself you must either ask the instructor for the group partition mapping or partition the data locally (see organizer instructions). For beginners, use the organizer-provided group archive.
 
#### Required Folder Structure (Participants)
After download, your workspace must look like:
```bash
workspace/
│
├── data/
│   ├── train.csv
│   ├── images/

├── client.py
└── utils.py
```

### Quick start (participant)

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install flwr numpy pandas scikit-learn pillow
```

2. Verify your local CSV contains at least a `label` column.

3. Set runtime variables (recommended, no file edit needed):

```bash
export FLOWER_SERVER_ADDRESS=<INSTRUCTOR_SERVER_IP>:8080
export GROUP_ID=Group_A   # change to Group_B or Group_C as assigned
export DATA_PATH=data/Group_A/train.csv
```

4. Run the client to join the federation (server must already be running):

```bash
python client/client.py
```

If the instructor gave you a `group_x.zip`, extract it and point `DATA_PATH` to that CSV.

### Notes on reproducibility and evaluation

- The workshop `client.py` and `local_training.py` simulate features with random vectors (so `train.csv` only needs labels). This is intentional for teaching the FL flow with minimal setup. If you want real image training, ensure `data/images/` is present and modify the client to extract image features or train a lightweight CNN.
- If you see shape or aggregation errors during federated rounds, ask the organizer: likely a label-class coverage mismatch between groups. Organizers should ensure each group contains at least one sample for every label (see organizer guide).
#### Beginner AI Pipeline Skeleton (Fully Runnable)
This pipeline assumes participants have never built an AI model before.
We use:
- Pandas
- Scikit-learn
- Simple features (no deep learning)
- Logistic Regression
 
Step 1 - Install Requirements

```bash
pip install numpy pandas scikit-learn flwr pillow
```

Step 2 - Basic AI Pipeline (Local Training)
Create file: local_training.py

```python
import os
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# ---------------------------------------
# STEP 1: Load CSV Metadata
# ---------------------------------------

DATA_PATH = "data/train.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset loaded.")
print(df.head())

# ---------------------------------------
# STEP 2: Prepare Features and Labels
# ---------------------------------------

# For simplicity we simulate features
# (In real image case, use CNN or embeddings)

X = np.random.normal(size=(len(df), 10))
y = df["label"].values

# ---------------------------------------
# STEP 3: Train/Test Split
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------
# STEP 4: Initialize Model
# ---------------------------------------

model = LogisticRegression(max_iter=200)

# ---------------------------------------
# STEP 5: Train
# ---------------------------------------

model.fit(X_train, y_train)

# ---------------------------------------
# STEP 6: Evaluate
# ---------------------------------------

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
```


- This ensures everyone understands:
- 	Load data
- 	Prepare data
- 	Train
- 	Evaluate
 
#### Federated Version - Complete Beginner Client Skeleton
Create file: client.py
This version works even if participants never implemented FL before.

```python 
import flwr as fl
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss, accuracy_score

# ---------------------------------------
# STEP 1: Identify Your Group
# ---------------------------------------

GROUP_ID = "Group_A"

# ---------------------------------------
# STEP 2: Load Local Dataset
# ---------------------------------------

df = pd.read_csv("data/train.csv")

X = np.random.normal(size=(len(df), 10))
y = df["label"].values

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------
# STEP 3: Initialize Model
# ---------------------------------------

model = LogisticRegression(max_iter=200)

model.classes_ = np.unique(y)
model.coef_ = np.zeros((len(model.classes_), 10))
model.intercept_ = np.zeros(len(model.classes_))

# ---------------------------------------
# STEP 4: Define Flower Client
# ---------------------------------------

class FLClient(fl.client.NumPyClient):

    def get_parameters(self, config):
        return [model.coef_, model.intercept_]

    def set_parameters(self, parameters):
        model.coef_ = parameters[0]
        model.intercept_ = parameters[1]

    def fit(self, parameters, config):
        self.set_parameters(parameters)

        model.fit(X_train, y_train)

        print(f"{GROUP_ID} finished training.")

        return self.get_parameters(config={}), len(X_train), {}

    def evaluate(self, parameters, config):
        self.set_parameters(parameters)

        predictions = model.predict_proba(X_test)
        loss = log_loss(y_test, predictions)
        accuracy = accuracy_score(y_test, model.predict(X_test))

        return loss, len(X_test), {"accuracy": accuracy}

# ---------------------------------------
# STEP 5: Connect to Server
# ---------------------------------------

SERVER_ADDRESS = "<INSTRUCTOR_SERVER_IP>:8080"

fl.client.start_numpy_client(
    server_address=SERVER_ADDRESS,
    client=FLClient()
)
 
🖥 Instructor Server Skeleton (Complete)
Create file: server.py
import flwr as fl

strategy = fl.server.strategy.FedAvg(
    min_fit_clients=2,
    min_available_clients=2,
)

print("Server starting...")

fl.server.start_server(
    server_address="0.0.0.0:8080",
    config=fl.server.ServerConfig(num_rounds=5),
    strategy=strategy,
)
print("Local Model Accuracy:", accuracy)
```
Run server first:
```bash
python server/server.py
```
Then participants run:
```bash 
python client/client.py # set GROUP_ID and FLOWER_SERVER_ADDRESS first
``` 
What Participants Should Observe
During rounds:
```bash
Round 1
Round 2
Round 3
```
Accuracy should increase across rounds.
 
#### What Was Missing Before (Now Fixed)
We added:
- [ ] Explicit dataset source
- [ ] Download instructions
- [ ] Folder structure
- [ ] Installation instructions
- [ ] A full AI pipeline example
- [ ] A complete FL client skeleton
- [ ] A complete server skeleton
- [ ] No prior AI experience required
 
#### Final Reflection Questions (Technical Level)
1.	What changed between local and global training?
2.	What exactly was transmitted?
3.	Could gradients leak private information?
4.	How would you secure this system further?


## 11. Three-VM Deployment Playbook (1 Server + 2 Clients)

This section explains exactly how to run the tutorial on **3 VMs**.

### 11.1 VM Role Assignment (Example)
Use this mapping:

| VM User | IP | Password | Role |
| --- | --- | --- | --- |
| student123 | 145.100.130.123 | ieth3eiLoop6ceew | Flower Server |
| student124 | 145.100.130.124 | aixeiGhieke1safu | Client A |
| student125 | 145.100.130.125 | waicaiGhee6Vaiqu | Client B |

### 11.2 SSH Login
From your local machine, open three terminals:

```bash
ssh student123@145.100.130.123
ssh student124@145.100.130.124
ssh student125@145.100.130.125
```

### 11.3 Prepare Code on All Three VMs
On each VM:

```bash
cd ~/Tutorials/Distributed-Systems/federated-learning
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 11.4 Start Server on `student123`
On VM `145.100.130.123`:

```bash
cd ~/Tutorials/Distributed-Systems/federated-learning
source .venv/bin/activate
export FLOWER_SERVER_HOST=0.0.0.0
export FLOWER_SERVER_PORT=8080
export MIN_FIT_CLIENTS=2
export MIN_AVAILABLE_CLIENTS=2
export MIN_EVALUATE_CLIENTS=2
export NUM_ROUNDS=5
python server/server.py
```

### 11.5 Start Client A on `student124`
On VM `145.100.130.124`:

```bash
cd ~/Tutorials/Distributed-Systems/federated-learning
source .venv/bin/activate
export FLOWER_SERVER_ADDRESS=145.100.130.123:8080
export GROUP_ID=Group_A
export DATA_PATH=data/Group_A/train.csv
python client/client.py
```

### 11.6 Start Client B on `student125`
On VM `145.100.130.125`:

```bash
cd ~/Tutorials/Distributed-Systems/federated-learning
source .venv/bin/activate
export FLOWER_SERVER_ADDRESS=145.100.130.123:8080
export GROUP_ID=Group_B
export DATA_PATH=data/Group_B/train.csv
python client/client.py
```

### 11.7 Expected Logs
- Server terminal shows clients connected and rounds progressing.
- Each client terminal prints training completion for its group.

### 11.8 Minimum Network Checks
On server VM:

```bash
sudo ufw allow 8080/tcp
sudo ufw status
ss -ltnp | grep 8080
```

On each client VM:

```bash
nc -vz 145.100.130.123 8080
```

### 11.9 Notes
- With this setup, `Group_C` is optional and can be used later as a third client.
- In this FL workflow, raw data stays on each client VM; only model parameters are exchanged.
- Do not keep plaintext passwords in shared/public repositories after the workshop.
