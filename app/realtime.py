import os
import requests
from dotenv import load_dotenv
from typing import Any, Dict, Optional

load_dotenv() # Load from .env file

def get_api_key() -> str:
    """
    Retrieves the API key from environment variable or returns a fallback key.

    Returns:
        str: API key for WeatherAPI.
    """
    # Ideally, it will be from .env but for this purpose, I will just leave it here for your convenience.
    # In production, you should set this in your environment variables.
    return os.getenv("WEATHER_API_KEY") or "e406b1bef8ec43b497e33630250608" 


def get_weather_data(api_key: str, location: str = "London") -> Dict[str, Any]:
    """
    Fetches current weather data from WeatherAPI.

    Args:
        api_key (str): API key for authentication.
        location (str): Location to fetch weather for.

    Returns:
        dict: JSON response from WeatherAPI.

    Raises:
        Exception: If the API call fails.
    """
     
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching weather data: {response.status_code} - {response.text}")


def extract_weather_info(weather_data: Dict[str, Any]) -> Dict[str, Optional[float]]:
    """
    Extracts temperature, humidity, and wind speed from the weather data.

    Args:
        weather_data (dict): JSON response from WeatherAPI.

    Returns:
        dict: Dictionary with temperature, humidity, and wind speed.
    """
    current = weather_data.get("current", {})
    fetched = {
        "temperature": current.get("temp_c"),
        "humidity": current.get("humidity"),
        "wind_speed": current.get("wind_kph")
    }
    return {k: float(v) for k, v in fetched.items()}


def main():
    """
    Main function to demonstrate weather data retrieval and extraction.
    """
    api_key = get_api_key()
    current_weather_data = get_weather_data(api_key)

    try:
        return extract_weather_info(current_weather_data)
    except Exception as e:
        print(f"Failed to extract weather info: {e}")
        return None


if __name__ == "__main__":
    main()