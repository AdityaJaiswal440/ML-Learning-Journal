import streamlit as st

col1, col2 = st.columns([2, 1])

with col1:
    st.title("Customer Churn Dashboard")
    st.write("Analyze customer behavior and predict retention.")

with col2:
    st.sidebar.header("Model Settings")
    threshold = st.sidebar.slider("Certainty Threshold", 0.0, 1.0, 0.5)