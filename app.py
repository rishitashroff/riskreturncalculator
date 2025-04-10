"""
DS4420: Data Mining & Machine Learning 2
Final Project
Calvin Li & Rishita Shroff

Data Collection & Pre-processing
"""

import streamlit as st
import project.py as p

# project title
st.title("Stock Return Prediction")

stock_input = st.input_text("Enter a ticker (e.g. AAPL)", value="AAPL")

if st.button("Predict"):
    st.subheader(f"Model Prediction for {stock}")

    df, X_train, X_test, y_train, y_test = test_train_split(stock)

    pred_plot = lstm(X_train, X_test, y_train, y_test)
    
    st.write("Prediction completed!!")
