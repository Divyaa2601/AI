# 📘 **Handwritten Digit Recognition using Neural Networks (MNIST)**

This project demonstrates handwritten digit classification using the **MNIST dataset** and a **Convolutional Neural Network (CNN)** built with PyTorch.
The model learns to recognize digits (0–9) and visualizes predictions along with training curves.

This project is inspired by sample neural-network notebooks but uses a **CNN**, making it more robust and unique while staying close to the original structure.

---

## 📂 **Project Overview**

In this project, you will:

*  Load the MNIST dataset
*  Build a Convolutional Neural Network using PyTorch
*  Train the model and visualize accuracy & loss curves
*  Predict digits on test images
*  Display results with actual vs. predicted values
*  Evaluate model performance using test accuracy

This showcases deep learning fundamentals applied to image classification.

---

## 📊 **Dataset Details**

### **MNIST Handwritten Digit Dataset**

* **Images:** 70,000
* **Type:** 28×28 grayscale images
* **Classes:** Digits 0–9
* **Train/Test Split:** 60,000 train, 10,000 test
* **Source:** TensorFlow / PyTorch datasets

This dataset is a standard benchmark used for learning neural networks.

---

## 🛠️ **Technologies & Tools Used**

* **Python 3**
* **PyTorch**
* **torchvision**
* **NumPy**
* **Matplotlib**
* **Jupyter Notebook**

---

## 🤖 **Model Architecture Used**

### **Convolutional Neural Network (CNN)**

The model consists of:

1. **Conv2D layer → ReLU → MaxPool**
2. **Conv2D layer → ReLU → MaxPool**
3. **Fully connected (Dense) layers**
4. **Output: 10 classes (digits 0–9)**

CNN is chosen because it performs significantly better than simple fully connected networks on image data.

---

## 🔄 **Project Workflow**

1. Load dataset from torchvision
2. Apply normalization
3. Define CNN architecture
4. Train model for 5 epochs
5. Plot loss & accuracy
6. Visualize predictions
7. Evaluate test accuracy

---

## 📁 **Project Structure**

```
📦 TASK-8 Handwritten Digit Recognition (NN)
│
├── digit_cnn_recognition.ipynb        # Main Project Notebook
├── README.md                          # Documentation
```

---

## 📈 **Training Evaluation**

During training, the notebook visualizes:

📌 **Training Loss Curve**

📌 **Training Accuracy Curve**

These graphs help understand model learning behavior over epochs.

---

## 🖼️ **Prediction Visualization**

The notebook displays:

* First 10 test images
* Predicted vs. true labels
* Clear visualization of model performance

This helps in interpreting the model beyond numbers.

---

## 🎯 **Learning Outcomes**

By completing this project, you will learn:

* How to build and train CNN models in PyTorch
* How image datasets are preprocessed and normalized
* Forward & backward propagation concepts
* How to visualize deep learning metrics
* How to test and interpret predictions
* Practical understanding of MNIST classification

---

## 📝 **Conclusion**

This project demonstrates a complete deep learning workflow using MNIST and PyTorch.
The CNN model achieves strong accuracy and shows reliable recognition of handwritten digits.
With additional improvements like dropout, batch normalization, or deeper networks, performance can be further enhanced.

---

## 👩‍💻 **Author Information**

* **Name:** Divya A
* **Course:** B.Tech Artificial Intelligence & Machine Learning
* **College:** Bannari Amman Institute of Technology
* **Academic Year:** 2025–2026

---
