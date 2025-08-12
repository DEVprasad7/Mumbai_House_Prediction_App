import streamlit as st
import joblib
from data_preprocessor import predict_price, LOCATION_COLUMNS

# Load the trained model
model = joblib.load('model.pkl')

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

st.markdown('<h1 class="title">🏠 Mumbai House Price Prediction 💵</h1>', unsafe_allow_html=True)
st.write("Estimate the price of a house in Mumbai based on its Type, Location, and Total Square Feet.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    type_o = st.selectbox(
        "🏢 House Type",
        ("BHK"),
        index=None,
        placeholder="Select",
    )
    type = st.number_input(f"Number Of {type_o if type_o else 'Units'}", min_value=1, value=1)

with col2:
    # Get unique locations from LOCATION_COLUMNS (skip bhk and total_sqft)
    locations = sorted([loc for loc in LOCATION_COLUMNS[2:]])
    Location = st.selectbox('Select Location', locations)
    Total_area = st.number_input("📐 Area of Apartment (sq ft)", min_value=100, value=100, max_value=4000)


# --- Format Function ---
def format_price(price):
    if price >= 1_00:
        return f"{price/1_00:.1f} Cr"
    else:
        return f"{price:.1f} Lakhs"

# --- Prediction Button ---
st.markdown("---")
if st.button("🔮 Predict Price"):
    if not Location or not type or not Total_area or not type_o:
        st.error("⚠️ Please fill all the fields!")
    else:
        st.balloons()
        prediction = predict_price(model, type, Total_area, Location)
        formatted_price = format_price(prediction)
        st.markdown(f'<div class="prediction-box">Estimated Price: {formatted_price}</div>', unsafe_allow_html=True)
        st.divider()
        st.caption("All The Price Estimation Made By The Model Are Based On The Data That Was Used To Train This Model")
        
    