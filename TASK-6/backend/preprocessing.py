# preprocessing.py
from PIL import Image
import numpy as np

def extract_features(img_path, size=(128, 128)):
    """
    Load image, resize, normalize and flatten to 1D vector.
    Returns numpy array of shape (1, features).
    """
    img = Image.open(img_path).convert("RGB")
    img = img.resize(size)
    arr = np.array(img, dtype=np.float32) / 255.0
    return arr.flatten().reshape(1, -1)
