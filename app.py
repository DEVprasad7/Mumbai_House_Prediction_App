import streamlit as st
import joblib

model = joblib.load("model.pkl")

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
        "🏢 House / Apartment Type",
        ("BHK"),
        index=None,
        placeholder="Select",
    )
    type = st.number_input(f"Number Of {type_o if type_o else 'Units'}", min_value=1, value=1)

with col2:
    Location_list = [
                        'Agripada','Airoli','Ambernath','Andheri',
                        'Anjurdive','Badlapur','Bandra','Bandra Kurla Complex',
                        'Bhandup','Bhayandar','Bhiwandi','Boisar',
                        'Borivali','Byculla','Chembur','Cuffe Parade',
                        'Dadar','Dahisar','Deonar','Diva',
                        'Dombivali','Dronagiri','Dundare','Fort',
                        'Ghansoli','Ghatkopar','Girgaon','Goregaon',
                        'Jogeshwari','Juhu','Kalamboli','Kalwa',
                        'Kalyan','Kamathipura','Kamothe','Kandivali',
                        'Kanjurmarg','Karanjade','Karjat','Kasheli','Khar',
                        'Kharghar','Khopoli','Koper Khairane','Koproli',
                        'Kurla','Lbs Marg','Lower Parel','Madanpura',
                        'Mahim','Malad','Matunga','Mazagaon',
                        'Mazgaon','Mira Road','Mulund','Nahur','Naigaon',
                        'Nala Sopara','Nalasopara','Napeansea Road''Navade',
                        'Neral','Nerul','Nilje Gaon','Palava','Palghar','Panvel',
                        'Peddar Road','Powai','Prabhadevi','Rabale',
                        'Rasayani','Sanpada','Santacruz','Saphale',
                        'Seawoods','Sector-20 Koparkhairane','Sewri','Shahapur',
                        'Shil Phata','Sion','Taloja','Thane','Titwala',
                        'Ulhasnagar','Ulwe','Umroli','Usarghar Gaon',
                        'Vangani','Vasai','Vasind','Vichumbe','Vikhroli',
                        'Vikroli','Ville Parle','Virar','Wada','Wadala','Worli'
                    ]
    Location = st.text_input("📍 Enter the location").strip().capitalize()
    Location_input = Location_list.index(Location)
    Total_area = st.number_input("📐 Area of Apartment (sq ft)", min_value=100, value=100, max_value=4000)

