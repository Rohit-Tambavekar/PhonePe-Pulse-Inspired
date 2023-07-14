# Importing libraries required
import os
import git
import json
import pandas as pd
from geopy.geocoders import Nominatim


#defining paths for clonned dir

state_district_path = "D:/Guvi/Projects/PhonePe/state/state_districts.csv"

# Defining constant
all_csv_names = [
                    "state_trans_data",
                    "state_user_data",
                    "state_map_trans_data",
                    "state_map_user_data",
                    "top_state_trans_data",
                    "top_state_user_data",
                    "top_state_user_pin_data",
                    "top_state_trans_pin_data",
                    "all_district_lat_long_data",
                    "all_state_lat_long_data"
                ]

state_groups = {
                    'Northern Region': ['Jammu and Kashmir', 'Himachal Pradesh', 'Punjab', 'Chandigarh', 'Uttarakhand', 'Ladakh',
                                        'Delhi', 'Haryana'],
                    'Central Region': ['Uttar Pradesh', 'Madhya Pradesh', 'Chhattisgarh'],
                    'Western Region': ['Rajasthan', 'Gujarat', 'Dadra and Nagar Haveli and Daman and Diu', 'Maharashtra'],
                    'Eastern Region': ['Bihar', 'Jharkhand', 'Odisha', 'West Bengal', 'Sikkim'],
                    'Southern Region': ['Andhra Pradesh', 'Telangana', 'Karnataka', 'Kerala', 'Tamil Nadu', 'Puducherry', 'Goa',
                                        'Lakshadweep', 'Andaman and Nicobar Islands'],
                    'North-Eastern Region': ['Assam', 'Meghalaya', 'Manipur', 'Nagaland', 'Tripura', 'Arunachal Pradesh', 'Mizoram']
                }


def get_state_district_lat_long_df():
    
    all_state_district_df = pd.read_csv(state_district_path)
    
    all_state_district_df['District']=(all_state_district_df['District']
                                                    .str.replace(r'\(.*\)','')
                                                    .str.replace('Lahaul \&amp\; Spiti', 'Lahul and Spiti')
                                                    .str.replace('Jayashankar Bhoopalpally','Bhupalpally')
                                                    .str.replace('Shamali','Shamli')
                                                    .str.replace('Bithra','Bitra')
                                                    .str.replace('Chethlath','Chetlat')
                                                    .str.replace('Kilthan','Kilthan Island')
                                                    .str.replace('Kanshiram Nagar','Kasganj')
                                                    
                                    )
    all_state_district_df['State']=all_state_district_df['State'].str.replace(r'\(.*\)','')
    
    # Initialize geocoder
    geolocator = Nominatim(user_agent='my_geocoder')

    # Create empty columns for latitude and longitude
    all_state_district_df['Latitude'] = None
    all_state_district_df['Longitude'] = None
    

    # Iterate over each row in the DataFrame
    for index, row in all_state_district_df.iterrows():
        state = row['State']
        district = row['District']
        
        # Create the address string for district
        district_address = f'{district}, {state}, India'
        
        try:
            # Geocode the district address
            district_location = geolocator.geocode(district_address)
            
            # Extract latitude and longitude for district
            district_latitude = district_location.latitude
            district_longitude = district_location.longitude
            
            # Assign latitude and longitude to the DataFrame for district
            all_state_district_df.at[index, 'Latitude'] = district_latitude
            all_state_district_df.at[index, 'Longitude'] = district_longitude
            
        except:
            print(f'Geocoding failed for district: {district_address}')
    
  
    pd.set_option('display.max_columns', None)
    print(all_state_district_df)
    return all_state_district_df

def get_state_trans_csv(all_state_district_df):
    path = "D:/Guvi/Projects/PhonePe/preprocesseddata"
    if not os.path.exists(path):
        os.makedirs(path)
    
    
    # save the DataFrame to a CSV file in the specified directory
    file_path = os.path.join(path, "state_district_lat.csv") 
    all_state_district_df.to_csv(file_path, index=False)
    
all_state_district_df = get_state_district_lat_long_df()

get_state_trans_csv(all_state_district_df)

# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(agg_trans_state_df)



