# 🐾 **Animal Classifier Web App**

---

## 🚀 **Project Overview**

This project is a complete **image classification web application** capable of identifying animals from images using classical machine learning algorithms.
It features a **FastAPI backend** for ML inference and a **modern HTML/CSS/JS frontend** with drag-and-drop image upload and real-time prediction display.

---

## 📥 **Dataset Details**

This project uses a **custom curated subset** of the Animals-10 dataset (Kaggle), containing 6 animal classes:

```
cat, cow, dog, elephant, horse, squirrel
```

Dataset is stored inside:

```
backend/images/
```

Original dataset link (for reference):
🔗 [https://www.kaggle.com/datasets/alessiocorrado99/animals10](https://www.kaggle.com/datasets/alessiocorrado99/animals10)

Since datasets are large, **they are not included** in the repository.


---

## 🛠️ **Technology and Tools Used**

### 🔹 Backend

* FastAPI
* Uvicorn
* Scikit-Learn
* NumPy
* Pillow
* Joblib

### 🔹 Frontend

* HTML
* CSS (Aqua Blue Modern Theme)
* JavaScript (Fetch API + drag-and-drop upload)

---

## 🧠 **Machine Learning Models Used**

The system supports multiple classical ML algorithms:

* **Support Vector Machine (SVM)**
* **Random Forest Classifier**
* **Logistic Regression**
* **K-Nearest Neighbors (KNN)**

These models are trained on extracted image features and saved as `.pkl` files in the backend.

---

## 🗂 **Folder Structure**

```
TASK-6/
│
├── backend/
│   ├── main.py               # FastAPI routes & prediction API
│   ├── train_models.py       # Training script for ML models
│   ├── preprocessing.py      # Feature extraction from images
│   ├── model_utils.py        # Utility functions for model loading
│   └── models/               # Trained model files (.pkl)
│
├── frontend/
│   ├── index.html            # Main UI
│   ├── style.css             # Aqua blue theme + animations
│   └── script.js             # Client-side logic
│
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation
```

---

## 🏋️‍♂️ **Training the Models**

Run the following commands:

```bash
cd backend
pip install -r ../requirements.txt
python train_models.py
```

Training output (saved files):

```
backend/models/svm.pkl
backend/models/random_forest.pkl
backend/models/logreg.pkl
backend/models/knn.pkl
```

---

## 🖥️ **Running the Backend**

Install dependencies:

```bash
pip install -r requirements.txt
```

Start FastAPI server:

```bash
uvicorn main:app --reload
```

Open API documentation:

👉 [http://localhost:8000/docs](http://localhost:8000/docs)

You can test image classification directly from Swagger UI.

---

## 🌐 **Running the Frontend**

Simply open:

```
frontend/index.html
```

Features include:

* Drag & drop image upload
* Live image preview
* Model selection
* Instant prediction display

---

## ✨ **Key Features**

* Easy-to-use animal classification web app
* Multiple classical ML models supported
* Clean and modular FastAPI backend
* Beautiful, responsive, modern frontend UI
* Drag-and-drop image upload
* Pretrained models for fast prediction
* Simple training workflow for dataset updates

---

## 🏁 **Conclusion**

This project demonstrates how to build a complete machine learning application—from dataset preparation and feature extraction to model training, API development, and user-friendly frontend integration.
The modular structure makes it easy to expand the project by adding more models, improving the UI, or integrating deep learning techniques.

---

## 🎯 **Learning Outcomes**

By completing this project, learners will:

* Understand end-to-end ML application development
* Learn how to preprocess images and extract features
* Train, save, and load classical ML models
* Build REST APIs using FastAPI
* Implement interactive frontend interfaces using HTML/CSS/JS
* Use the Fetch API to send images from frontend to backend
* Organize a scalable project structure (backend + frontend)
* Deploy and document ML projects professionally

---

## 👩‍💻 Author Information

* **Name:** Divya A
* **Course:** B.Tech, Artificial Intelligence and Machine Learning
* **College:** Bannari Amman Institute of Technology
* **Academic Year:** 2025–2026

