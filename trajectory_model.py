import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error


def train_model():

    data = pd.read_csv("trajectory_data.csv")

    # Input features
    X = data[['x','y','z','vx','vy','vz']]

    # Target future position
    y = data[['x','y','z']].shift(-1)

    X = X[:-1]
    y = y[:-1]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2
    )

    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mse = mean_squared_error(y_test, predictions)

    print("Model trained")
    print("MSE:", mse)

    return model


def predict_next_position(model, current_state):

    prediction = model.predict([current_state])

    return prediction