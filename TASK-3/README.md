# 🌦️ Weather Precipitation Prediction using Linear Regression

This project implements a **Linear Regression model** to predict **precipitation** using real-world **weather data**. The model is trained using important weather parameters such as **maximum temperature, minimum temperature, and wind speed**.  
The performance of the model is evaluated using standard regression metrics like **MAE, MSE, RMSE, and R² Score**.

---

## 📌 Project Objective

To develop a machine learning model that predicts **precipitation** based on weather features and to evaluate its accuracy using different **model performance metrics**.

---

## 📊 Dataset Details

- **Source:** Kaggle – [WEATHER PREDICTION](https://www.kaggle.com/datasets/ananthr1/weather-prediction)
- **File Format:** CSV
- **Target Variable:** `precipitation`
- **Input Features Used:**
  - `temp_max`
  - `temp_min`
  - `wind`

Missing values are handled using the following step in the code:

```python
df = df.dropna(subset=features + [target])
````

---

## 🛠️ Technologies & Tools Used

* Python
* Jupyter Notebook
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## ⚙️ Machine Learning Algorithm

* **Linear Regression**

Linear Regression is a supervised machine learning algorithm used for predicting continuous values by finding the best-fitting linear relationship between input variables and the target variable.

---

## 📈 Model Evaluation Metrics

The model performance is evaluated using the following regression metrics:

* **MAE (Mean Absolute Error)**
  Measures the average absolute difference between actual and predicted values.

* **MSE (Mean Squared Error)**
  Measures the average of the squared differences between actual and predicted values.

* **RMSE (Root Mean Squared Error)**
  Square root of MSE, provides error in the same unit as the target variable.

* **R² Score (Coefficient of Determination)**
  Indicates how well the independent variables explain the variance in the target variable.

---

## 📁 File Structure

```
task 3/
│
├── weather_data.csv                      # Weather dataset
├── Weather_Model_Performance.ipynb       # Jupyter Notebook containing the code
└── README.md                             # Project documentation
```

---

## ▶️ Steps to Run the Project

1. Open the **task 3** folder.
2. Ensure that the dataset file (`weather_data.csv`) is present in the folder.
3. Open the notebook file `Weather_Model_Performance.ipynb` using Jupyter Notebook or VS Code.
4. Run each cell sequentially.
5. Observe the output:

   * Printed values of MAE, MSE, RMSE, and R²
   * Pairplot visualization
   * Actual vs Predicted precipitation graph
   * Residual plot for error analysis

---

## ✅ Expected Output

* Numerical values for:

  * Mean Absolute Error (MAE)
  * Mean Squared Error (MSE)
  * Root Mean Squared Error (RMSE)
  * R² Score
* Visualizations:

  * Feature relationship plots
  * Actual vs Predicted values graph
  * Residual error plot

---

## 🎯 Conclusion

This project successfully demonstrates the use of **Linear Regression** for predicting **precipitation** using weather data. By evaluating the model using MAE, MSE, RMSE, and R² Score, the accuracy and reliability of the model can be clearly understood.

---

## 🎓 Learning Outcomes

Through this project, the following concepts were learned:

- Understanding of weather datasets and data preprocessing
- Application of Linear Regression for prediction tasks
- Calculation of MAE, MSE, RMSE, and R² Score
- Visualization of model performance using graphs
- Interpretation of regression evaluation metrics

---

## 👩‍💻 Author Information

**Name:** Divya A  
**Course:** B.Tech – Artificial Intelligence and Machine Learning  
**College:** Bannari Amman Institute of Technology  
**Academic Year:** 2025–2026
