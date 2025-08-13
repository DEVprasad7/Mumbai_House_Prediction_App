import pandas as pd
import numpy as np
import joblib

model = joblib.load('model.pkl')

LOCATION_COLUMNS = ['total_sqft',
 'bhk',
 'Agripada',
 'Airoli',
 'Ambernath East',
 'Ambernath West',
 'Andheri East',
 'Andheri West',
 'Anjurdive',
 'Badlapur East',
 'Badlapur West',
 'Bandra Kurla Complex',
 'Bandra West',
 'Bhandup East',
 'Bhandup West',
 'Bhayandar East',
 'Bhayandar West',
 'Bhiwandi',
 'Boisar',
 'Borivali East',
 'Borivali West',
 'Byculla',
 'Chembur',
 'Cuffe Parade',
 'Dadar East',
 'Dadar West',
 'Dahisar',
 'Deonar',
 'Diva',
 'Dombivali',
 'Dronagiri',
 'Dundare',
 'Fort',
 'Ghansoli',
 'Ghatkopar East',
 'Ghatkopar West',
 'Girgaon',
 'Goregaon East',
 'Goregaon West',
 'Jogeshwari East',
 'Jogeshwari West',
 'Juhu',
 'Kalamboli',
 'Kalwa',
 'Kalyan East',
 'Kalyan West',
 'Kamathipura',
 'Kamothe',
 'Kandivali East',
 'Kandivali West',
 'Kanjurmarg',
 'Kanjurmarg East',
 'Karanjade',
 'Karjat',
 'Kasheli',
 'Khar',
 'Khar West',
 'Kharghar',
 'Khopoli',
 'Koper Khairane',
 'Koproli',
 'Kurla',
 'Lbs Marg',
 'Lower Parel',
 'Madanpura',
 'Mahim',
 'Malad East',
 'Malad West',
 'Matunga',
 'Mazagaon',
 'Mazgaon',
 'Mira Road East',
 'Mulund East',
 'Mulund West',
 'Nahur East',
 'Naigaon East',
 'Nala Sopara',
 'Nalasopara East',
 'Napeansea Road',
 'Navade',
 'Neral',
 'Nerul',
 'Nilje Gaon',
 'Palava',
 'Palghar',
 'Panvel',
 'Peddar Road',
 'Powai',
 'Prabhadevi',
 'Rabale',
 'Rasayani',
 'Sanpada',
 'Santacruz East',
 'Santacruz West',
 'Saphale',
 'Seawoods',
 'Sector-20 Koparkhairane',
 'Sewri',
 'Shahapur',
 'Shil Phata',
 'Sion',
 'Taloja',
 'Thane East',
 'Thane West',
 'Titwala',
 'Ulhasnagar',
 'Ulwe',
 'Umroli',
 'Usarghar Gaon',
 'Vangani',
 'Vasai',
 'Vasai East',
 'Vasind',
 'Vichumbe',
 'Vikhroli',
 'Vikroli East',
 'Ville Parle East',
 'Virar',
 'Wada',
 'Wadala',
 'Worli']


def preprocess_input(bhk, total_sqft, location):
    """
    Preprocess input data to match the model's expected format.
    
    Args:
        bhk (int): Number of BHK
        total_sqft (int): Total square footage
        location (str): Location name
        
    Returns:
        pd.DataFrame: Processed input data with all required features
    """
    # Create initial dataframe with numeric features
    input_dict = {
        'bhk': [bhk],
        'total_sqft': [total_sqft]
    }
    
    # Initialize all location columns to 0
    for loc in LOCATION_COLUMNS[2:]:  # Skip bhk and total_sqft
        input_dict[loc] = [0]
    
    # Convert location to match training data format
    location = location.strip().title()
    
    # Findiing the matching column name
    matching_locations = [col for col in LOCATION_COLUMNS[2:] if col.lower() == location.lower()]
    
    # Seting the matching location to 1
    if matching_locations:
        input_dict[matching_locations[0]] = [1]
    
    # Create DataFrame with all features in correct order
    df = pd.DataFrame(input_dict)
    return df[LOCATION_COLUMNS]  # Return columns in correct order

def predict_price(model, bhk, total_sqft, location):
    """
    Make a price prediction using the preprocessed input.
    
    Args:
        model: Trained model
        bhk (int): Number of BHK
        total_sqft (int): Total square footage
        location (str): Location name
        
    Returns:
        float: Predicted price
    """
    processed_input = preprocess_input(bhk, total_sqft, location)
    prediction = model.predict(processed_input)
    return prediction[0]

# def main():
#     bhk = int(input("Enter BHK: "))
#     total_sqft = int(input("Enter Area: "))
#     location = input("Location: ")

#     test = [bhk, total_sqft, ]
#     prediction = predict_price(model,bhk, total_sqft, location)

#     print(f"{prediction:.2f}")


# if __name__ == "__main__":
#     main()