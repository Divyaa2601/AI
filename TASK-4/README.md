# 📧 SMS/Email Spam Detection using Logistic Regression

---

## 📌 Project Overview
This project implements a **machine learning-based spam detection system** using **Logistic Regression**.  
The system classifies messages as **SPAM** or **NOT SPAM** based on their content.  
Text data is converted to numerical form using **TF-IDF Vectorization**, and the model outputs both **class predictions** and **probability scores (sigmoid output)**.

---

## 📊 Dataset Details
The project uses the **SMS Spam Collection Dataset** from Kaggle.

- **Kaggle Link:** [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)  
- **File:** `spam.csv`  
- **Columns:**

| Column | Description |
|--------|-------------|
| v1     | Label (`ham` for not spam, `spam` for spam) |
| v2     | Message text |

**Preprocessing Steps:**  
1. Renamed columns to `label` and `message`.  
2. Converted labels to numeric: `ham = 0`, `spam = 1`.  
3. Performed train-test split (80% train, 20% test).  

---

## 🛠️ Technology and Tools Used
- **Programming Language:** Python 3.x  
- **Libraries:** pandas, numpy, scikit-learn, matplotlib (optional)  
- **IDE/Platform:** VS Code / Jupyter Notebook / Google Colab  
- **Dataset Source:** Kaggle  

---

## ⚙️ Machine Learning Algorithm
- **Algorithm Used:** Logistic Regression  
- **Purpose:** Binary classification of messages into SPAM or NOT SPAM  
- **Feature Extraction:** TF-IDF Vectorization of text messages  
- **Model Output:** Class predictions and probability scores (sigmoid output)  

---

## 🔄 Project Workflow
1. **Data Loading:** Load the CSV dataset into a Pandas DataFrame.  
2. **Preprocessing:** Map labels to numeric values.  
3. **Train-Test Split:** 80% training data, 20% testing data.  
4. **Text Vectorization:** Convert messages to TF-IDF feature vectors.  
5. **Model Training:** Train a Logistic Regression classifier.  
6. **Evaluation:**  
   - Accuracy score  
   - Classification report  
7. **Prediction:**  
   - Predict on test messages  
   - Sigmoid probability output for each message  
   - Test on custom messages  

---

## 📈 Model Evaluation Metrics
- **Accuracy:** Measures the proportion of correctly classified messages.  
- **Classification Report:** Includes precision, recall, and F1-score for both classes (SPAM and NOT SPAM).  
- **Sigmoid Probability Output:** Shows the likelihood of a message being SPAM.  

---

## 📁 File Structure (TASK-4 Folder)
```

TASK-4/
│
├── spam_detection.py        # Main Python code
├── spam.csv                 # Dataset file from Kaggle
├── README.md                # Project documentation (this file)

````

---

## ▶️ Steps to Run the Project
1. Download `spam.csv` from Kaggle and place it in the `TASK-4/` folder.  
2. Open `spam_detection.py` in Python IDE (VS Code / Jupyter Notebook / Colab).  
3. Install required libraries if not already installed:
   ```bash
   pip install pandas numpy scikit-learn matplotlib
````

4. Run the Python script to train the model, test on sample messages, and view predictions.

---

## ✅ Expected Output

* **Accuracy score** on test dataset.
* **Classification report** showing precision, recall, F1-score.
* **Sigmoid probabilities** for test/custom messages.
* **Predicted labels**: SPAM or NOT SPAM.

**Example:**

```
Message: Congratulations! You won a free mobile
Prediction: SPAM, Probability of Spam: 0.97

Message: Please submit the report by today
Prediction: NOT SPAM, Probability of Spam: 0.03
```

---

## 🎯 Conclusion

* The **Logistic Regression model** effectively classifies messages into **SPAM** and **NOT SPAM**.
* Using **TF-IDF vectorization** helps the model understand the importance of words in spam detection.
* The **sigmoid output** provides the probability of a message being spam, useful for email filters.
* This lab demonstrates the **practical application of machine learning in text classification**.

---

## 🎓 Learning Outcomes

After completing this lab, students will be able to:

1. Understand the concept of **spam detection** and its real-world applications.
2. Preprocess text data for machine learning tasks.
3. Implement **TF-IDF vectorization** to convert text into numerical features.
4. Train and evaluate a **Logistic Regression model** for binary classification.
5. Interpret model outputs, including **accuracy, classification report, and sigmoid probabilities**.
6. Test the model on custom messages to predict spam or not spam.

---

## 👩‍💻 Author Information

* **Name:** Divya A
* **Course:** B.Tech, Artificial Intelligence and Machine Learning
* **College:** Bannari Amman Institute of Technology
* **Academic Year:** 2025–2026
