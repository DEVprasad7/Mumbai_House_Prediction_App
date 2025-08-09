import streamlit as st
import joblib
import numpy as np

# Load the model
model = joblib.load("model.pkl")

# --- Custom CSS Styling ---
st.markdown("""
    <style>
        .title {
            font-size: 2rem;
            color: #1f77b4;
            font-weight: bold;
        }
        .prediction-box {
            padding: 15px;
            background-color: #f0f2f6;
            border-radius: 10px;
            text-align: center;
            font-size: 1.5rem;
            font-weight: bold;
            border: 2px solid #1f77b4;
            color: #1f77b4;
        }
        .stButton>button {
            background-color: #1f77b4;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stButton>button:hover {
            background-color: #10527a;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# --- App Title ---
st.markdown('<h1 class="title">🏠 Mumbai House Price Prediction 💵</h1>', unsafe_allow_html=True)
st.write("Estimate the price of a house in Mumbai based on its Type, Location, and Total Square Feet.")

st.markdown("---")

# --- Input Layout ---
col1, col2 = st.columns(2)

with col1:
    type_o = st.selectbox(
        "🏢 House / Apartment Type",
        ("BHK", "RK", "RK Studio"),
        index=None,
        placeholder="Select",
    )
    type = st.number_input(f"Number Of {type_o if type_o else 'Units'}", min_value=1, value=1)

with col2:
    Location = st.text_input("📍 Enter the location").strip().capitalize()
    Total_area = st.number_input("📐 Area of Apartment (sq ft)", min_value=0, value=100)

# Convert location & city to numeric
Location_ascii = sum(ord(ch) for ch in str(Location))
City_ascii = sum(ord(ch) for ch in str("Mumbai"))

X = [[type, Location_ascii, City_ascii, Total_area]]

# --- Format Function ---
def format_price(price):
    if price >= 1_00_00_000:
        return f"{price/1_00_00_000:.1f} Cr"
    elif price >= 1_00_000:
        return f"{price/1_00_000:.1f} Lakhs"
    else:
        return f"{price:,.1f}"

# --- Prediction Button ---
st.markdown("---")
if st.button("🔮 Predict Price"):
    if not Location or not type or not Total_area:
        st.error("⚠️ Please fill all the fields!")
    else:
        st.balloons()
        X_array = np.array(X)
        prediction = model.predict(X_array)[0]
        formatted_price = format_price(prediction)
        st.markdown(f'<div class="prediction-box">Estimated Price: {formatted_price}</div>', unsafe_allow_html=True)
