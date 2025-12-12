# 📘 **Customer Churn Prediction using Random Forest & Decision Tree Visualization**

This project predicts **customer churn** using the popular **Telco Customer Churn dataset** and visualizes a **single decision tree** extracted from a Random Forest model.
The goal is to understand **why customers leave** and how machine learning models can help businesses reduce churn.

---

## 📂 **Project Overview**

This project demonstrates:

✔ Loading and preprocessing the Telco Customer Churn dataset
✔ Encoding categorical variables
✔ Training a **Random Forest Classifier**
✔ Evaluating the model using accuracy, confusion matrix & classification report
✔ Plotting **feature importance**
✔ Visualizing a **single decision tree** inside the forest
✔ Understanding decision rules used for churn prediction

The notebook is split into **clean Jupyter cells** for easy execution.

---

## 📊 **Dataset Details**

📌 **Dataset Name:** Telco Customer Churn
📌 **Source:** Kaggle
🔗 [https://www.kaggle.com/datasets/blastchar/telco-customer-churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

**Features include:**

* Customer demographics
* Monthly & total charges
* Contract type
* Payment method
* Internet & phone services
* Tenure
* Whether the customer churned (target variable)

---

## 🛠️ **Technologies & Tools Used**

* **Python 3**
* **Pandas, NumPy** → Data handling
* **Matplotlib, Seaborn** → Visualization
* **Scikit-Learn** → ML models & evaluation
* **RandomForestClassifier** → Classification
* **Decision Tree Plotting** → Model interpretability

---

## 🤖 **Machine Learning Model Used**

### **Random Forest Classifier**

* Ensemble of multiple decision trees
* Reduces overfitting
* Provides reliable & interpretable churn predictions
* Allows extracting and visualizing one tree

---

## 🔄 **Project Workflow**

1. Load dataset
2. Handle missing values
3. Encode categorical features
4. Split into training and testing sets
5. Train Random Forest
6. Predict churn
7. Evaluate model
8. Plot feature importance
9. Visualize one randomly chosen tree

---

## 📁 **Project Structure**

```
📦 TASK-7
│
├── churn_tree_visualization.ipynb     # Main Jupyter Notebook
├── Telco-Customer-Churn.csv           # Kaggle dataset
├── README.md                          # Documentation file
│
└── images/                            # Folder to save tree plots
    ├── single_tree.png
    └── feature_importance.png

```

---

## 📈 **Model Evaluation Metrics**

* **Accuracy Score**
* **Confusion Matrix**
* **Classification Report** (Precision, Recall, F1-score)
* **Feature Importance Chart**

These metrics help understand how well the model predicts churn and which factors influence it the most.

---

## 🌳 **Tree Visualization**

A **single decision tree** from the Random Forest is plotted to understand:

* What rules the model uses
* How features contribute to churn
* Decision boundaries

This improves interpretability and provides insight into customer behavior.

---

## 📝 **Conclusion**

This project successfully demonstrates how machine learning can help telecom companies identify customers at risk of churn.
Using a Random Forest model, we achieve strong prediction performance while also providing interpretable visualizations through tree plots and feature importance graphs.

This makes the model not just accurate but also **explainable**, which is crucial in real-world business applications.

---

## 🎯 **Learning Outcomes**

By completing this project, you will:

* Understand preprocessing of categorical datasets
* Apply Random Forest for churn classification
* Evaluate classification models
* Visualize and interpret decision trees
* Improve understanding of feature importance
* Build a clean, reproducible ML project

---

## 👩‍💻 **Author Information**

**Name:** Divya A
**Course:** B.Tech Artificial Intelligence & Machine Learning
**College:** Bannari Amman Institute of Technology
**Academic Year:** 2025–2026

---


Just tell me! 💙
