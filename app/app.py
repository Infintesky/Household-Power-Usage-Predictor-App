import streamlit as st
from library import beta_values, season_params, predict_power_usage

st.set_page_config(
    page_title="Household Power Usage Predictor - UK (London)"
)

st.header("Household Power Usage Predictor - UK (London)")

# Initialize session state for season tracking
if 'previous_season' not in st.session_state:
    st.session_state.previous_season = None

season = st.selectbox(
    "Select a season:",
    ("Winter", "Spring", "Summer", "Fall")
)

# Check if season changed and clear cache
if st.session_state.previous_season != season:
    st.cache_data.clear()  # Clear all cached data
    st.session_state.previous_season = season
    st.rerun()  # Rerun the app to refresh inputs

# Get selected beta
beta = beta_values[season]

# Get seasons parameters
params = season_params[season]

# Input fields for user data
st.subheader("Enter Weather Conditions:")

temperature = st.number_input("Temperature (°C)", min_value=params["temp_min"], max_value=params["temp_max"], value=params["temp_val"], step=1.0)
humidity = st.number_input("Humidity (%)", min_value=params["humidity_min"], max_value=params["humidity_max"], value=params["humidity_val"], step=1.0)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=params["wind_min"], max_value=params["wind_max"], value=params["wind_val"], step=1.0)

# Button to trigger prediction
if st.button("Predict Power Usage per Household"):
    result = predict_power_usage(beta, temperature, humidity, wind_speed)
    st.success(f"Estimated Power Usage per Household: **{result:.2f} kWh**")
