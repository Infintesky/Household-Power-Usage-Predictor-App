import numpy as np
from config import beta_values

def predict_power_usage(beta: np.ndarray, temp: float, humidity: float, wind: float) -> float:
    """
    Predict power usage based on temperature, humidity, and wind speed using
    a provided beta coefficient vector.

    Args:
        beta (np.ndarray): A 4x1 array containing regression coefficients.
        temp (float): Temperature value (°C).
        humidity (float): Humidity value (%).
        wind (float): Wind speed (kph).

    Returns:
        float: Predicted power usage.
    """
    # Construct feature vector: [1, temp, humidity, wind]
    x = np.array([[1.0], [temp], [humidity], [wind]])
    prediction = float(beta.T @ x)  # Cleaner than np.dot
    return prediction

def main() -> None:
    """Example usage of the prediction function."""
    season = "Winter"
    beta = beta_values[season]
    temp, humidity, wind = 10.0, 80.0, 10.0
    prediction = predict_power_usage(beta, temp, humidity, wind)
    print(f"Predicted power usage for {season}: {prediction:.2f}")


if __name__ == "__main__":
    main()
