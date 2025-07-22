import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('trained_model.pkl')

st.set_page_config(page_title="AQI Predictor", layout="centered")
st.title("🌫️ AQI Prediction App")

st.write("Enter pollutant levels to estimate the Air Quality Index.")

# Inputs
pm25 = st.slider("PM2.5 (µg/m³)", 0.0, 500.0, 50.0)
pm10 = st.slider("PM10 (µg/m³)", 0.0, 600.0, 100.0)
no2 = st.slider("NO₂ (µg/m³)", 0.0, 300.0, 40.0)
so2 = st.slider("SO₂ (µg/m³)", 0.0, 200.0, 20.0)
co = st.slider("CO (mg/m³)", 0.0, 10.0, 1.0)
o3 = st.slider("O₃ (µg/m³)", 0.0, 200.0, 30.0)

# Prediction
if st.button("Predict AQI"):
    input_data = np.array([[pm25, pm10, no2, so2, co, o3]])
    aqi = model.predict(input_data)[0]
    
    st.success(f"Predicted AQI: {round(aqi, 2)}")

    if aqi < 50:
        st.info("Air Quality: Good 🌱")
    elif aqi < 100:
        st.warning("Air Quality: Moderate 🌤️")
    else:
        st.error("Air Quality: Unhealthy 😷")

# Model Restriction
st.markdown("---")  # Adds a horizontal line

st.markdown(
    "⚠️ This model simulates AQI prediction, but isn’t tuned for real-world accuracy."
)
