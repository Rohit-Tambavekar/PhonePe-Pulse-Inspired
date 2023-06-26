import pandas as pd

path = "D:/Guvi/Projects/PhonePe/preprocesseddata/"

agg_map_state_trans_df = pd.read_csv(path + "state_map_trans_data.csv")
all_state_district_df = pd.read_csv(path + "state_district_lat.csv")

import pandas as pd

path = "D:/Guvi/Projects/PhonePe/preprocesseddata/"

agg_map_state_trans_df = pd.read_csv(path + "state_map_trans_data.csv")
all_state_district_df = pd.read_csv(path + "all_district_lat_long_data.csv")

agg_map_state_trans_df['Latitude'] = None
agg_map_state_trans_df['Longitude'] = None
agg_map_state_trans_df['State'] = agg_map_state_trans_df['State'].str.strip()
agg_map_state_trans_df['District'] = agg_map_state_trans_df['District'].str.strip()
all_state_district_df['State'] = all_state_district_df['State'].str.strip()
all_state_district_df['District'] = all_state_district_df['District'].str.strip()


for index_lat, rows_lat in enumerate(all_state_district_df['District']):
    for index_map, row_map in enumerate(agg_map_state_trans_df['District']):
        if rows_lat == row_map:
            agg_map_state_trans_df['Latitude'].iloc[index_map] = all_state_district_df['Latitude'].iloc[index_lat]
            agg_map_state_trans_df['Longitude'].iloc[index_map] = all_state_district_df['Longitude'].iloc[index_lat]

pd.set_option('display.max_rows',None)
# print(agg_map_state_trans_df.isnull().sum())
filtered = agg_map_state_trans_df[['District', 'Latitude', 'Longitude']][(agg_map_state_trans_df['Latitude'].isnull()) | (agg_map_state_trans_df['Longitude'].isnull())]
print(filtered)




