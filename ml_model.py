import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import root_mean_squared_error
from sklearn.model_selection import train_test_split
import pickle
import json

# Reading data
data = pd.read_csv('income_sample_data.csv')
print(data.head())

#Splitting data
X = data.drop('income', axis=1)
y = data.income
print(X.head())
print(y.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

# Creating model
model = RandomForestRegressor(n_estimators=100,
                              max_depth=3,
                              max_features= 0.7,
                              random_state=42)
model.fit(X_train, y_train)

#Predicting with training data
y_pred_train = model.predict(X_train)
train_rmse = root_mean_squared_error(y_pred=y_pred_train,  y_true=y_train)
print(f'Training Root Mean Squared Error is {train_rmse}')

#PRedicting with testing data
y_pred_test = model.predict(X_test)
test_rmse = root_mean_squared_error(y_pred=y_pred_test,  y_true=y_test)
print(f'Test Root Mean Squared Error is {test_rmse}')

# Saving the model
filename = 'income_model.pkl'
pickle.dump(model, open(filename, 'wb'))