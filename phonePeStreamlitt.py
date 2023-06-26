import streamlit as st
from streamlit_option_menu import option_menu
from streamlitfun import *
from streamlit_elements import dashboard, elements, mui
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
import io
from streamlit_elements import nivo

st.set_page_config(
    page_title="PhonePe Pulse",
    layout="wide",
    page_icon=":dna:",
    menu_items={
        'About': "Created By Rohit Tambavekar 'https://www.linkedin.com/in/rohit-tambavekar/'"
    }
)



hide_st_style = """
<style>
header { visibility: hidden; }
footer { visibility: hidden; }

</style>
"""

contn_color_image = """
                            <style>
                            [class="css-119uhnj esravye1"]
                            {
                                background-color : #2c1942;
                                opacity : 1;
                                font-family: 'Arial', sans-serif;
                                border-radius: 20px;
                                font-size: 25px;
                                color: #ffffff;
                                padding: 20px 20px;
                                border: none;
                                line-height: 0.5;
                            }
                            </style>
                        """

st.markdown(hide_st_style, unsafe_allow_html=True)


st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #391c59;">
  <a class="navbar-brand" href="#" style="color: #e9d6ff;">PhonePe Pulse</a>
  <a class="navbar-brand" href="#" style="color: #8657d3;">| THE BEAT OF PROGRESS</a>
</nav>
""", unsafe_allow_html=True)

Type_Options = ["Transactions", "Users"]
Type_Options_Year = ["2018","2019","2020","2021","2022"]

def main():
    # st.write("<h1 style='text-align: center;margin-top: 0px;'>PhonePe Pulse</h1>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options = ["Home","Contact"],
        icons=["house","envelope"],
        menu_icon = "cast",
        default_index = 0,
        orientation = "horizontal"
    )

    if selected == "Home":
        col1, col2, col3 = st.columns([4, 12, 5])
        
        with col1:
            sub_col1, sub_col2 = st.columns(2)
            with sub_col1:
                type_dropdown = st.selectbox("Select an option:",Type_Options, label_visibility = "collapsed")
            with sub_col2:
                year_dropdown = st.selectbox("Select an option:",Type_Options_Year, label_visibility = "collapsed") 
            # sub_col11, sub_col12, sub_col13,sub_col14 = st.columns([3, 6, 4])
            quarters = st.radio(
                                "Select channel using: ",
                                ('Q1','Q2','Q3','Q4'),index = 0,horizontal = True,label_visibility = "collapsed")

        with col2:
                       
            if type_dropdown == 'Transactions':
                if year_dropdown == '2018':
                    if quarters == 'Q1':
                        elevation = 0.0001
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                                            
                    if quarters == 'Q2':
                        elevation = 0.0001
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                    if quarters == 'Q3':
                        elevation = 0.0001
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                    if quarters == 'Q4':
                        elevation = 0.0001
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                
                elif year_dropdown == '2019':
                    if quarters == 'Q1':
                        elevation = 0.00008
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                                            
                    if quarters == 'Q2':
                        elevation = 0.00008
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                    if quarters == 'Q3':
                        elevation = 0.00008
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                    if quarters == 'Q4':
                        elevation = 0.00008
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                        
                if year_dropdown == '2020':
                    if quarters == 'Q1':
                        
                        elevation = 0.00005
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                        
                    if quarters == 'Q2':
                        elevation = 0.00005
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                    if quarters == 'Q3':
                        elevation = 0.00005
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                    if quarters == 'Q4':
                        elevation = 0.00005
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                
                elif year_dropdown == '2021':
                    if quarters == 'Q1':
                        elevation = 0.00003
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                                            
                    if quarters == 'Q2':
                        elevation = 0.00003
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                    if quarters == 'Q3':
                        elevation = 0.00003
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                    if quarters == 'Q4':
                        elevation = 0.00003
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                 
                elif year_dropdown == '2022':
                    if quarters == 'Q1':
                        elevation = 0.00002
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                                            
                    if quarters == 'Q2':
                        elevation = 0.00002
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                    if quarters == 'Q3':
                        elevation = 0.00002
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                    if quarters == 'Q4':
                        elevation = 0.00002
                        ele_range=[0,0.000001]
                        trans_col_map(year_dropdown,quarters,elevation,*ele_range)
            
            elif type_dropdown == 'Users':
                if year_dropdown == '2018':
                    if quarters == 'Q1':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
                     
                    if quarters == 'Q2':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
    
                    if quarters == 'Q3':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
    
                    if quarters == 'Q4':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                if year_dropdown == '2019':
                    if quarters == 'Q1':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)

                    if quarters == 'Q2':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
    
                    if quarters == 'Q3':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
    
                    if quarters == 'Q4':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                if year_dropdown == '2020':
                    if quarters == 'Q1':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)

                    if quarters == 'Q2':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
    
                    if quarters == 'Q3':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
    
                    if quarters == 'Q4':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                if year_dropdown == '2021':
                    if quarters == 'Q1':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)

                    if quarters == 'Q2':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
    
                    if quarters == 'Q3':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
    
                    if quarters == 'Q4':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
                    
                if year_dropdown == '2022':
                    if quarters == 'Q1':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)

                    if quarters == 'Q2':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
    
                    if quarters == 'Q3':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
    
                    if quarters == 'Q4':
                        elevation = 0.5
                        ele_range=[0,0.1]
                        user_col_map(year_dropdown,quarters,elevation,*ele_range)
                 
        with col3:
            
            if type_dropdown == 'Transactions':
                if year_dropdown == '2018':
                    if quarters == 'Q1':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                                    
                    elif quarters == 'Q2':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                    
                    elif quarters == 'Q3':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                    
                    elif quarters == 'Q4':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                            
                if year_dropdown == '2019':
                    if quarters == 'Q1':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                                    
                    elif quarters == 'Q2':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                    
                    elif quarters == 'Q3':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                    
                    elif quarters == 'Q4':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                            
                if year_dropdown == '2020':
                    if quarters == 'Q1':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                                    
                    elif quarters == 'Q2':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                    
                    elif quarters == 'Q3':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                    
                    elif quarters == 'Q4':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                            
                if year_dropdown == '2021':
                    if quarters == 'Q1':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                                    
                    elif quarters == 'Q2':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                    
                    elif quarters == 'Q3':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                    
                    elif quarters == 'Q4':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)

                if year_dropdown == '2022':
                    if quarters == 'Q1':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                                    
                    elif quarters == 'Q2':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                    
                    elif quarters == 'Q3':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
                    
                    elif quarters == 'Q4':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        trans_display(year_dropdown,quarters,col3)
            
            elif type_dropdown == 'Users':
                if year_dropdown == '2018':
                    if quarters == 'Q1':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display_unavail(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q2':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display_unavail(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q3':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display_unavail(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q4':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display_unavail(year_dropdown,quarters,col3)
                
                if year_dropdown == '2019':
                    if quarters == 'Q1':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display_unavail(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q2':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q3':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q4':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                          
                if year_dropdown == '2020':
                    if quarters == 'Q1':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q2':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q3':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q4':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                
                if year_dropdown == '2021':
                    if quarters == 'Q1':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q2':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q3':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q4':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                          
                if year_dropdown == '2022':
                    if quarters == 'Q1':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q2':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q3':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                    
                    if quarters == 'Q4':
                        st.markdown(
                                contn_color_image,
                                unsafe_allow_html=True
                                )
                        user_display(year_dropdown,quarters,col3)
                          
                       
    # if selected == "Dashboard":
    #     with elements("dashboard"):

    #         # You can create a draggable and resizable dashboard using
    #         # any element available in Streamlit Elements.

            
    #         # First, build a default layout for every element you want to include in your dashboard
    #         map_trans_df = get_map_trans_data()
    #         filtered_df = map_trans_df[(map_trans_df['Year'] == 2018) & (map_trans_df['Quarter'] == 'Q1')]

    #         # Create a bar chart for transaction count by state
    #         count_by_state = filtered_df.groupby('State')['Transaction_count'].sum().reset_index()
    #         count_by_state_chart_data = [{"id": row['State'], "value": row['Transaction_count']} for index, row in count_by_state.iterrows()]

            
    #         x = nivo.Bar(
    #             data=count_by_state_chart_data,
    #             x="id",
    #             y="value",
    #             indexBy="id",
    #             keys=["value"],
    #             margin={"top": 50, "right": 50, "bottom": 50, "left": 50},
    #             padding=0.2,
    #             labelTextColor="inherit:darker(1.6)",
    #             borderColor="inherit:darker(1.6)",
    #             theme={"background": "#ffffff"}
    #         )

    #         # Create a scatter plot for transaction amount by district
    #         amount_by_district = filtered_df[['Transaction_amount', 'District']]
    #         amount_by_district_chart_data = [{"x": row['Transaction_amount'], "y": row['District']} for index, row in amount_by_district.iterrows()]

            
    #         y = nivo.Bar(
    #             data=count_by_state_chart_data,
    #             x="id",
    #             y="value",
    #             indexBy="id",
    #             keys=["value"],
    #             margin={"top": 50, "right": 50, "bottom": 50, "left": 50},
    #             padding=0.2,
    #             labelTextColor="inherit:darker(1.6)",
    #             borderColor="inherit:darker(1.6)",
    #             theme={"background": "#ffffff"}
    #         )
                    
    #         layout = [
    #             dashboard.Item("first_item", 4, 8, 6, 2),
    #             dashboard.Item("second_item", 4, 4, 1, 1),
    #             dashboard.Item("third_item", 0, 0, 2, 2),
    #         ]

    #         # If you want to retrieve updated layout values as the user move or resize dashboard items,
    #         # you can pass a callback to the onLayoutChange event parameter.

    #         def handle_layout_change(updated_layout):
    #             # You can save the layout in a file, or do anything you want with it.
    #             # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
    #             print(updated_layout)

    #         with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
    #             mui.Paper("x", key="first_item")
    #             mui.Paper("y", key="second_item")
    #             mui.Paper("z", key="third_item")
        
    if selected == "Contact":
        st.title(f"You have selected {selected}")


    
    

if __name__ == "__main__":
    main()