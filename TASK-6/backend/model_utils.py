# model_utils.py
import joblib
import os
from preprocessing import extract_features

MODELS_DIR = os.path.join(os.path.dirname(__file__), "models")

def load_model(model_name: str):
    """
    model_name should match the filename prefix: 'knn', 'logreg', 'nb', 'tree'
    loads models/<model_name>.pkl
    """
    path = os.path.join(MODELS_DIR, f"{model_name}.pkl")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Model file not found: {path}")
    return joblib.load(path)

def predict_image(img_path: str, model_name: str):
    model = load_model(model_name)
    features = extract_features(img_path)
    prediction = model.predict(features)[0]
    return prediction
