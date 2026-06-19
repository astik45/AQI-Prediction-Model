# 🌫️ AQI Prediction App

A web application that predicts the Air Quality Index (AQI) based on pollutant concentrations using a **Random Forest Regressor** model. Built with **Streamlit** and deployed live.

**[Try the live app here](https://aqi-prediction-model-astik45.streamlit.app/)**

---

## Overview

This project takes six key air pollutant values as input and estimates the AQI. The model was trained on a synthetically generated dataset (500 samples) with an **R² score of 0.96**, which means it captures patterns reasonably well for a demo/simulation tool.

### Input Pollutants
| Pollutant | Description | Typical Range |
|-----------|-------------|---------------|
| PM2.5 | Fine particulate matter (µg/m³) | 0 – 500 |
| PM10 | Coarse particulate matter (µg/m³) | 0 – 600 |
| NO₂ | Nitrogen dioxide (µg/m³) | 0 – 300 |
| SO₂ | Sulfur dioxide (µg/m³) | 0 – 200 |
| CO | Carbon monoxide (mg/m³) | 0 – 10 |
| O₃ | Ozone (µg/m³) | 0 – 200 |

### Output Categories
| AQI Range | Category |
|-----------|----------|
| 0 – 50 | Good ✅ |
| 51 – 100 | Moderate ⚠️ |
| 100+ | Unhealthy 🚫 |

---

## Model

- **Algorithm:** Random Forest Regressor (100 estimators)
- **Training set:** 400 samples (80% split)
- **Test set:** 100 samples (20% split)
- **Performance:**
  - Mean Squared Error: **67.36**
  - R² Score: **0.96**

---

## 🗂️ Project Structure

```
AQI_Prediction/
├── app.py                    # Streamlit web app
├── aqi_Model_train.ipynb     # Model training notebook
├── aqi_dataset_sample.csv    # Dataset (500 records)
├── trained_model.pkl         # Serialized model
├── requirements.txt          # Python dependencies
└── README.md
```

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/astik45/AQI-Prediction-Model.git
cd AQI-Prediction-Model

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```

---

## 🛠️ Tech Stack

- **Python** — core logic & data processing
- **scikit-learn** — Random Forest model
- **pandas / numpy** — data handling
- **joblib** — model serialization
- **Streamlit** — web UI & deployment

---

## ⚠️ Disclaimer

This model was trained on a small synthetic dataset and is **not intended for real-world use**. It's a learning/demo project to illustrate how machine learning can be applied to environmental data.

