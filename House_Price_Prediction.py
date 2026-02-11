import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dummy dataset
data = {
    'Rooms': [2, 3, 4, 3, 5, 4, 6, 2, 3, 5],
    'Size': [800, 1200, 1500, 1300, 2000, 1700, 2500, 900, 1100, 2100],
    'Location': [2, 3, 4, 3, 5, 4, 5, 2, 3, 5],
    'Age': [10, 8, 5, 7, 2, 4, 1, 12, 9, 3],
    'Price': [120000, 180000, 250000, 200000, 350000,
              300000, 420000, 110000, 160000, 370000]
}

df = pd.DataFrame(data)

X = df[['Rooms', 'Size', 'Location', 'Age']]
y = df['Price']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

new_house = np.array([[4, 1600, 4, 3]])
print("Predicted Price:", model.predict(new_house)[0])
