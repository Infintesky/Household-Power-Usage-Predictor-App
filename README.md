# Household Power Usage Predictor - UK (London)

## About the App

The **Household Power Usage Predictor - UK (London)** is a web application designed to assist in predicting estimated power usage of a household based on features such as temperature, humidity and wind speed. It is developed for **SUTD DTP III** and is built using [streamlit](https://streamlit.io/).

This application leverages user inputs and a predictive model to provide insightful information about estimated power usage in a household with regards to the season, aiding in demand forecasting for energy companies, infrastructure planning by informing decisions on grid upgrades and energy resource allocation.

---

## Get Started

Follow these steps to get the app up and running:

### Prerequisites

Make sure you have the following installed on your system:
- Python 3.13 or later
- `pipenv` for dependency management (install it using `pip install pipenv` if not already installed)

### Installation Steps

1. Install the required dependencies using pipenv:
    ```bash
    python -m pipenv install
    ```

2. Activate the virtual environment:
    ```bash
    python -m pipenv shell
    ```

3. Run the Flask app:
    ```bash
    streamlit run app/app.py
    ```

4. Access the app in your browser at the following URL:
    ```bash
    http://localhost:8501
    ```