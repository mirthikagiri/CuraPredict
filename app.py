import streamlit as st
import joblib
import pandas as pd
import plotly.graph_objects as go



st.set_page_config(
    page_title="CuraPredict",
    page_icon="🏥",
    layout="wide"
)



model = joblib.load("models/icu_model.pkl")



if "history" not in st.session_state:
    st.session_state.history = []


st.title("🏥 CuraPredict")

st.subheader(
    "Machine Learning-Powered ICU Capacity Planning & Demand Forecasting Platform"
)

st.markdown("""
**CuraPredict** helps healthcare administrators forecast ICU bed requirements,
assess operational risk, and make proactive resource allocation decisions using
machine learning-driven scenario analysis.
""")

st.divider()


st.header("Hospital Operational Parameters")

col1, col2 = st.columns(2)

with col1:

    emergency_admissions = st.number_input(
        "Emergency Admissions",
        min_value=0,
        value=20
    )

    scheduled_surgeries = st.number_input(
        "Scheduled Surgeries",
        min_value=0,
        value=10
    )

    current_occupancy = st.slider(
        "Current Occupancy (%)",
        min_value=0,
        max_value=100,
        value=75
    )

    infection_index = st.slider(
        "Infection Index",
        min_value=0.0,
        max_value=10.0,
        value=3.0
    )

with col2:

    avg_stay = st.number_input(
        "Average Stay (days)",
        min_value=0.0,
        value=5.0
    )

    monthly_footfall = st.number_input(
        "Average Monthly Patient Footfall",
        min_value=0,
        value=3000
    )

    ambulance_available = st.selectbox(
        "Ambulance Service Available",
        [0, 1],
        help="0 = No, 1 = Yes"
    )

    ambulance_count = st.number_input(
        "Count of Ambulance",
        min_value=0,
        value=5
    )

    emergency_beds = st.number_input(
        "Number of Beds in Emergency Wards",
        min_value=0,
        value=25
    )



if st.button("Predict ICU Demand", use_container_width=True):

    input_df = pd.DataFrame([[
        emergency_admissions,
        scheduled_surgeries,
        current_occupancy,
        infection_index,
        avg_stay,
        monthly_footfall,
        ambulance_available,
        ambulance_count,
        emergency_beds
    ]], columns=[
        'Emergency Admissions',
        'Scheduled Surgeries',
        'Current Occupancy (%)',
        'Infection Index',
        'Avg Stay (days)',
        'Average Monthly Patient Footfall',
        'Ambulance Service Available',
        'Count of Ambulance',
        'Number of Beds in Emergency Wards'
    ])

    prediction = round(model.predict(input_df)[0])



    st.session_state.history.append({
        "Predicted ICU Beds": prediction,
        "Emergency Admissions": emergency_admissions,
        "Occupancy (%)": current_occupancy
    })

    st.divider()

   

    st.subheader("ICU Demands Results")

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text': "Predicted ICU Beds"},
        gauge={
            'axis': {'range': [0, 300]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 110], 'color': "lightgreen"},
                {'range': [110, 207], 'color': "yellow"},
                {'range': [207, 300], 'color': "red"}
            ]
        }
    ))

    st.plotly_chart(
        fig,
        use_container_width=True
    )



    st.subheader("Key Metrics")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Predicted ICU Beds",
            prediction
        )

    with c2:
        st.metric(
            "Current Occupancy",
            f"{current_occupancy}%"
        )

    with c3:
        st.metric(
            "Emergency Admissions",
            emergency_admissions
        )

    st.divider()

 

    st.subheader("Risk Assessment")

    if prediction < 110:

        st.success("🟢 LOW DEMAND RISK")

        st.info("""
### Recommended Actions

- Maintain current staffing levels
- Continue routine hospital operations
- Monitor ICU occupancy trends
- Maintain emergency readiness
""")

    elif prediction < 207:

        st.warning("🟡 MODERATE DEMAND RISK")

        st.info("""
### Recommended Actions

- Prepare additional ICU staff
- Review bed allocation strategy
- Monitor emergency admissions closely
- Ensure ambulance availability
- Review resource utilization
""")

    else:

        st.error("🔴 HIGH DEMAND RISK")

        st.info("""
### Recommended Actions

- Activate surge capacity planning
- Increase ICU staffing immediately
- Prepare additional ICU beds
- Review ventilator availability
- Delay non-critical procedures
- Escalate hospital resource planning
""")
   

    st.subheader("Executive Summary")

    if prediction < 110:

        st.success(f"""
CuraPredict forecasts a LOW ICU demand scenario with an estimated requirement of
{prediction} ICU beds.

Current operational conditions indicate sufficient capacity to manage expected demand
without major resource escalation.
""")

    elif prediction < 207:

        st.warning(f"""
CuraPredict forecasts a MODERATE ICU demand scenario with an estimated requirement of
{prediction} ICU beds.

Hospital administrators should closely monitor occupancy trends and prepare contingency
resources if admissions continue increasing.
""")

    else:
        st.error(f"""
CuraPredict forecasts a HIGH ICU demand scenario with an estimated requirement of
{prediction} ICU beds.

Immediate resource planning is recommended, including staffing adjustments,
capacity expansion, and emergency preparedness measures.
""")
    st.caption(
    "Model Performance: R² = 0.9907 | MAE = 4.19 | RMSE = 5.32"
)


if len(st.session_state.history) > 0:

    st.divider()

    st.header("Prediction History")

    history_df = pd.DataFrame(
        st.session_state.history
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )