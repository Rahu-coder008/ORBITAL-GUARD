import os, numpy as np, joblib
from sklearn.ensemble import RandomForestRegressor

MODEL_PATH = "orbital_risk_model.pkl"
_model = None

def predict(distance_km, velocity_km_s=7.5):
    global _model
    if _model is None:
        if os.path.exists(MODEL_PATH): _model = joblib.load(MODEL_PATH)
        else:
            X = np.random.uniform(0.1, 100, (1000, 2))
            y = np.clip(1.0 - (X[:,0]/100.0) + np.random.normal(0, 0.05, 1000), 0, 1)
            _model = RandomForestRegressor(n_estimators=10).fit(X, y)
            joblib.dump(_model, MODEL_PATH)
    
    prob = float(_model.predict([[distance_km, velocity_km_s]])[0])
    levels = [("CRITICAL", 0.75), ("HIGH", 0.5), ("WARNING", 0.3), ("MEDIUM", 0.15)]
    label = next((l for l, t in levels if prob >= t), "LOW")
    return label, prob