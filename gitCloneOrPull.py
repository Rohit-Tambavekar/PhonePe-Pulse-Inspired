# Importing libraries required
import os
import git
import json
import pandas as pd
import numpy as np
from geopy.geocoders import Nominatim


#defining paths for clonned dir
repo_path = "D:/Guvi/Projects/PhonePe/pulse"
repo_path_state_trans = repo_path+"/data/aggregated/transaction/country/india/state"
repo_path_state_user = repo_path+"/data/aggregated/user/country/india/state"
repo_path_map_state_trans = repo_path+"/data/map/transaction/hover/country/india/state"
repo_path_map_state_user = repo_path+"/data/map/user/hover/country/india/state"
repo_path_top_state_trans = repo_path+"/data/top/transaction/country/india/state"
repo_path_top_state_user = repo_path+"/data/top/user/country/india/state"
state_district_path = "D:/Guvi/Projects/PhonePe"



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
                    "all_state_lat_long_data"
                ]

all_csv_names_lat = [
                    "state_map_trans_data",
                    "state_map_user_data",
                    "top_state_trans_data",
                    "top_state_user_data"
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
# all_csv_names = ["uniq_state"]
# geolocator = Nominatim(user_agent="gitCloneOrPull")

# Clone the git repository and if present pull request for the same repository
def get_git_clone_pull(repo_path):
    if os.path.isdir(os.path.join(repo_path, ".git")):
        # Repository data already exists, so pull changes
        repo = git.Repo(repo_path)
        origin = repo.remote(name="origin")
        origin.pull()
    else:
        # Repository data does not exist, so clone the repository
        try:
            git.Repo.clone_from("https://github.com/PhonePe/pulse.git", repo_path)
            repo = git.Repo(repo_path)
        except git.exc.GitCommandError as e:
            print("Error: ", e)
    # Removing unwanted files
    repo_path_readme = repo_path+"/"+"README.md"
    print(repo_path_readme)
    os.remove(repo_path_readme)
    # Renaming directories
    directory = os.path.join(repo_path, 'data')
    for root, dirs, files in os.walk(directory):
        if 'state' in dirs:
            state_dir = os.path.join(root, 'state')
            for state_folder in os.listdir(state_dir):
                # rename the state folder
                old_path = os.path.join(state_dir, state_folder)
                new_path = os.path.join(state_dir, state_folder.title().replace('-', ' ').replace('&', 'and'))
                os.rename(old_path, new_path)
    print("Renamed all sub-directories successfully")

# Getting the aggregate state transactions files from clonned directories
def get_state_trans_df():
    agg_trans_dict = {
                        'State':[],
                        'Year':[],
                        'Quarter':[],
                        'Transaction_type':[],
                        'Transaction_count':[],
                        'Transaction_amount':[]
                    }
    
    agg_trans_st_names = os.listdir(repo_path_state_trans)
    #agg_trans_st_path = ""
    for states in agg_trans_st_names:
        agg_trans_st_path = repo_path_state_trans+"/"+states
        st_year = os.listdir(agg_trans_st_path)
        for year in st_year:
            agg_trans_st_year_path = agg_trans_st_path+"/"+year+"/"
            agg_trans_st_year = os.listdir(agg_trans_st_year_path)
            for json_files in agg_trans_st_year:
                json_file_name = agg_trans_st_year_path+json_files
                json_data = open(json_file_name, 'r')
                data = json.load(json_data)
                
                for elem in data['data']['transactionData']:
                                Name = elem['name']
                                count = elem['paymentInstruments'][0]['count']
                                amount = elem['paymentInstruments'][0]['amount']
                                agg_trans_dict['Transaction_type'].append(Name)
                                agg_trans_dict['Transaction_count'].append(count)
                                agg_trans_dict['Transaction_amount'].append(amount)
                                agg_trans_dict['State'].append(states)
                                agg_trans_dict['Year'].append(year)
                                agg_trans_dict['Quarter'].append('Q'+json_files.strip('.json'))
    agg_trans_state_df = pd.DataFrame(agg_trans_dict)
    agg_trans_state_df.insert(
                                0,
                                'Region', agg_trans_state_df['State']
                                .map({state: region for region, states in state_groups.items() for state in states})
                            )
    
    
    return agg_trans_state_df


def get_state_user_df():
    agg_user_dict = {
                        'State': [],
                        'Year': [],
                        'Quarter': [],
                        'Brand': [],
                        'Brand_count': [],
                        'Brand_percentage': []
                    }
    
    agg_user_st_names = os.listdir(repo_path_state_user)
    for states in agg_user_st_names:
        agg_user_st_path = repo_path_state_user+"/"+states
        st_year = os.listdir(agg_user_st_path)
        for year in st_year:
            agg_user_st_year_path = agg_user_st_path+"/"+year+"/"
            agg_trans_st_year = os.listdir(agg_user_st_year_path)
            for json_files in agg_trans_st_year:
                json_file_name = agg_user_st_year_path+json_files
                json_data = open(json_file_name, 'r')
                data = json.load(json_data)
                try:
                    for elem in data['data']['usersByDevice']:
                        brand = elem['brand']
                        count = elem['count']
                        percentage = elem['percentage']

                        agg_user_dict['Brand'].append(brand)
                        agg_user_dict['Brand_count'].append(count)
                        agg_user_dict['Brand_percentage'].append(percentage)
                        agg_user_dict['State'].append(states)
                        agg_user_dict['Year'].append(year)
                        agg_user_dict['Quarter'].append('Q'+json_files.strip('.json'))
                except:
                    pass
    agg_user_state_df = pd.DataFrame(agg_user_dict)
    agg_user_state_df.insert(
                                0,
                                'Region', agg_user_state_df['State']
                                .map({state: region for region, states in state_groups.items() for state in states})
                            )
    
    
    return agg_user_state_df


def get_map_state_trans_df():
    map_trans_dict = {
                        'State': [],
                        'District': [],
                        'Year': [],
                        'Quarter': [],
                        'Transaction_count': [],
                        'Transaction_amount': []
                    }

    
    agg_trans_st_names = os.listdir(repo_path_map_state_trans)
    #agg_trans_st_path = ""
    for states in agg_trans_st_names:
        agg_trans_st_path = repo_path_map_state_trans+"/"+states
        st_year = os.listdir(agg_trans_st_path)
        for year in st_year:
            agg_trans_st_year_path = agg_trans_st_path+"/"+year+"/"
            agg_trans_st_year = os.listdir(agg_trans_st_year_path)
            for json_files in agg_trans_st_year:
                json_file_name = agg_trans_st_year_path+json_files
                json_data = open(json_file_name, 'r')
                data = json.load(json_data)
                
                try:
                    for elem in data['data']["hoverDataList"]:
                        district = elem['name']
                        trans_count = elem['metric'][0]['count']
                        trans_amount = elem['metric'][0]['amount']
                        map_trans_dict['District'].append(
                                                            district.title()
                                                            .replace(' And', ' and')
                                                            .replace('andaman', 'Andaman')
                                                            .replace('District','')
                                                            .replace('Nicobars','Nicobar')
                                                            .replace('Ribhoi','Ri Bhoi')
                                                            .replace('North Twenty Four Parganas','North 24 Parganas')
                                                            .replace('South Twenty Four Parganas','South 24 Parganas')
                                                        )
                        map_trans_dict['Transaction_count'].append(trans_count)
                        map_trans_dict['Transaction_amount'].append(trans_amount)
                        map_trans_dict['State'].append(states)
                        map_trans_dict['Year'].append(year)
                        map_trans_dict['Quarter'].append('Q'+json_files.strip('.json'))
                except TypeError:
                    pass
    agg_map_trans_dict_df = pd.DataFrame(map_trans_dict)
    
    delhi_filter = agg_map_trans_dict_df['State'] == 'Delhi'
    for index, row in agg_map_trans_dict_df.loc[delhi_filter].iterrows():
        district = row['District']
        if not district.endswith('Delhi') and 'Delhi' not in district:
            agg_map_trans_dict_df.at[index, 'District'] = district + ' Delhi'
            
    sikkim_filter = agg_map_trans_dict_df['State'] == 'Sikkim'
    for index, row in agg_map_trans_dict_df.loc[sikkim_filter].iterrows():
        district = row['District']
        if not district.endswith('Sikkim') and 'Sikkim' not in district:
            agg_map_trans_dict_df.at[index, 'District'] = district + ' Sikkim'
    
    agg_map_trans_dict_df.insert(
                                    0, 
                                    'Region',
                                    agg_map_trans_dict_df['State']
                                    .map({state: region for region, states in state_groups.items() for state in states})
                                )
    
    agg_map_trans_dict_df['District'] = agg_map_trans_dict_df['District'].str.replace('  ',' ')
    
    return agg_map_trans_dict_df


def get_map_state_user_df():
    map_user_dict = {
                        'State': [],
                        'District': [],
                        'Year': [],
                        'Quarter': [],
                        'Registered_user': [],
                        'App_opening': []
                    }
    
    agg_trans_st_names = os.listdir(repo_path_map_state_user)
    #agg_trans_st_path = ""
    for states in agg_trans_st_names:
        agg_trans_st_path = repo_path_map_state_user+"/"+states
        st_year = os.listdir(agg_trans_st_path)
        for year in st_year:
            agg_trans_st_year_path = agg_trans_st_path+"/"+year+"/"
            agg_trans_st_year = os.listdir(agg_trans_st_year_path)
            for json_files in agg_trans_st_year:
                json_file_name = agg_trans_st_year_path+json_files
                json_data = open(json_file_name, 'r')
                data = json.load(json_data)
                
                try:
                    for elem in data['data']["hoverData"]:
                        district = elem
                        registeredUser =  data['data']["hoverData"][elem]["registeredUsers"]
                        app_opening = data['data']["hoverData"][elem]["appOpens"]
                        map_user_dict['District'].append(
                                                            district.title()
                                                            .replace(' And', ' and')
                                                            .replace('andaman', 'Andaman')
                                                            .replace('District','')
                                                            .replace('Nicobars','Nicobar')
                                                            .replace('Ribhoi','Ri Bhoi')
                                                            .replace('North Twenty Four Parganas','North 24 Parganas')
                                                            .replace('South Twenty Four Parganas','South 24 Parganas')
                                                        )
                        map_user_dict['Registered_user'].append(registeredUser)
                        map_user_dict['App_opening'].append(app_opening)
                        map_user_dict['State'].append(states)
                        map_user_dict['Year'].append(year)
                        map_user_dict['Quarter'].append('Q'+json_files.strip('.json'))
                except TypeError:
                    pass
    agg_map_user_dict_df = pd.DataFrame(map_user_dict)
    
    delhi_filter = agg_map_user_dict_df['State'] == 'Delhi'
    for index, row in agg_map_user_dict_df.loc[delhi_filter].iterrows():
        district = row['District']
        if not district.endswith('Delhi') and 'Delhi' not in district:
            agg_map_user_dict_df.at[index, 'District'] = district + ' Delhi'
            
    sikkim_filter = agg_map_user_dict_df['State'] == 'Sikkim'
    for index, row in agg_map_user_dict_df.loc[sikkim_filter].iterrows():
        district = row['District']
        if not district.endswith('Sikkim') and 'Sikkim' not in district:
            agg_map_user_dict_df.at[index, 'District'] = district + ' Sikkim'
    
    agg_map_user_dict_df.insert(
                                0,
                                'Region', agg_map_user_dict_df['State']
                                .map({state: region for region, states in state_groups.items() for state in states})
                            )
    
    agg_map_user_dict_df['District'] = agg_map_user_dict_df['District'].str.replace('  ',' ')
    
    return agg_map_user_dict_df


def get_top_state_trans_df():
    tot_trans_state_dict = {
                        'State': [],
                        'District': [],
                        'Year': [],
                        'Quarter': [],
                        'Total_transaction_count': [],
                        'Total_transaction_amount': []
                    }

    
    agg_trans_st_names = os.listdir(repo_path_top_state_trans)
    #agg_trans_st_path = ""
    for states in agg_trans_st_names:
        tot_trans_st_path = repo_path_top_state_trans+"/"+states
        st_year = os.listdir(tot_trans_st_path)
        for year in st_year:
            agg_trans_st_year_path = tot_trans_st_path+"/"+year+"/"
            agg_trans_st_year = os.listdir(agg_trans_st_year_path)
            for json_files in agg_trans_st_year:
                json_file_name = agg_trans_st_year_path+json_files
                json_data = open(json_file_name, 'r')
                data = json.load(json_data)
                
                try:
                    for elem in data['data']["districts"]:
                        district = elem['entityName']
                        tot_trans_count = elem['metric']['count']
                        trans_amount = elem['metric']['amount']
                        tot_trans_state_dict['District'].append(
                                                            district.title()
                                                            .replace(' And', ' and')
                                                            .replace('andaman', 'Andaman')
                                                            .replace('District','')
                                                            .replace('Nicobars','Nicobar')
                                                            .replace('Ribhoi','Ri Bhoi')
                                                            .replace('North Twenty Four Parganas','North 24 Parganas')
                                                            .replace('South Twenty Four Parganas','South 24 Parganas')
                                                        )
                        tot_trans_state_dict['Total_transaction_count'].append(tot_trans_count)
                        tot_trans_state_dict['Total_transaction_amount'].append(trans_amount)
                        tot_trans_state_dict['State'].append(states)
                        tot_trans_state_dict['Year'].append(year)
                        tot_trans_state_dict['Quarter'].append('Q'+json_files.strip('.json'))
                except TypeError:
                    pass
    tot_state_trans_dict_df = pd.DataFrame(tot_trans_state_dict)
    
    delhi_filter = tot_state_trans_dict_df['State'] == 'Delhi'
    for index, row in tot_state_trans_dict_df.loc[delhi_filter].iterrows():
        district = row['District']
        if not district.endswith('Delhi') and 'Delhi' not in district:
            tot_state_trans_dict_df.at[index, 'District'] = district + ' Delhi'
            
    sikkim_filter = tot_state_trans_dict_df['State'] == 'Sikkim'
    for index, row in tot_state_trans_dict_df.loc[sikkim_filter].iterrows():
        district = row['District']
        if not district.endswith('Sikkim') and 'Sikkim' not in district:
            tot_state_trans_dict_df.at[index, 'District'] = district + ' Sikkim'
    
    tot_state_trans_dict_df.insert(
                                    0,
                                    'Region', tot_state_trans_dict_df['State']
                                    .map({state: region for region, states in state_groups.items() for state in states})
                                )
    
    tot_state_trans_dict_df['District'] = tot_state_trans_dict_df['District'].str.replace('  ',' ')
    
    return tot_state_trans_dict_df


def get_top_state_user_df():
    tot_user_state_dict = {
                        'State': [],
                        'District': [],
                        'Year': [],
                        'Quarter': [],
                        'Registered_user': []
                    }
    
    agg_trans_st_names = os.listdir(repo_path_top_state_user)
    #agg_trans_st_path = ""
    for states in agg_trans_st_names:
        agg_trans_st_path = repo_path_top_state_user+"/"+states
        st_year = os.listdir(agg_trans_st_path)
        for year in st_year:
            agg_trans_st_year_path = agg_trans_st_path+"/"+year+"/"
            agg_trans_st_year = os.listdir(agg_trans_st_year_path)
            for json_files in agg_trans_st_year:
                json_file_name = agg_trans_st_year_path+json_files
                json_data = open(json_file_name, 'r')
                data = json.load(json_data)
                try:
                    for elem in data['data']["districts"]:
                        district = elem['name']
                        registeredUser =  elem["registeredUsers"]
                        tot_user_state_dict['District'].append(
                                                            district.title()
                                                            .replace(' And', ' and')
                                                            .replace('andaman', 'Andaman')
                                                            .replace('District','')
                                                            .replace('Nicobars','Nicobar')
                                                            .replace('Ribhoi','Ri Bhoi')
                                                            .replace('North Twenty Four Parganas','North 24 Parganas')
                                                            .replace('South Twenty Four Parganas','South 24 Parganas')
                                                        )
                        tot_user_state_dict['Registered_user'].append(registeredUser)
                        tot_user_state_dict['State'].append(states)
                        tot_user_state_dict['Year'].append(year)
                        tot_user_state_dict['Quarter'].append('Q'+json_files.strip('.json'))
                except TypeError:
                    pass
    tot_state_user_dict_df = pd.DataFrame(tot_user_state_dict)
    
    delhi_filter = tot_state_user_dict_df['State'] == 'Delhi'
    for index, row in tot_state_user_dict_df.loc[delhi_filter].iterrows():
        district = row['District']
        if not district.endswith('Delhi') and 'Delhi' not in district:
            tot_state_user_dict_df.at[index, 'District'] = district + ' Delhi'
    
    sikkim_filter = tot_state_user_dict_df['State'] == 'Sikkim'
    for index, row in tot_state_user_dict_df.loc[sikkim_filter].iterrows():
        district = row['District']
        if not district.endswith('Sikkim') and 'Sikkim' not in district:
            tot_state_user_dict_df.at[index, 'District'] = district + ' Sikkim'
            
    tot_state_user_dict_df.insert(
                                    0,
                                    'Region', tot_state_user_dict_df['State']
                                    .map({state: region for region, states in state_groups.items() for state in states})
                                )
    
    tot_state_user_dict_df['District'] = tot_state_user_dict_df['District'].str.replace('  ',' ')
    
    return tot_state_user_dict_df


def get_top_state_trans_pin_df():
    tot_trans_state_pin_dict = {
                        'State': [],
                        'Pincode': [],
                        'Year': [],
                        'Quarter': [],
                        'Total_transaction_count': [],
                        'Total_transaction_amount': []
                    }

    
    agg_trans_st_names = os.listdir(repo_path_top_state_trans)
    #agg_trans_st_path = ""
    for states in agg_trans_st_names:
        tot_trans_st_path = repo_path_top_state_trans+"/"+states
        st_year = os.listdir(tot_trans_st_path)
        for year in st_year:
            agg_trans_st_year_path = tot_trans_st_path+"/"+year+"/"
            agg_trans_st_year = os.listdir(agg_trans_st_year_path)
            for json_files in agg_trans_st_year:
                json_file_name = agg_trans_st_year_path+json_files
                json_data = open(json_file_name, 'r')
                data = json.load(json_data)
                
                try:
                    for elem in data['data']["pincodes"]:
                        pincodes = elem['entityName']
                        tot_trans_count = elem['metric']['count']
                        trans_amount = elem['metric']['amount']
                        tot_trans_state_pin_dict['Pincode'].append(pincodes)
                        tot_trans_state_pin_dict['Total_transaction_count'].append(tot_trans_count)
                        tot_trans_state_pin_dict['Total_transaction_amount'].append(trans_amount)
                        tot_trans_state_pin_dict['State'].append(states)
                        tot_trans_state_pin_dict['Year'].append(year)
                        tot_trans_state_pin_dict['Quarter'].append('Q'+json_files.strip('.json'))
                except TypeError:
                    pass
    tot_state_trans_pin_dict_df = pd.DataFrame(tot_trans_state_pin_dict)
    
    tot_state_trans_pin_dict_df.insert(
                                        0,
                                        'Region', tot_state_trans_pin_dict_df['State']
                                        .map({state: region for region, states in state_groups.items() for state in states})
                                    )
    
    return tot_state_trans_pin_dict_df


def get_top_state_user_pin_df():
    tot_user_state_pin_dict = {
                        'State': [],
                        'Pincode': [],
                        'Year': [],
                        'Quarter': [],
                        'Registered_user': []
                    }
    
    agg_trans_st_names = os.listdir(repo_path_top_state_user)
    #agg_trans_st_path = ""
    for states in agg_trans_st_names:
        agg_trans_st_path = repo_path_top_state_user+"/"+states
        st_year = os.listdir(agg_trans_st_path)
        for year in st_year:
            agg_trans_st_year_path = agg_trans_st_path+"/"+year+"/"
            agg_trans_st_year = os.listdir(agg_trans_st_year_path)
            for json_files in agg_trans_st_year:
                json_file_name = agg_trans_st_year_path+json_files
                json_data = open(json_file_name, 'r')
                data = json.load(json_data)
                try:
                    for elem in data['data']["pincodes"]:
                        pincodes = elem['name']
                        registeredUser =  elem["registeredUsers"]
                        tot_user_state_pin_dict['Pincode'].append(pincodes)
                        tot_user_state_pin_dict['Registered_user'].append(registeredUser)
                        tot_user_state_pin_dict['State'].append(states)
                        tot_user_state_pin_dict['Year'].append(year)
                        tot_user_state_pin_dict['Quarter'].append('Q'+json_files.strip('.json'))
                except TypeError:
                    pass
    # for key in tot_user_state_pin_dict.keys():
    #     print(f"{key}: {len(tot_user_state_pin_dict[key])}")
    
    tot_state_user_pin_dict_df = pd.DataFrame(tot_user_state_pin_dict)
    
    tot_state_user_pin_dict_df.insert(
                                        0,
                                        'Region', tot_state_user_pin_dict_df['State']
                                        .map({state: region for region, states in state_groups.items() for state in states})
                                    )
    
    return tot_state_user_pin_dict_df


def get_state_lat_long_df():
    all_state_district_dict = {
                        'State': [],
                        'District': []
                    }
    
    agg_trans_st_names = os.listdir(repo_path_map_state_trans)
    #agg_trans_st_path = ""
    for states in agg_trans_st_names:
        agg_trans_st_path = repo_path_top_state_user+"/"+states
        st_year = os.listdir(agg_trans_st_path)
        for year in st_year:
            agg_trans_st_year_path = agg_trans_st_path+"/"+year+"/"
            agg_trans_st_year = os.listdir(agg_trans_st_year_path)
            for json_files in agg_trans_st_year:
                json_file_name = agg_trans_st_year_path+json_files
                json_data = open(json_file_name, 'r')
                data = json.load(json_data)
                try:
                    for elem in data['data']["districts"]:
                        district = elem['name']
                        all_state_district_dict['District'].append(
                                                            district.title()
                                                            .replace(' And', ' and')
                                                            .replace('andaman', 'Andaman')
                                                            .replace('District','')
                                                            .replace('Nicobars','Nicobar')
                                                            .replace('Ribhoi','Ri Bhoi')
                                                            .replace('North Twenty Four Parganas','North 24 Parganas')
                                                            .replace('South Twenty Four Parganas','South 24 Parganas')
                                                        )
                        all_state_district_dict['State'].append(states)
                except TypeError:
                    pass
    all_state_district_df = pd.DataFrame(all_state_district_dict)
    all_state_district_df = all_state_district_df[['State', 'District']].drop_duplicates(subset=['District'])
    all_state_df = all_state_district_df['State'].drop_duplicates().reset_index(drop = True).to_frame(name='State')
    
    # Initialize geocoder
    geolocator = Nominatim(user_agent='my_geocoder')

    # Create empty columns for latitude and longitude
    all_state_district_df['Latitude'] = None
    all_state_district_df['Longitude'] = None
    all_state_df['Latitude'] = None
    all_state_df['Longitude'] = None
    
        
    for index, row in all_state_df.iterrows():
        state = row['State']    
        # Create the address string for state
        state_address = f'{state}, India'
        try:
            # Geocode the state address
            state_location = geolocator.geocode(state_address)
            
            # Extract latitude and longitude for state
            state_latitude = state_location.latitude
            state_longitude = state_location.longitude
            
            # Assign latitude and longitude to the DataFrame for state
            all_state_df.at[index, 'Latitude'] = state_latitude
            all_state_df.at[index, 'Longitude'] = state_longitude
            
        except:
            print(f'Geocoding failed for state: {state_address}')

    
    all_state_df.insert(
                                        0,
                                        'Region', all_state_df['State']
                                        .map({state: region for region, states in state_groups.items() for state in states})
                                    )

    return all_state_df


def get_state_trans_csv(all_user_df,all_csv_names):
    path = "D:/Guvi/Projects/PhonePe/preprocesseddata"
    if not os.path.exists(path):
        os.makedirs(path)
    
    for df_index,dataFs in enumerate(all_user_df):
        # save the DataFrame to a CSV file in the specified directory
        file_path = os.path.join(path, all_csv_names[df_index]+".csv") 
        dataFs.to_csv(file_path, index=False)
    

def get_all_lat_long_district(agg_map_state_trans_df):
    
    path = "D:/Guvi/Projects/PhonePe/preprocesseddata/"
    
    all_state_district_df = pd.read_csv(path+"state_district_lat.csv")

    agg_map_state_trans_df['District']=(
                                        agg_map_state_trans_df['District']
                                                        .str.replace('Spsr Nellore', 'Nellore')
                                                        .str.replace('Ysr', 'YSR Kadapa')
                                                        .str.replace('South Salmara Mancachar', 'South Salmara-Mankachar')
                                                        .str.replace('Marigaon', 'Morigaon')
                                                        .str.replace('Pashchim Champaran', 'West Champaran')
                                                        .str.replace('Kaimur Bhabua', 'Kaimur')
                                                        .str.replace('Purbi Champaran', 'East Champaran')
                                                        .str.replace('Janjgir Champa', 'Janjgir-Champa')
                                                        .str.replace('Marigaon', 'Morigaon')
                                                        .str.replace('  ', ' ')
                                                        .str.replace('Shahdara  Delhi', 'Shahdara')
                                                        .str.replace('Devbhumi Dwarka', 'Devbhoomi Dwarka')
                                                        .str.replace('Aravallis', 'Aravalli')
                                                        .str.replace('Chhotaudepur', 'Chhota Udepur')
                                                        .str.replace('Mahesana', 'Mehsana')
                                                        .str.replace('The Dangs', 'Dangs')
                                                        .str.replace('Panch Mahals', 'Panchmahal')
                                                        .str.replace('Sabar Kantha', 'Sabarkantha')
                                                        .str.replace('Banas Kantha', 'Banaskantha')
                                                        .str.replace('Ahmadabad', 'Ahmedabad')
                                                        .str.replace('Dohad', 'Dahod')
                                                        .str.replace('Hazaribagh', 'Hazaribag')
                                                        .str.replace('Saraikela Kharsawan', 'Seraikela-Kharsawan')
                                                        .str.replace('Sahebganj', 'Sahibganj')
                                                        .str.replace('Chikkaballapura', 'Chikballapur')
                                                        .str.replace('Davanagere', 'Davangere')
                                                        .str.replace('Bagalkote', 'Bagalkot')
                                                        .str.replace('Chamarajanagara', 'Chamarajanagar')
                                                        .str.replace('Leh Ladakh', 'Leh')
                                                        .str.replace('Mumbai', 'Mumbai City')
                                                        .str.replace('Mumbai City Suburban', 'Mumbai Suburban')
                                                        .str.replace('Anugul', 'Angul')
                                                        .str.replace('Jajapur', 'Jajpur')
                                                        .str.replace('Baleshwar', 'Balasore')
                                                        .str.replace('Puducherry', 'Pondicherry')
                                                        .str.replace('Firozepur', 'Ferozepur')
                                                        .str.replace('Ganganagar', 'Sri Ganganagar')
                                                        .str.replace('Kancheepuram', 'Kanchipuram')
                                                        .str.replace('Thoothukkudi', 'Thoothukudi')
                                                        .str.replace('The Nilgiris', 'Nilgiris')
                                                        .str.replace('Kanniyakumari', 'Kanyakumari')
                                                        .str.replace('Thiruvallur', 'Tiruvallur')
                                                        .str.replace('Thiruvarur', 'Tiruvarur')
                                                        .str.replace('Warangal Rural', 'Warangal')
                                                        .str.replace('Kumuram Bheem Asifabad', 'Komaram Bheem Asifabad')
                                                        .str.replace('Peddapalle', 'Peddapalli')
                                                        .str.replace('Mahbubnagar', 'Mahabubnagar')
                                                        .str.replace('Jaya Shankar Bhalupally', 'Bhupalpally')
                                                        .str.replace('Warangal Urban', 'Warangal')
                                                        .str.replace('Siddharthnagar', 'Siddharth Nagar')
                                                        .str.replace('Sant Kabeer Nagar', 'Sant Kabir Nagar')
                                                        .str.replace('Bara Banki', 'Barabanki')
                                                        .str.replace('Rae Bareli', 'RaeBareli')
                                                        .str.replace('Maldah', 'Malda')
                                                        .str.replace('Darjiling', 'Darjeeling')
                                                        .str.replace('Gurugram', 'Gurgaon')
                                                        .str.replace('Shahdara Delhi', 'Shahdara')
                                                        .str.replace('Medchal Malkajgiri', 'Medchal')
                                                        .str.replace('Kheri', 'Lakhimpur - Kheri')
        

                                    )
    agg_map_state_trans_df['State'] = (
                            agg_map_state_trans_df['State']
                                                    .str.replace('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli')
                                        )

    all_state_district_df['State'] = (
                            all_state_district_df['State']
                                                    .str.replace('  ', ' ')
                                        )

    all_state_district_df['District'] = (
                            all_state_district_df['District']
                                                    .str.replace('  ', ' ')
                                                    .str.replace('Androth', 'Lakshadweep')
                                                    .str.replace('Dadra & Nagar Haveli', 'Dadra and Nagar Haveli')
                                        )

    agg_map_state_trans_df['Latitude'] = None
    agg_map_state_trans_df['Longitude'] = None

    agg_map_state_trans_df['State'] = agg_map_state_trans_df['State'].str.strip()
    agg_map_state_trans_df['District'] = agg_map_state_trans_df['District'].str.strip()
    all_state_district_df['State'] = all_state_district_df['State'].str.strip()
    all_state_district_df['District'] = all_state_district_df['District'].str.strip()



    for index_lat, rows_lat in enumerate(all_state_district_df['District']):
        for index_map,row_map in enumerate(agg_map_state_trans_df['District']):
            if rows_lat == row_map:
                agg_map_state_trans_df['Latitude'].at[index_map] = all_state_district_df['Latitude'].iloc[index_lat]
                agg_map_state_trans_df['Longitude'].at[index_map] = all_state_district_df['Longitude'].iloc[index_lat]
                
    return agg_map_state_trans_df


def all_dist_lat(all_dist_lat_list):
    all_dist_lat_return = []
    for index,df in enumerate(all_dist_lat_list):
        dfs = get_all_lat_long_district(df)
        print(dfs)
        # if index == 0:
        #     agg_map_state_trans_df = dfs
        # elif index == 1:
        #     agg_map_state_user_df = dfs
        # elif index == 2:
        #     top_state_trans_df = dfs
        # elif index == 3:
        #     top_state_user_df = dfs
        all_dist_lat_return.append(dfs)
    # all_dist_lat_return.append(agg_map_state_trans_df)
    # all_dist_lat_return.append(agg_map_state_user_df)
    # all_dist_lat_return.append(top_state_trans_df)
    # all_dist_lat_return.append(top_state_user_df)
    
    return all_dist_lat_return


def get_warangal_back(all_dist_lat_list):
    all_dist_lat_return_war = []
    old_value = 'Warangal'
    new_value = 'Warangal Rural'

    for df in all_dist_lat_list:
        indices = np.where(df['District'] == old_value)[0]

        # Check if the count is even and greater than or equal to 8
        if len(indices) % 2 == 0 and len(indices) >= 4:
            # Iterate over the indices and change alternate occurrences
            for i in range(1, len(indices), 2):
                df.at[indices[i], 'District'] = new_value
        all_dist_lat_return_war.append(df)
        
        
    # all_dist_lat_return_war.append(agg_map_state_trans_df)
    # all_dist_lat_return_war.append(agg_map_state_user_df)
    # all_dist_lat_return_war.append(top_state_trans_df)
    # all_dist_lat_return_war.append(top_state_user_df)
    
    return all_dist_lat_return_war


def preprocessing_data(all_user_df):
    
    pd.set_option('display.max_rows', 10)
    pd.set_option('display.max_columns', None)
    
    # for df_name in all_user_df:
    #     for name, val in globals().items():
    #         if val is df_name:
    #             print(name)
    #             pass
    #     print(f"{df_name} :")    
    #     print(f"Null count: \n{df_name.isnull().sum()}")
    #     print(f"Duplicated rows count: \n{df_name.duplicated().sum()}")
    #     print(f"Unique values count: \n{df_name.nunique()}")
    #     print(df_name.shape)
    #     print(df_name.dtypes)
    #     print(f"Descrbe : \n{df_name.describe()}")
    #     print('DATAFRAME INFO:\n')
    #     print(df_name.info())
    #     print("\n", 50 * "*-*", "\n")

    #  There are 2 null values in top_state_trans_pin_df
    # top_state_trans_pin_df = pd.read_csv('D:/Guvi/Projects/PhonePe/preprocesseddata/top_state_trans_pin_data.csv')

    # Create a boolean mask for the null values
    null_mask = top_state_trans_pin_df.isna().any(axis=1)

    # Select only the rows with null values
    null_rows = top_state_trans_pin_df[null_mask]

    # Print the boolean mask
    # pd.set_option('display.max_rows', 100)
    # Convert the Year column to a string type column
    top_state_trans_pin_df['Year'] = top_state_trans_pin_df['Year'].astype(str)
    top_state_trans_pin_df['Pincode'] = top_state_trans_pin_df['Pincode'].fillna(194105)
    # print(top_state_trans_pin_df.dtypes)
    
    # Create a boolean mask for the desired state and year values
    # mask = (top_state_trans_pin_df['State'] == 'Ladakh') & (top_state_trans_pin_df['Year'].isin(['2019', '2020']))

    # Select the rows that match the boolean mask
    # selected_rows = top_state_trans_pin_df.loc[mask, :]

    # Print the selected rows
    # print(selected_rows)
    
    all_user_df[7] = top_state_trans_pin_df
    
    # pd.set_option('display.max_rows', None)
    # pd.set_option('display.max_columns', None)
    mask = (all_user_df[7]['State'] == 'Ladakh') & (all_user_df[7]['Quarter'] == 'Q4') & (all_user_df[7]['Year'].isin(['2020', '2019']))
    selected_rows = all_user_df[7].loc[mask, ['Pincode', 'Quarter', 'Year']]

    # Print the selected rows
    print(selected_rows)
    
    for df_name in all_user_df:
        for name, val in locals().items():
            if val is df_name:
                print("Local variable name:", name)
        for name, val in globals().items():
            if val is df_name:
                print("Global variable name:", name)
        print(f"Null count: \n{df_name.isnull().sum()}")
        
    
        
    return all_user_df,top_state_trans_pin_df


# get_git_clone_pull(repo_path) #################
agg_trans_state_df = get_state_trans_df()
agg_user_state_df = get_state_user_df()
agg_map_state_trans_df = get_map_state_trans_df()
agg_map_state_user_df = get_map_state_user_df()
top_state_trans_df = get_top_state_trans_df()
top_state_user_df = get_top_state_user_df()
top_state_user_pin_df = get_top_state_user_pin_df()
top_state_trans_pin_df = get_top_state_trans_pin_df()
all_state_df = get_state_lat_long_df()


all_dist_lat_list = [
                agg_map_state_trans_df,
                agg_map_state_user_df,
                top_state_trans_df,
                top_state_user_df
]
all_dist_lat_list_return = all_dist_lat(all_dist_lat_list)

all_dist_lat_return_war = get_warangal_back(all_dist_lat_list_return)

all_user_df = [
                agg_trans_state_df,
                agg_user_state_df,
                agg_map_state_trans_df,
                agg_map_state_user_df,
                top_state_trans_df,
                top_state_user_df,
                top_state_user_pin_df,
                top_state_trans_pin_df,
                all_state_df
               ]

get_state_trans_csv(all_user_df,all_csv_names)
get_state_trans_csv(all_dist_lat_return_war,all_csv_names_lat)

all_user_df,top_state_trans_pin_df = preprocessing_data(all_user_df)


get_state_trans_csv(all_user_df,all_csv_names)
get_state_trans_csv(all_dist_lat_return_war,all_csv_names_lat)

agg_trans_state_df, agg_user_state_df, agg_map_state_trans_df, agg_map_state_user_df, top_state_trans_df, top_state_user_df, top_state_user_pin_df, top_state_trans_pin_df, all_state_df = all_user_df
agg_map_state_trans_df, agg_map_state_user_df, top_state_trans_df, top_state_user_df = all_dist_lat_return_war


# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(agg_trans_state_df)



