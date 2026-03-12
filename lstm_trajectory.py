import numpy as np
import pandas as pd

from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

def load_dataset():

    data = pd.read_csv("../data/trajectory_data.csv")

    features = data[['x','y','z','vx','vy','vz']].values

    return features


def prepare_sequences(data, seq_len=10):

    X = []
    y = []

    for i in range(len(data)-seq_len):

        X.append(data[i:i+seq_len])
        y.append(data[i+seq_len][:3])

    return np.array(X), np.array(y)


def train_lstm():

    print("Training LSTM trajectory model...")

    data = load_dataset()

    scaler = MinMaxScaler()

    data_scaled = scaler.fit_transform(data)

    X, y = prepare_sequences(data_scaled)

    model = Sequential()

    model.add(LSTM(64, input_shape=(X.shape[1], X.shape[2])))

    model.add(Dense(32))

    model.add(Dense(3))

    model.compile(
        optimizer="adam",
        loss="mse"
    )

    model.fit(
        X,
        y,
        epochs=20,
        batch_size=32
    )

    model.save("../models/lstm_model.h5")

    print("LSTM model saved")

    return model, scaler


def predict_next_position(model, scaler, sequence):

    sequence_scaled = scaler.transform(sequence)

    sequence_scaled = sequence_scaled.reshape(1, sequence_scaled.shape[0], sequence_scaled.shape[1])

    prediction = model.predict(sequence_scaled)

    pred = scaler.inverse_transform(
        np.hstack((prediction, np.zeros((1,3))))
    )[0][:3]

    return pred