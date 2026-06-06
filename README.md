# 🏥 CuraPredict
ICU Capacity Planning & Demand Forecasting Platform

# Live Demo
[Launch CuraPredict](https://curapredict.streamlit.app/)

## Overview

CuraPredict is a machine learning-powered healthcare analytics platform that forecasts ICU bed requirements based on hospital operational indicators.

The platform helps administrators estimate ICU demand, assess operational risk, and make proactive resource allocation decisions.

## Features

- ICU Bed Demand Forecasting
- Interactive Streamlit Dashboard
- Risk Assessment Engine
- Operational Insights
- Prediction History Tracking

## Tech Stack

- Python
- Scikit-Learn
- Pandas
- NumPy
- Streamlit
- Plotly

## Machine Learning Models

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

## Dataset

The project uses a synthetic healthcare operations dataset generated using realistic hospital operational ranges.

Features include:

- Emergency Admissions
- Scheduled Surgeries
- Occupancy Rate
- Infection Index
- Average Stay Duration
- Ambulance Availability
- Emergency Ward Capacity

## Model Performance

The deployed Random Forest Regressor achieved:

- R² Score: 0.9907
- Mean Absolute Error (MAE): 4.19
- Root Mean Squared Error (RMSE): 5.32

The model demonstrates strong predictive performance on the generated healthcare operations dataset and was selected for deployment due to its ability to capture nonlinear relationships between hospital operational indicators and ICU bed demand.

## Future Enhancements

- Real Hospital Dataset Integration
- Explainable AI (SHAP)
- Multi-Hospital Comparison
- Resource Optimization Engine
