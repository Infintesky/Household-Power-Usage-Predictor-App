import streamlit as st
from library import beta_values, predict_power_usage

st.set_page_config(
    page_title="Household Power Usage Predictor - UK (London)"
)


st.header("Household Power Usage Predictor - UK (London)")

season = st.selectbox(
    "Select a season:",
    ("Winter", "Spring", "Summer", "Fall")
)

# Get selected beta
beta = beta_values[season]

# Input fields for user data
st.subheader("Enter Weather Conditions:")

temperature = st.number_input("Temperature (°C)", min_value=-10.0, max_value=50.0, value=15.0, step=1.0)
humidity = st.number_input("Humidity (%)", min_value=50.0, max_value=100.0, value=60.0, step=1.0)
wind_speed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=35.0, value=10.0, step=1.0)

# Button to trigger prediction
if st.button("Predict Power Usage per Household"):
    result = predict_power_usage(beta, temperature, humidity, wind_speed)
    st.success(f"Estimated Power Usage per Household: **{result:.2f} kWh**")
