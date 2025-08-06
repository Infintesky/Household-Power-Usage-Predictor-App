import streamlit as st
from datetime import datetime
from config import beta_values, season_params
from predict_power import predict_power_usage
from realtime import get_weather_data, extract_weather_info, get_api_key
from get_season import get_season_from_month

# Determine default season from current month
default_season = get_season_from_month(datetime.now().month)

# Set default season in session state
if "selected_season" not in st.session_state:
    st.session_state.selected_season = default_season

# Store fetched weather data in session state
for key in ["temperature", "humidity", "wind_speed"]:
    st.session_state.setdefault(key, None)



# Streamlit app 
st.set_page_config(page_title="Household Power Usage Predictor - UK (London)")
st.header("Household Power Usage Predictor - UK (London)")

# Season selector
season = st.selectbox(
    "Select a season:",
    ("Winter", "Spring", "Summer", "Fall"),
    index=("Winter", "Spring", "Summer", "Fall").index(st.session_state.selected_season)
)

st.session_state.selected_season = season

# Check if season changed and clear cache
if 'previous_season' not in st.session_state or st.session_state.previous_season != season:
    st.cache_data.clear()
    st.session_state.previous_season = season
    st.rerun()

# Get selected beta
beta = beta_values[season]

# Get season-specific parameter limits
params = season_params[season]

# Input fields for user data (with realtime defaults if available)
st.subheader("Enter Weather Conditions:")

# Button to autofill using realtime weather data
if st.button("Autofill With Realtime Weather Data (London)"):
    try:
        api_key = get_api_key()
        weather_data = get_weather_data(api_key, location="London")
        weather_info = extract_weather_info(weather_data)

        st.session_state.temperature = weather_info["temperature"]
        st.session_state.humidity = weather_info["humidity"]
        st.session_state.wind_speed = weather_info["wind_speed"]

        st.info(f"Fetched: Temperature 🌡️ {weather_info['temperature']}°C | Humidity 💧 {weather_info['humidity']}% | Wind Speed 🌬️ {weather_info['wind_speed']} km/h")

    except Exception as e:
        st.error(f"Failed to fetch realtime weather data: {e}")

temperature = st.number_input(
    "Temperature (°C)",
    min_value=params["temp_min"],
    max_value=params["temp_max"],
    value=st.session_state.temperature if st.session_state.temperature is not None and st.session_state.temperature > params["temp_min"] else params["temp_val"],
    step=0.1
)

humidity = st.number_input(
    "Humidity (%)",
    min_value=params["humidity_min"],
    max_value=params["humidity_max"],
    value=st.session_state.humidity if st.session_state.humidity is not None and st.session_state.humidity > params["humidity_min"] else params["humidity_val"],
    step=1.0
)

wind_speed = st.number_input(
    "Wind Speed (km/h)",
    min_value=params["wind_min"],
    max_value=params["wind_max"],
    value=st.session_state.wind_speed if st.session_state.wind_speed is not None and st.session_state.wind_speed > params["wind_min"] else params["wind_val"],
    step=0.1
)

# Prediction button
if st.button("Predict Power Usage per Household"):
    result = predict_power_usage(beta, temperature, humidity, wind_speed)
    st.success(f"Estimated Power Usage per Household: **{result:.2f} kWh**")
