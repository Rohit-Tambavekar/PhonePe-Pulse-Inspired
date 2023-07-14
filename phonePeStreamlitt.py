import streamlit as st
from streamlit_option_menu import option_menu
from streamlitfun import *
from streamlit_elements import dashboard, elements, mui
import pandas as pd
from streamlit_elements import nivo
from streamlit_card import card
import plotly.express as px
from PIL import Image


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
Dash_Options_ques = [
    "1: How does the transaction count vary across different States?",
    "2: What are the top transaction types?",
    "3: How does the user distribution vary across different States?",
    "4: What are the top users in terms of registered user count?",
    "5: How does the registered user distribution vary across different States?"
]

def main():
    # st.write("<h1 style='text-align: center;margin-top: 0px;'>PhonePe Pulse</h1>", unsafe_allow_html=True)
    selected = option_menu(
        menu_title=None,
        options = ["Home","Dashboard","Contact"],
        icons=["house","kaban","envelope"],
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
                          
                       
    if selected == "Dashboard":
        map_user_df = get_map_user_data()
        top_user_df = get_top_user_data()
        top_user_pin_df = get_agg_user_pin_data()
        map_trans_df = get_map_trans_data()
        agg_trans_df = get_agg_trans_data()
        top_trans_df = get_top_trans_data()
        top_trans_pin_df = get_agg_trans_pin_data()
        col1, col2, col3 = st.columns([5, 10, 5])
        with col2:
            ques_dropdown = st.selectbox("Select an option:",Dash_Options_ques, label_visibility = "collapsed")
        col1_col2, col2_col2 = st.columns(2)
        if ques_dropdown == "1: How does the transaction count vary across different States?":
            with col1_col2:
                colors = ['#f44336', '#2196f3', '#4caf50', '#ffc107']
                
                # Scatter Plot
                scatter_fig = px.scatter(map_trans_df, x='Longitude', y='Latitude', size='Transaction_count', color='State', hover_data=['District'])
                st.plotly_chart(scatter_fig, use_container_width=True)
                
                # Bar Chart
                bar_fig = px.bar(map_trans_df, x='State', y='Transaction_count', color='Region', barmode='overlay')
                st.plotly_chart(bar_fig, use_container_width=True)

                
            with col2_col2:
                # Pie Chart
                pie_fig = px.pie(map_trans_df, values='Transaction_count', names='State', color='Region')
                pie_fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(pie_fig, use_container_width=True)

                # Heatmap
                heatmap_fig = px.density_heatmap(map_trans_df, x='Quarter', y='State', z='Transaction_count',
                                    color_continuous_scale="Agsunset")
                st.plotly_chart(heatmap_fig, use_container_width = True)
                
        elif ques_dropdown == "2: What are the top transaction types?":
            with col1_col2:
                # Bar Chart
                bar_fig = px.bar(agg_trans_df, x='Transaction_type', y='Transaction_count', color='Region', barmode="stack")
                st.plotly_chart(bar_fig, use_container_width=True)
                
            with col2_col2:
                # Sunburst Chart
                sunburst_fig = px.sunburst(agg_trans_df, path=['Region', 'Transaction_type'], values='Transaction_count')
                st.plotly_chart(sunburst_fig, use_container_width=True)
                
        
            # Treemap
            treemap_fig = px.treemap(agg_trans_df, path=['Region', 'Transaction_type'], values='Transaction_count')
            st.plotly_chart(treemap_fig, use_container_width=True)

        elif ques_dropdown == "3: How does the user distribution vary across different States?":
            with col1_col2:
                # Bar Chart
                bar_fig = px.bar(map_user_df, x='State', y='Registered_user', color='Region', barmode='overlay')
                st.plotly_chart(bar_fig, use_container_width=True)

                # Scatter Plot
                scatter_fig = px.scatter(map_user_df, x='State', y='Registered_user', color='Region')
                st.plotly_chart(scatter_fig, use_container_width=True)
                
            with col2_col2:
                
                # Pie Chart
                pie_fig = px.pie(map_user_df, values='Registered_user', names='Region', color='Region')
                pie_fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(pie_fig, use_container_width=True)

                # Heatmap
                heatmap_fig = px.density_heatmap(map_user_df, y='Region', x='Registered_user', color_continuous_scale='Viridis',range_x=[0, 2e6])
                st.plotly_chart(heatmap_fig, use_container_width=True)
                            
        elif ques_dropdown == "4: What are the top users in terms of registered user count?":
            with col1_col2:   
                # Bar Chart
                bar_fig = px.bar(top_user_df, x='Registered_user', y='State', color='Region', orientation='h',barmode='overlay')
                st.plotly_chart(bar_fig, use_container_width=True)

                # Scatter Plot
                scatter_fig = px.scatter(top_user_df, x='Registered_user', y='State', color='Region')
                st.plotly_chart(scatter_fig, use_container_width=True)
            with col2_col2:
                # Group the data by 'State' and calculate the sum of 'Registered_user'
                grouped_states = top_user_df.groupby('State').sum().reset_index()

                # Sort the DataFrame by the sum of 'Registered_user' column in descending order
                top_10_states = grouped_states.nlargest(10, 'Registered_user')
                # Pie Chart
                pie_fig = px.pie(top_10_states, values='Registered_user', names='State', color='Region')
                pie_fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(pie_fig, use_container_width=True)

                # Heatmap
                heatmap_fig = px.density_heatmap(top_user_df, x='Registered_user', y='State', color_continuous_scale='Viridis',range_x=[0, 2e6])
                st.plotly_chart(heatmap_fig, use_container_width=True)                

        elif ques_dropdown == "5: How does the registered user distribution vary across different States?":
            with col1_col2:
                # Bar Chart
                bar_fig = px.bar(map_user_df, x='State', y='Registered_user',color='Region')
                st.plotly_chart(bar_fig)

                # Pie Chart
                pie_fig = px.pie(map_user_df, values='Registered_user', names='State')
                pie_fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(pie_fig)
            with col2_col2:
                # Scatter Plot
                scatter_fig = px.scatter(map_user_df, x='State', y='Registered_user',color='Region')
                st.plotly_chart(scatter_fig)

                # Heatmap
                heatmap_fig = px.density_heatmap(map_user_df, x='District', y='Registered_user',range_y=[0, 2e6])
                st.plotly_chart(heatmap_fig)
        
                
    if selected == "Contact":
        aboutme ="""I am interested in pursuing a career in data science
                  and eager to learn and grow in the field of data science
                  and working towards becoming a professional in
                  this exciting and rapidly evolving field.!"""
        links={
            "GITHUB": "https://github.com/Rohit-Tambavekar",
            "LINKEDIN": "https://www.linkedin.com/in/rohit-tambavekar/"}
        col1, col2, col3= st.columns([4,5,10])
        with col2:
            col2.image(Image.open(r"D:\Rohit Doc\RohitImg.jpg"),width=150)
        with col3:
            st.subheader("Rohit Tambavekar")
            st.subheader(f'{"Mail :  "}{"rohit.tambavekar@gmail.com"}')
            st.write(aboutme)
            S=st.columns(len(links))
            for i, (x, y) in enumerate(links.items()):
                S[i].write(f"[{x}]({y})")
           

if __name__ == "__main__":
    main()