# train_models.py
import os
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from preprocessing import extract_features 

BASE_DIR = os.path.dirname(__file__)
DATASET_DIR = os.path.join(BASE_DIR, "images")
MODELS_DIR = os.path.join(BASE_DIR, "models")
os.makedirs(MODELS_DIR, exist_ok=True)

def load_dataset():
    X, y = [], []
    class_names = []
    for label in sorted(os.listdir(DATASET_DIR)):
        class_path = os.path.join(DATASET_DIR, label)
        if not os.path.isdir(class_path):
            continue
        class_names.append(label)
        for fname in os.listdir(class_path):
            img_path = os.path.join(class_path, fname)
            try:
                feat = extract_features(img_path)
                X.append(feat.flatten())
                y.append(label)
            except Exception as e:
                print(f"Skipped {img_path}: {e}")
    X = np.array(X)
    y = np.array(y)
    print(f"Loaded dataset: X.shape={X.shape}, y.shape={y.shape}, classes={class_names}")
    return X, y

def train_and_save():
    X, y = load_dataset()
    if len(X) == 0:
        raise RuntimeError("No training data found. Put dataset into backend/images/CLASS_NAME/*.jpg")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    models = {
    "svm": SVC(probability=True),
    "random_forest": RandomForestClassifier(n_estimators=200),
    "logreg": LogisticRegression(max_iter=400, solver='lbfgs'),
    "knn": KNeighborsClassifier(n_neighbors=5)
    }


    for name, model in models.items():
        print(f"Training {name} ...")
        model.fit(X_train, y_train)
        # evaluate quickly
        score = model.score(X_test, y_test)
        print(f"{name} test accuracy: {score:.4f}")
        save_path = os.path.join(MODELS_DIR, f"{name}.pkl")
        joblib.dump(model, save_path)
        print(f"Saved {save_path}")

if __name__ == "__main__":
    train_and_save()
