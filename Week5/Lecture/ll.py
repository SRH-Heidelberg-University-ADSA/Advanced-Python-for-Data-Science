import pickle

import numpy as np
from sklearn.linear_model import LinearRegression

X_train = np.array([[30], [50], [70], [90]])
Y_train = np.array([8, 12, 16, 24])

model = LinearRegression()
model.fit(X_train, Y_train)

print(f" slope is : {model.coef_[0]}  ")
print(f"intercept : {model.intercept_:.2f}")

# test = 110
# prediction = model.predict([[test]])[0]

# print(f"prediction is : {prediction:.1f}")

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("model saved")
