"""
Project: Agri-Bot - AI Agricultural Price Predictor
Author: Tasimudzwa Vision Makoni
Purpose: Using Machine Learning to forecast market trends for 
         small-scale farmers in Zimbabwe.
Framework: TensorFlow / Keras
"""

import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. DATA SIMULATION (Representing Historical Market Prices)
# In a production environment, this would be replaced with a CSV of ZWL/USD market rates.
def load_agri_data():
    np.random.seed(42)
    # Creating 1000 data points (Days, Seasonality, Historical Price)
    days = np.arange(1000).reshape(-1, 1)
    prices = 50 + (0.5 * days) + (10 * np.sin(days / 50)) + np.random.normal(0, 2, (1000, 1))
    return days, prices

# 2. PREPROCESSING
X, y = load_agri_data()
scaler_x = StandardScaler()
scaler_y = StandardScaler()

X_scaled = scaler_x.fit_transform(X)
y_scaled = scaler_y.fit_transform(y)

# Splitting into Training (80%) and Testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_test_size=0.2)

# 3. MODEL ARCHITECTURE (Neural Network)
model = Sequential([
    Dense(64, activation='relu', input_shape=(1,)),
    Dropout(0.2), # Preventing Overfitting
    Dense(32, activation='relu'),
    Dense(1)      # Output layer for Regression (Price Prediction)
])

# 4. COMPILATION
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

# 5. TRAINING
print("Starting Training...")
model.fit(X_train, y_train, epochs=50, batch_size=32, verbose=0)

# 6. EVALUATION
loss, mae = model.evaluate(X_test, y_test)
print(f"Model Evaluation - Loss: {loss:.4f}, Mean Absolute Error: {mae:.4f}")

# 7. PREDICTION LOGIC
def predict_price(day_number):
    day_scaled = scaler_x.transform([[day_number]])
    prediction_scaled = model.predict(day_scaled)
    return scaler_y.inverse_transform(prediction_scaled)[0][0]

# Testing a prediction for Day 1005
test_day = 1005
predicted_val = predict_price(test_day)
print(f"Predicted Market Price for Day {test_day}: ${predicted_val:.2f}")