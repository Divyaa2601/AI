# 😃 Sentiment Analysis using Naive Bayes

## 📄 Project Overview

This project demonstrates **sentiment analysis** using **Naive Bayes classifiers** (MultinomialNB and BernoulliNB) on a **custom synthetic dataset**. The goal is to classify text into **positive** or **negative sentiment** and visualize the **most influential words** for each sentiment class.

---

## 🗂 Dataset Details

* **Type:** Synthetic / Custom
* **Size:** 20 sentences (10 positive, 10 negative)
* **Columns:**

  * `text` – Original sentence
  * `label` – Sentiment class (`positive` or `negative`)
  * `clean` – Preprocessed text (lowercased, special characters removed)

**Positive Examples:** “This book is absolutely brilliant”, “I really enjoyed the movie last night”
**Negative Examples:** “The food tasted awful and stale”, “I regret buying this product”

---

## ⚙️ Technology & Tools Used

* **Programming Language:** Python 3
* **Libraries:**

  * `pandas` – Data manipulation
  * `numpy` – Numerical computations
  * `re` – Text cleaning
  * `matplotlib` – Data visualization
  * `scikit-learn` – Machine learning models and metrics
* **Environment:** VS Code / Jupyter Notebook / Google Colab

---

## 🧰 File Structure

```
TASK-4/
│
├── sentiment_analysis_naive_bayes.ipynb    # Main notebook with code
├── README.md                               # Project documentation
```

---

## 🤖 Machine Learning Algorithms

* **Multinomial Naive Bayes:** Suitable for **word count features**
* **Bernoulli Naive Bayes:** Suitable for **binary features** (word presence/absence)

---

## ⚡ Project Workflow

1. Import necessary libraries
2. Create a **custom synthetic dataset**
3. **Clean and preprocess** text
4. Convert text into **vectorized features** using `CountVectorizer`
5. Split data into **training and testing sets**
6. Train **MultinomialNB** and **BernoulliNB** classifiers
7. Evaluate models using **accuracy** and **confusion matrix**
8. Extract and visualize **top positive and negative words**

---

## 📊 Model Evaluation Metrics

* **Accuracy** – Measures how well the model classifies sentiments
* **Confusion Matrix** – Shows correct vs incorrect predictions

**Example Output (MultinomialNB):**

```
Accuracy: 1.0
Confusion Matrix:
[[3 0]
 [0 3]]
```

---

## 🔍 Top Words Visualization

* **MultinomialNB:** Top words determined by **log-odds**
* **BernoulliNB:** Top words determined by **word probability**
* Positive words are shown in **green** and negative words in **red**

---

## 🚀 Steps to Run the Project

1. Open `sentiment_analysis_naive_bayes.ipynb` in Jupyter Notebook
2. Run the notebook **cell by cell**
3. Observe:

   * Model accuracies
   * Confusion matrices
   * Positive & negative word bar charts

---

## 🎯 Expected Output

* Accuracy values for both classifiers
* Confusion matrices
* Plots of **top positive and negative words** for each classifier

---

## ✅ Conclusion

This project demonstrates how **Naive Bayes classifiers** can be applied for **text classification** and **sentiment analysis** on a small custom dataset. It also highlights the importance of **preprocessing** and **feature extraction** in NLP tasks.

---

## 📚 Learning Outcomes

* Understand **MultinomialNB vs BernoulliNB** in NLP
* Learn to **clean and preprocess text data**
* Visualize the **most important words** for sentiment classification
* Gain hands-on experience in **text classification workflow**

---

## 👩‍💻 Author Information

* **Name:** Divya A
* **Course:** B.Tech, Artificial Intelligence and Machine Learning
* **College:** Bannari Amman Institute of Technology
* **Academic Year:** 2025–2026

---
