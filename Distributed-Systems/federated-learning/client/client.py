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

SERVER_ADDRESS = "IP_PROVIDED_BY_INSTRUCTOR:8080"

fl.client.start_numpy_client(
    server_address=SERVER_ADDRESS,
    client=FLClient()
)
 
# 🖥 Instructor Server Skeleton (Complete)
# Create file: server.py
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