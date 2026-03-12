import pandas as pd
from lstm_trajectory import train_lstm, predict_next_position

model, scaler = train_lstm()

data = pd.read_csv("../data/trajectory_data.csv")

sequence = data[['x','y','z','vx','vy','vz']].values[-10:]

prediction = predict_next_position(model, scaler, sequence)

print("Predicted next satellite position:")
print(prediction)