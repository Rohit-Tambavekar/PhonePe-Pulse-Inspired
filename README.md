# PhonePe Pulse Project

## Contents
- [Description](#Description)
- [Installation](#Installation)
- [Usage](#Usage)
- [File Descriptions](#File-Descriptions)
- [Data Sources](#Data-Sources)
- [Flow of the Code](#Flow of the Code)
- [Dependencies](#Dependencies)


## Description

PhonePe Pulse is a project that visualizes transaction and user data to provide insights into the performance and trends of the PhonePe platform. It utilizes various data visualization techniques to present the data in an interactive and informative manner.

## Installation

To run the PhonePe Pulse project, please ensure you have the following dependencies installed:

- Python (version 3.6 or higher)
- Streamlit
- Plotly
- Pandas
- PIL
- MySQLConnector
- SQLAlchemy

You can install the necessary dependencies using pip:

```
pip install streamlit plotly pandas Pillow
```

## Usage

To run the PhonePe Pulse project, execute the following command in the project's root directory:

```
streamlit run phonepeStreamlitt.py
```

This will launch the project's user interface on your local machine, allowing you to interact with the visualizations and explore the data.

## File-Descriptions

The project consists of the following files:

- `gitCloneOrPull.py` module has the codes to get the data from the Phonepe pulse repository and convert the data to dataframes
- `phonepeStreamlitt.py`: The main script that runs the PhonePe Pulse project. It sets up the Streamlit application, defines the user interface, and handles the logic for displaying the visualizations.
- `streamlitfun.py`: A module providing custom functionality for converting dataframes to display format
- `streamlitfun.py`: A module containing various utility functions used in the Streamlit application.
- `getfromSQL.py`: A module containing custom SQL queries to fetch data from MySQL.
- `pushtoSQL.py`: A module containing custom SQL queries to create tables and insert data to MySQL.
- `data/`: A directory containing the data files used in the project.
- `preprocessed/`: A directory containing all processed dataframes exported as .CSV files

## Data-Sources

The data used in the PhonePe Pulse project is sourced from PhonePe's transaction and user records. The data is stored in CSV format and preprocessed before visualisations are used.

## Flow of the Code

1. The `phonepeStreamlitt.py` script sets up the Streamlit application and defines the layout and user interface.
2. The user can navigate between different sections, including the home page, dashboard, and contact page.
3. On the home page, the user can select the type of data to visualize (transactions or users) and choose the year and quarter.
4. Based on the user's selections, the appropriate visualization is displayed using functions from the `streamlitfun.py` module.
5. The `streamlitfun.py` module contains functions for creating transaction and user visualizations, including pydeck maps and other interactive charts.
6. The `getfromSQL.py` module contains custom SQL queries to fetch data from MySQL.
7. The `pushtoSQL.py` module contains custom SQL queries to create tables and insert data into MySQL.
8. The `gitCloneOrPull.py` module has the codes to get the data from the Phonepe pulse repository and convert the data to dataframes
9. The data for the visualizations are sourced from the CSV files in the `data/` directory, which are preprocessed and loaded into Pandas DataFrames.
10. The visualizations are created using Plotly and displayed within the Streamlit application.

## Dependencies

The PhonePe Pulse project relies on the following Python packages:

- Streamlit: A framework for building interactive web applications with Python.
- Plotly: A data visualization library for creating interactive charts and graphs.
- Pandas: A powerful data manipulation and analysis library.
- PIL: The Python Imaging Library, used for image processing and manipulation.
- MySQL Connector and SQLAlchemy: Python libraries to get and push data from and into MySQL

Ensure that you have these dependencies installed to run the project successfully.

Please note that the project may have additional dependencies or specific setup requirements depending on your environment.

For any questions or inquiries, please contact Rohit Tambavekar via LinkedIn at [Rohit Tambavekar](https://www.linkedin.com/in/rohit-tambavekar/).
