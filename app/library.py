import numpy as np

beta_values = {
    "Winter": np.array([[13.38187998], [-0.82521816], [0.2493265], [0.29571266]]),
    "Spring": np.array([[11.2438524], [-1.61426629], [0.28645975], [0.05123477]]),
    "Summer": np.array([[8.62916928], [-0.11681827], [0.0509714], [0.08119708]]),
    "Fall": np.array([[10.5263], [-0.95269846], [0.29176881], [0.0400927]])
}

season_params = {
    "Winter": {
        "temp_min": -10.0, "temp_max": 15.0, "temp_val": 10.0,
        "humidity_min": 70.0, "humidity_max": 100.0, "humidity_val": 80.0,
        "wind_min": 0.0, "wind_max": 35.0, "wind_val": 10.0
    },
    "Spring": {
        "temp_min": -5.0, "temp_max": 25.0,"temp_val": 10.0,
        "humidity_min": 60.0, "humidity_max": 100.0,"humidity_val": 80.0,
        "wind_min": 5.0, "wind_max": 30.0, "wind_val": 10.0
    },
    "Summer": {
        "temp_min": 5.0, "temp_max": 35.0,"temp_val": 10.0,
        "humidity_min": 55.0, "humidity_max": 100.0,"humidity_val": 80.0,
        "wind_min": 3.0, "wind_max": 25.0, "wind_val": 10.0
    },
    "Fall": {
        "temp_min": -1.0, "temp_max": 30.0, "temp_val": 10.0,
        "humidity_min": 60.0, "humidity_max": 100.0,"humidity_val": 80.0,
        "wind_min": 0.0, "wind_max": 30.0, "wind_val": 10.0
    }
}

# Prediction function
def predict_power_usage(beta: np.ndarray, temp: float, humidity: float, wind: float) -> float:
    # Construct feature vector: [1, temp, humidity, wind]
    x = np.array([[1.0], [temp], [humidity], [wind]])
    prediction = float(np.dot(beta.T, x))
    return prediction
