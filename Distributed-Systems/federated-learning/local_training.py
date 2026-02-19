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
accuracy = accuracy_score(y_test, predictions)i

print("Local Model Accuracy:", accuracy)