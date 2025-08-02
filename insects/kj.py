import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from pytorch_tabnet.tab_model import TabNetClassifier
import torch
import numpy as np

# Load CSV
df = pd.read_csv("C:/Users/kisho/Downloads/insects/crop_insect_characteristics.csv")

# Preview
print("✅ Dataset loaded:")
print(df.head())

# Convert Yes/No to 1/0 if needed (optional)
df = df.replace({'Yes': 1, 'No': 0, 'yes': 1, 'no': 0})

# Separate features and target
X = df.drop(columns=["label", "filename"], errors='ignore')  # drop target column
y = df["label"]  # assume you already created this (0 or 1)

# Encode any categorical data (if any)
for col in X.columns:
    if X[col].dtype == "object":
        X[col] = LabelEncoder().fit_transform(X[col])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X.values, y.values, test_size=0.2, random_state=42
)

# Convert to float32
X_train = X_train.astype(np.float32)
X_test = X_test.astype(np.float32)
y_train = y_train.astype(np.int64)
y_test = y_test.astype(np.int64)

# Initialize TabNet model
clf = TabNetClassifier()

# Train model
clf.fit(
    X_train=X_train, y_train=y_train,
    eval_set=[(X_test, y_test)],
    eval_name=["test"],
    eval_metric=["accuracy"],
    max_epochs=100,
    patience=20,
    batch_size=16,
    virtual_batch_size=8,
    num_workers=0,
    drop_last=False
)

# Evaluate
from sklearn.metrics import accuracy_score

y_pred = clf.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Test Accuracy: {acc:.4f}")

