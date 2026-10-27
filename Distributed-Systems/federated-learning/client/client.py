import os
from pathlib import Path

import flwr as fl
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split


def _resolve_data_path(group_id: str) -> Path:
    configured = os.environ.get("DATA_PATH")
    if configured:
        return Path(configured)

    path = Path(f"data/{group_id}/train.csv")
    if path.exists():
        return path

    raise FileNotFoundError(
        f"No training CSV found for {group_id}. "
        f"Expected: data/{group_id}/train.csv or set DATA_PATH."
    )


def main() -> None:
    group_id = os.environ.get("GROUP_ID", "Group_A")
    server_address = os.environ.get("FLOWER_SERVER_ADDRESS", "localhost:8080")
    random_seed = int(os.environ.get("RANDOM_SEED", "42"))

    data_path = _resolve_data_path(group_id)
    df = pd.read_csv(data_path)
    if "label" not in df.columns:
        raise ValueError(f"Missing 'label' column in {data_path}")

    X = np.random.normal(size=(len(df), 10))
    y = df["label"].values
    classes = np.unique(y)

    if len(classes) < 2:
        raise ValueError(
            f"{group_id} has only {len(classes)} class in {data_path}. "
            "Need at least 2 classes for LogisticRegression."
        )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=random_seed
    )

    model = LogisticRegression(max_iter=200)
    model.classes_ = classes
    model.coef_ = np.zeros((len(model.classes_), 10))
    model.intercept_ = np.zeros(len(model.classes_))

    class FLClient(fl.client.NumPyClient):
        def get_parameters(self, config):
            return [model.coef_, model.intercept_]

        def set_parameters(self, parameters):
            model.coef_ = parameters[0]
            model.intercept_ = parameters[1]

        def fit(self, parameters, config):
            self.set_parameters(parameters)
            model.fit(X_train, y_train)
            print(f"{group_id} finished training on {len(X_train)} samples.")
            return self.get_parameters(config={}), len(X_train), {}

        def evaluate(self, parameters, config):
            self.set_parameters(parameters)
            predictions = model.predict_proba(X_test)
            loss = log_loss(y_test, predictions)
            accuracy = accuracy_score(y_test, model.predict(X_test))
            return loss, len(X_test), {"accuracy": accuracy}

    print("Client starting...")
    print(
        "Config:",
        {
            "group_id": group_id,
            "data_path": str(data_path),
            "server_address": server_address,
            "samples": len(df),
            "classes": classes.tolist(),
        },
    )
    fl.client.start_numpy_client(server_address=server_address, client=FLClient())


if __name__ == "__main__":
    main()
