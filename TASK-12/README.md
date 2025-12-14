# 🌐 English to Tamil Machine Translation using Attention

## 📌 Project Overview
This project implements a **Neural Machine Translation (NMT)** system that translates **English sentences into Tamil** using an **Encoder–Decoder architecture with Attention mechanism**.  
The model is built using **LSTM networks** and helps the decoder focus on relevant parts of the input sentence while generating the output.

---

## 📂 Dataset Description
- A small custom dataset of **English–Tamil sentence pairs**
- Sentences are simple and commonly used
- Tamil sentences include special tokens `<start>` and `<end>` for training

### Example:
- English: *i like coffee*  
- Tamil: *எனக்கு காபி பிடிக்கும்*

---

## 🛠️ Technologies and Tools Used
- **Programming Language:** Python
- **Deep Learning Framework:** TensorFlow & Keras
- **Model Type:** Seq2Seq with Attention
- **Neural Network:** LSTM
- **Tokenizer:** Keras Tokenizer
- **Development Environment:** Google Colab 
---

## 🧠 Machine Learning Approach
- **Learning Type:** Supervised Learning
- **Task:** Machine Translation
- **Loss Function:** Sparse Categorical Crossentropy
- **Optimizer:** Adam
- **Evaluation Metric:** Accuracy

---

## 🔄 Project Workflow
1. Prepare English and Tamil sentence pairs
2. Tokenize and convert text into sequences
3. Pad sequences to equal length
4. Build encoder using LSTM
5. Build decoder using LSTM
6. Apply attention mechanism
7. Train the model
8. Translate new English sentences into Tamil

---

## 🏗️ Model Architecture
- Encoder (Embedding + LSTM)
- Decoder (Embedding + LSTM)
- Attention Mechanism (Dot Product Attention)
- Dense Output Layer with Softmax

---

## 📁 File Structure
```

📦 TASK-12
┣ 📓 english_tamil_translation_attention.ipynb
┗ 📄 README.md

```

---

## ▶️ Steps to Run the Project
1. Open Google Colab or Jupyter Notebook
2. Upload the notebook file
3. Run all cells sequentially
4. Wait for the model to train
5. Test translation using sample sentences

---

## ✅ Sample Output
```

English : i like coffee
Tamil   : எனக்கு காபி பிடிக்கும்

```

---

## 🎯 Learning Outcomes
- Understanding Encoder–Decoder models
- Implementation of Attention mechanism
- Hands-on experience with Seq2Seq models
- Basics of Neural Machine Translation
- Handling text preprocessing and tokenization

---

## 👩‍💻 Author Information
Divya A  

---
