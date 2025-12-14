# 📱 MobileNet for Multi-Class Classification using MNIST

## 📌 Project Overview
This project implements **MobileNetV2** for **multi-class image classification** using the **MNIST handwritten digits dataset**.  
The goal is to classify grayscale digit images (0–9) into **10 different classes** using **transfer learning** with MobileNet.

Although MNIST images are small and grayscale, they are adapted to match MobileNet’s input requirements by converting them to RGB format and resizing them within the model.

---

## 📂 Dataset Details
- **Dataset Name:** MNIST Handwritten Digits
- **Number of Classes:** 10 (digits 0–9)
- **Training Samples:** 60,000 images
- **Testing Samples:** 10,000 images
- **Image Size:** 28 × 28 (grayscale)

The MNIST dataset is loaded directly using TensorFlow Keras.

---

## 🛠️ Technologies and Tools Used
- **Programming Language:** Python
- **Deep Learning Framework:** TensorFlow & Keras
- **Model Architecture:** MobileNetV2
- **Dataset:** MNIST (Keras built-in dataset)
- **Visualization:** Matplotlib
- **Development Environment:** Google Colab / Jupyter Notebook

---

## 🧠 Machine Learning Approach
- **Type:** Supervised Learning
- **Task:** Multi-Class Image Classification
- **Loss Function:** Sparse Categorical Crossentropy
- **Optimizer:** Adam
- **Evaluation Metric:** Accuracy
- **Activation Function:** Softmax (Output Layer)

---

## 🔄 Project Workflow
1. Load the MNIST dataset using Keras
2. Normalize image pixel values
3. Convert grayscale images to RGB format
4. Resize images inside the model using a preprocessing layer
5. Apply MobileNetV2 as a feature extractor
6. Add custom dense layers for classification
7. Train the model on training data
8. Evaluate performance on test data
9. Visualize predictions

---

## 🏗️ Model Architecture
- Input Layer (28 × 28 × 3)
- Resizing Layer (96 × 96)
- MobileNetV2 (Pre-trained on ImageNet)
- Global Average Pooling
- Dense Layer (ReLU)
- Dropout Layer
- Output Layer (Softmax – 10 classes)

---

## 📊 Model Evaluation
- **Metric Used:** Accuracy
- The trained model achieves **high classification accuracy** on the MNIST test dataset.
- Predictions are visualized for sample test images.

---

## 📁 File Structure
```

📦 TASK-9
│
├── mobilenet_mnist_multiclass.ipynb        # Main Project Notebook
├── README.md                               # Documentation

```

---

## ▶️ Steps to Run the Project
1. Open Google Colab or Jupyter Notebook
2. Upload the Python file or notebook
3. Run all cells sequentially
4. The model will train and evaluate automatically
5. Sample predictions will be displayed

---

## ✅ Expected Output
- Training and validation accuracy displayed per epoch
- Final test accuracy printed
- Visualization of predicted digit classes

---

## 🎯 Learning Outcomes
- Understanding of **transfer learning**
- Hands-on experience with **MobileNetV2**
- Knowledge of handling grayscale images for RGB-based models
- Implementation of **multi-class classification**
- Model evaluation and visualization techniques

---

## 👩‍💻 Author Information
Divya A  


---
