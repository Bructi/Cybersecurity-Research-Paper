import pickle
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier

# 1. Regenerate model quickly
X, y = make_classification(n_samples=10000, n_features=20, n_informative=12, 
                           n_redundant=4, n_classes=2, weights=[0.85, 0.15],
                           flip_y=0.01, class_sep=1.2, random_state=42)

rf_model = RandomForestClassifier(n_estimators=50, max_depth=10, random_state=42, n_jobs=-1)
rf_model.fit(X, y)

# 2. Save Model
with open('../scripts/rf_ids_model.pkl', 'wb') as f:
    pickle.dump(rf_model, f)
print("Model saved to rf_ids_model.pkl")
