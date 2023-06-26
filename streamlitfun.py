import streamlit as st
from streamlit_option_menu import option_menu
from getFromSQL import *
import pandas as pd
import pydeck as pdk
from streamlit_elements import dashboard, elements, mui


def trans_col_map(year_dropdown, quarters, elevation,*ele_range):
    
    map_trans_df = get_map_trans_data()
    filtered_df = map_trans_df[(map_trans_df['Year'] == int(year_dropdown)) & (map_trans_df['Quarter'] == quarters)]
    
    # Define layer
    layer = pdk.Layer(
        "ColumnLayer", 
        data = filtered_df,  
        get_position=["Longitude", "Latitude"],
        radius = 6500,
        get_color = "[200,30,80,100]",
        get_elevation = "Transaction_amount",  
        elevation_scale = elevation,
        elevation_range= ele_range,  
        pickable = True,
        extruded = True,
        auto_highlight=True, 
        hexagon_side_length = 1000,
        coverage=1,
        
    )

    # Define view state 
    view_state = pdk.ViewState(
        latitude = 20.97, 
        longitude = 76.65, 
        zoom = 4,
        pitch = 50,
        bearing= -330,
    )
    
    # Create chart   
    r = pdk.Deck(
                layers = [layer],
                initial_view_state=view_state,
                tooltip = {
                    "html": "<b>District:</b> {District}<br/><b>State:</b> {State}<br/><b>Region:</b> {Region}<br/><b>Year:</b> {Year}<br/><b>Quarter:</b> {Quarter}<br/><b>Transaction Count:</b> {Transaction_count}<br/><b>Transaction Amount:</b> {Transaction_amount}<br/><b>Latitude:</b> {Latitude}<br/><b>Longitude:</b> {Longitude}",
                    "style": {
                        "color": "white",
                        "backgroundColor": "steelblue",
                    }
                } # type: ignore
        )

    # Display in Streamlit
    st.pydeck_chart(r)
   

def user_col_map(year_dropdown, quarters, elevation,*ele_range):
    map_user_df = get_map_user_data()
    # Define center point  
    filtered_df = map_user_df[(map_user_df['Year'] == int(year_dropdown)) & (map_user_df['Quarter'] == quarters)]
           
    # Define layer
    layer = pdk.Layer(
        "ColumnLayer", 
        data = filtered_df,  
        get_position=["Longitude", "Latitude"],
        radius = 6500,
        get_color = "[200,30,80,100]",
        get_elevation = "Registered_user",  
        elevation_scale = elevation,
        elevation_range=ele_range,  
        pickable = True,
        extruded = True,
        auto_highlight=True, 
        hexagon_side_length = 1000,
        coverage=1,
        
    )

    # Define view state 
    view_state = pdk.ViewState(
        latitude = 20.97, 
        longitude = 76.65, 
        zoom = 4,
        pitch = 50,
        bearing= -330,
    )
    
    # Create chart   
    r = pdk.Deck(
                layers = [layer],
                initial_view_state=view_state,
                tooltip = {
                    "html": "<b>District:</b> {District}<br/><b>State:</b> {State}<br/><b>Region:</b> {Region}<br/><b>Year:</b> {Year}<br/><b>Quarter:</b> {Quarter}<br/><b>Registered_user:</b> {Registered_user}<br/><b>App Openings:</b> {App_opening}<br/>",
                    "style": {
                        "color": "white",
                        "backgroundColor": "steelblue"
                    }
                } # type: ignore
        )

    # Display in Streamlit
    st.pydeck_chart(r)


def trans_display(year_dropdown,quarters,col3):
    
    map_trans_df = get_map_trans_data()
    agg_trans_df = get_agg_trans_data()
    top_trans_df = get_top_trans_data()
    top_trans_pin_df = get_agg_trans_pin_data()
    
    st.title(":blue[Transactions]")
    st.write("All PhonePe transactions (UPI + Cards + Wallets)")
    
    filtered_df = map_trans_df[(map_trans_df['Year'] == int(year_dropdown)) & (map_trans_df['Quarter'] == quarters)]

    # calculate the sum of Transaction_count for the filtered DataFrame
    count_all = filtered_df['Transaction_count'].sum()
    formatted_count_all = "{:,}".format(count_all)
    total_amount_trans = int(filtered_df['Transaction_amount'].sum()/10000000)
    formatted_total_amount_trans = "{:,}".format(total_amount_trans)
    total_amount_count = int(filtered_df['Transaction_amount'].sum()/filtered_df['Transaction_count'].sum())
    formatted_total_amount_count = "{:,}".format(total_amount_count)
    st.subheader(f":blue[{formatted_count_all}]")
    col3_col1, col3_col2 = col3.columns(2)
    rupee = "\u20B9"
    with col3_col1:
        st.write("Total payment value")
        st.write(f":blue[{rupee}{formatted_total_amount_trans}]")
    with col3_col2:
        st.write("Avg. transaction value")
        st.write(f":blue[{rupee}{formatted_total_amount_count}]")
    st.markdown("""<hr style="height:2px;border:none;color:#391c59;background-color:#391c59;" /> """, unsafe_allow_html=True)
    
    fil_agg_trans_df = agg_trans_df[(agg_trans_df['Year'] == int(year_dropdown)) & (agg_trans_df['Quarter'] == quarters)]
    mer_df = fil_agg_trans_df[fil_agg_trans_df['Transaction_type'] == 'Merchant payments']
    peer_df = fil_agg_trans_df[fil_agg_trans_df['Transaction_type'] == 'Peer-to-peer payments']
    recharge_df = fil_agg_trans_df[fil_agg_trans_df['Transaction_type'] == 'Recharge & bill payments']
    fin_df = fil_agg_trans_df[fil_agg_trans_df['Transaction_type'] == 'Financial Services']
    other_df = fil_agg_trans_df[fil_agg_trans_df['Transaction_type'] == 'Others']
    
    mer_sum_df = mer_df.groupby('Transaction_type')['Transaction_count'].sum().iloc[0]
    peer_sum_df = peer_df.groupby('Transaction_type')['Transaction_count'].sum().iloc[0]
    recharge_sum_df = recharge_df.groupby('Transaction_type')['Transaction_count'].sum().iloc[0]
    fin_sum_df = fin_df.groupby('Transaction_type')['Transaction_count'].sum().iloc[0]
    other_sum_df = other_df.groupby('Transaction_type')['Transaction_count'].sum().iloc[0]
    
    st.subheader(":white[Categories]")
    col3_col11, col3_col21 = col3.columns([8,4])
    with col3_col11:
        st.write(":white[Recharge & bill payments]")
        st.write(":white[Peer-to-peer ayments]")
        st.write(":white[Merchant payments]")
        st.write(":white[Financial services]")
        st.write(":white[Others]")
    with col3_col21:    
        st.write(f":blue[{int(recharge_sum_df)}]")
        st.write(f":blue[{int(peer_sum_df)}]")
        st.write(f":blue[{int(mer_sum_df)}]")
        st.write(f":blue[{int(fin_sum_df)}]")
        st.write(f":blue[{int(other_sum_df)}]")
        
    st.markdown("""<hr style="height:2px;border:none;color:#391c59;background-color:#391c59;" /> """, unsafe_allow_html=True)
    top_trans_df = top_trans_df[(top_trans_df['Year'] == int(year_dropdown)) & (top_trans_df['Quarter'] == quarters)]
    top_trans_df['Total_transaction_count'] = top_trans_df['Total_transaction_count'].astype(int)
    top_trans_state_df = top_trans_df.groupby('State').agg({'Total_transaction_count': 'sum'}).reset_index()
    sorted_top_trans_state_df = top_trans_state_df.sort_values(by='Total_transaction_count', ascending=False).head(10)
    
    top_trans_district_df = top_trans_df.groupby('District').agg({'Total_transaction_count': 'sum'}).reset_index()
    sorted_top_trans_district_df = top_trans_district_df.sort_values(by='Total_transaction_count', ascending=False).head(10)
    
    top_trans_pin_df = top_trans_pin_df[(top_trans_pin_df['Year'] == int(year_dropdown)) & (top_trans_pin_df['Quarter'] == quarters)]
    top_trans_pin_df = top_trans_pin_df.groupby('Pincode').agg({'Total_transaction_count': 'sum'}).reset_index()
    sorted_top_trans_pin_df = top_trans_pin_df.sort_values(by='Total_transaction_count', ascending=False).head(10)
    
    col3_but_col1,col3_but_col2,col3_but_col3 = st.columns(3)
    state_button = col3_but_col1.button("State")
    district_button = col3_but_col2.button("District")
    pincode_button = col3_but_col3.button("Pincode")
    
    if state_button:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_trans_state_df['State']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_trans_state_df['Total_transaction_count']:
                st.write(f":blue[{round(rows/10000000,2)}Cr]")
                
    elif district_button:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_trans_district_df['District']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_trans_district_df['Total_transaction_count']:
                st.write(f":blue[{round(rows/100000,2)}L]")
                
    elif pincode_button:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_trans_pin_df['Pincode']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_trans_pin_df['Total_transaction_count']:
                st.write(f":blue[{round(rows/100000,2)}L]")
                
    else:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_trans_state_df['State']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_trans_state_df['Total_transaction_count']:
                st.write(f":blue[{round(rows/10000000,2)}Cr]")
                
                
def user_display_unavail(year_dropdown,quarters,col3):
    map_user_df = get_map_user_data()
    top_user_df = get_top_user_data()
    top_user_pin_df = get_agg_user_pin_data()
    
    st.title(":blue[Users]")
    st.write(f"Registered PhonePe users till {quarters} {year_dropdown}")
    filtered_user_df = map_user_df[(map_user_df['Year'] == int(year_dropdown)) & (map_user_df['Quarter'] == quarters)]
    count_all = filtered_user_df['Registered_user'].sum()
    formatted_count_all = "{:,}".format(count_all)
    # total_amount_apps = int(filtered_user_df['App_opening'].sum())
    # formatted_total_amount_trans = "{:,}".format(total_amount_apps)
    
    st.subheader(f":blue[{formatted_count_all}]")
    st.write(f"PhonePe app opens in {quarters} {year_dropdown}")
    st.subheader(f":blue[Unavailable]")
    st.markdown("""<hr style="height:2px;border:none;color:#391c59;background-color:#391c59;" /> """, unsafe_allow_html=True)
    
    
    top_user_df = top_user_df[(top_user_df['Year'] == int(year_dropdown)) & (top_user_df['Quarter'] == quarters)]
    top_user_state_df = top_user_df.groupby('State').agg({'Registered_user': 'sum'}).reset_index()
    sorted_top_user_state_df = top_user_state_df.sort_values(by='Registered_user', ascending=False).head(10)
    
    top_user_district_df = top_user_df.groupby('District').agg({'Registered_user': 'sum'}).reset_index()
    sorted_top_user_district_df = top_user_district_df.sort_values(by='Registered_user', ascending=False).head(10)
    
    top_user_pin_df = top_user_pin_df[(top_user_pin_df['Year'] == int(year_dropdown)) & (top_user_pin_df['Quarter'] == quarters)]
    top_user_pin_df = top_user_pin_df.groupby('Pincode').agg({'Registered_user': 'sum'}).reset_index()
    sorted_top_user_pin_df = top_user_pin_df.sort_values(by='Registered_user', ascending=False).head(10)
    
    
    col3_but_col1,col3_but_col2,col3_but_col3 = st.columns(3)
    state_button = col3_but_col1.button("State")
    district_button = col3_but_col2.button("District")
    pincode_button = col3_but_col3.button("Pincode")
    
    if state_button:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_user_state_df['State']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_user_state_df['Registered_user']:
                st.write(f":blue[{round(rows/100000,2)}L]")
                
    elif district_button:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_user_district_df['District']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_user_district_df['Registered_user']:
                st.write(f":blue[{round(rows/100000,2)}L]")
                
    elif pincode_button:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_user_pin_df['Pincode']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_user_pin_df['Registered_user']:
                st.write(f":blue[{round(rows/100000,2)}L]")
                
    else:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_user_state_df['State']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_user_state_df['Registered_user']:
                st.write(f":blue[{round(rows/100000,2)}L]") 


def user_display(year_dropdown,quarters,col3):
    map_user_df = get_map_user_data()
    top_user_df = get_top_user_data()
    top_user_pin_df = get_agg_user_pin_data()
    
    st.title(":blue[Users]")
    st.write(f"Registered PhonePe users till {quarters} {year_dropdown}")
    filtered_user_df = map_user_df[(map_user_df['Year'] == int(year_dropdown)) & (map_user_df['Quarter'] == quarters)]
    count_all = filtered_user_df['Registered_user'].sum()
    formatted_count_all = "{:,}".format(count_all)
    total_amount_apps = int(filtered_user_df['App_opening'].sum())
    formatted_total_amount_trans = "{:,}".format(total_amount_apps)
    
    st.subheader(f":blue[{formatted_count_all}]")
    st.write(f"PhonePe app opens in {quarters} {year_dropdown}")
    st.subheader(f":blue[{formatted_total_amount_trans}]")
    st.markdown("""<hr style="height:2px;border:none;color:#391c59;background-color:#391c59;" /> """, unsafe_allow_html=True)
    
    
    top_user_df = top_user_df[(top_user_df['Year'] == int(year_dropdown)) & (top_user_df['Quarter'] == quarters)]
    top_user_state_df = top_user_df.groupby('State').agg({'Registered_user': 'sum'}).reset_index()
    sorted_top_user_state_df = top_user_state_df.sort_values(by='Registered_user', ascending=False).head(10)
    
    top_user_district_df = top_user_df.groupby('District').agg({'Registered_user': 'sum'}).reset_index()
    sorted_top_user_district_df = top_user_district_df.sort_values(by='Registered_user', ascending=False).head(10)
    
    top_user_pin_df = top_user_pin_df[(top_user_pin_df['Year'] == int(year_dropdown)) & (top_user_pin_df['Quarter'] == quarters)]
    top_user_pin_df = top_user_pin_df.groupby('Pincode').agg({'Registered_user': 'sum'}).reset_index()
    sorted_top_user_pin_df = top_user_pin_df.sort_values(by='Registered_user', ascending=False).head(10)
    
    
    col3_but_col1,col3_but_col2,col3_but_col3 = st.columns(3)
    state_button = col3_but_col1.button("State")
    district_button = col3_but_col2.button("District")
    pincode_button = col3_but_col3.button("Pincode")
    
    if state_button:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_user_state_df['State']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_user_state_df['Registered_user']:
                st.write(f":blue[{round(rows/100000,2)}L]")
                
    elif district_button:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_user_district_df['District']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_user_district_df['Registered_user']:
                st.write(f":blue[{round(rows/100000,2)}L]")
                
    elif pincode_button:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_user_pin_df['Pincode']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_user_pin_df['Registered_user']:
                st.write(f":blue[{round(rows/100000,2)}L]")
                
    else:
        col3_col121, col3_col222 = col3.columns(2)
        with col3_col121:
            for rows in sorted_top_user_state_df['State']:
                st.write(rows)
        with col3_col222:
            for rows in sorted_top_user_state_df['Registered_user']:
                st.write(f":blue[{round(rows/100000,2)}L]")          
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                