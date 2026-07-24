import streamlit as st
import util

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="Bangalore House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# Load model
util.load_saved_artifacts()

# -------------------------
# Header
# -------------------------
st.title("🏠 Bangalore House Price Prediction")

st.markdown("""
Predict the estimated house price using a Machine Learning model trained on Bangalore housing data.
""")

# -------------------------
# Sidebar
# -------------------------

st.sidebar.header("House Details")

location = st.sidebar.selectbox(
    "Select Location",
    util.get_location_names()
)

sqft = st.sidebar.number_input(
    "Total Square Feet",
    min_value=300,
    max_value=10000,
    value=1000
)

bhk = st.sidebar.slider(
    "BHK",
    1,
    10,
    2
)

bath = st.sidebar.slider(
    "Bathrooms",
    1,
    10,
    2
)

# -------------------------
# Prediction
# -------------------------

if st.button("Predict Price"):

    price = util.get_estimated_price(
        location,
        sqft,
        bhk,
        bath
    )

    st.success(f"Estimated Price: ₹ {price:.2f} Lakhs")

# -------------------------
# About
# -------------------------

st.divider()

st.subheader("Model Information")

st.write("""
- Linear Regression
- Dataset: Bangalore House Prices
- Features:
    - Location
    - Total Sqft
    - BHK
    - Bathrooms
""")