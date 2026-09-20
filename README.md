# 🏠 House Price Prediction using Linear Regression

A machine learning project that predicts **house prices** based on property features such as the number of rooms, house size, location rating, and property age.

The project uses **Linear Regression** to learn the relationship between house characteristics and their prices, and evaluates the model using **Mean Squared Error (MSE)** and **R² Score**.

---

## 📌 Project Overview

House price prediction is a common machine learning regression problem.

In this project, a simple dataset containing information about houses is used to train a **Linear Regression model**. The trained model can then estimate the price of a new house based on its characteristics.

### Input Features

* 🛏️ **Rooms** — Number of rooms in the house
* 📐 **Size** — House size in square feet
* 📍 **Location** — Numerical location rating
* 🕐 **Age** — Age of the property in years

### Target

* 💰 **Price** — House price

---

## 🎯 Objectives

The main objectives of this project are to:

* Build a basic regression model for house price prediction
* Train a Linear Regression model using property features
* Split the dataset into training and testing sets
* Evaluate model performance
* Predict the price of a new house

---

## 🧠 Machine Learning Workflow

```text
House Dataset
      ↓
Data Preparation
      ↓
Feature Selection
      ↓
Train/Test Split
      ↓
Linear Regression
      ↓
Model Training
      ↓
Price Prediction
      ↓
Model Evaluation
```

---

## 📊 Dataset

This project uses a **dummy dataset** containing 10 house records.

| Feature  | Description                  |
| -------- | ---------------------------- |
| Rooms    | Number of rooms              |
| Size     | Property size in square feet |
| Location | Numerical location rating    |
| Age      | Property age in years        |
| Price    | House price                  |

Example:

| Rooms |  Size | Location | Age |   Price |
| ----: | ----: | -------: | --: | ------: |
|     2 |   800 |        2 |  10 | 120,000 |
|     3 | 1,200 |        3 |   8 | 180,000 |
|     4 | 1,500 |        4 |   5 | 250,000 |
|     5 | 2,000 |        5 |   2 | 350,000 |
|     6 | 2,500 |        5 |   1 | 420,000 |

> **Note:** This is a demonstration dataset. For a production-level application, a larger real-world housing dataset would be required.

---

## 🔧 Technologies Used

* **Python**
* **Pandas** — Data manipulation
* **NumPy** — Numerical operations
* **Scikit-learn** — Machine learning and evaluation

### Machine Learning Algorithm

**Linear Regression**

Linear Regression models the relationship between input variables and a continuous target variable such as house price.

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/FatimaZulfiqarAli-123/house-price-prediction.git
```

### 2. Navigate to the project directory

```bash
cd house-price-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

Run the Python script:

```bash
python house_price_prediction.py
```

The program will:

1. Create the dataset
2. Separate features and target
3. Split the data into training and testing sets
4. Train the Linear Regression model
5. Generate predictions
6. Calculate MSE and R² Score
7. Predict the price of a new house

---

## 🏗️ Model Training

The selected features are:

```python
X = df[['Rooms', 'Size', 'Location', 'Age']]
```

The target variable is:

```python
y = df['Price']
```

The dataset is divided into:

* **80% training data**
* **20% testing data**

using:

```python
train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
```

---

## 📈 Model Evaluation

Two evaluation metrics are used.

### Mean Squared Error (MSE)

MSE measures the average squared difference between the actual and predicted prices.

```python
mean_squared_error(y_test, y_pred)
```

A lower MSE generally indicates smaller prediction errors.

### R² Score

R² measures how well the model explains the variation in the target variable.

```python
r2_score(y_test, y_pred)
```

An R² value closer to **1** indicates that the model explains more of the variation in the target data.

---

## 🏠 Example Prediction

The model is used to predict the price of a new house with:

```python
new_house = np.array([[4, 1600, 4, 3]])
```

This represents:

| Feature  |       Value |
| -------- | ----------: |
| Rooms    |           4 |
| Size     | 1,600 sq ft |
| Location |           4 |
| Age      |     3 years |

The model then generates the estimated house price:

```python
model.predict(new_house)
```

---

## 📁 Project Structure

```text
house-price-prediction/
│
├── house_price_prediction.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 📄 Requirements

Create a `requirements.txt` file containing:

```text
pandas
numpy
scikit-learn
```
