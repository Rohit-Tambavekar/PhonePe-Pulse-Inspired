import pandas as pd
from sqlalchemy import create_engine
# SELECT * FROM phonepe_pulse.map_trans WHERE State = 'Telangana' and District = 'Warangal';


def get_map_trans_data():
    
    
    # establish a connection to the database using SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:Rayz@localhost/phonepe_pulse')

    # define the SQL query
    query = """
        SELECT State, Year, Quarter, District, Transaction_count,
            Transaction_amount, Latitude, Longitude, Region
        FROM phonepe_pulse.map_trans
    """

    # execute the query and store the results in a pandas DataFrame
    df = pd.read_sql_query(query, engine)

    # set the primary key on the DataFrame
    # df.set_index(['State', 'Year', 'Quarter', 'District', 'Region'], inplace=True)
    # close the database connection
    engine.dispose()

    return df


def get_agg_trans_data():
    
    
    # establish a connection to the database using SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:Rayz@localhost/phonepe_pulse')

    # define the SQL query
    query = """
        SELECT State, Year, Quarter, Transaction_type, Transaction_count,
            Transaction_amount, Region
        FROM phonepe_pulse.agg_trans
    """

    # execute the query and store the results in a pandas DataFrame
    df = pd.read_sql_query(query, engine)

    # set the primary key on the DataFrame
    # df.set_index(['State', 'Year', 'Quarter', 'District', 'Region'], inplace=True)
    # close the database connection
    engine.dispose()

    return df


def get_top_trans_data():
    
    
    # establish a connection to the database using SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:Rayz@localhost/phonepe_pulse')

    # define the SQL query
    query = """
        SELECT State, Year, Quarter,District, Total_transaction_count, 
        Total_transaction_amount, Region
        FROM phonepe_pulse.top_trans_dist
    """

    # execute the query and store the results in a pandas DataFrame
    df = pd.read_sql_query(query, engine)

    # set the primary key on the DataFrame
    # df.set_index(['State', 'Year', 'Quarter', 'District', 'Region'], inplace=True)
    # close the database connection
    engine.dispose()

    return df


def get_agg_trans_pin_data():
    
    
    # establish a connection to the database using SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:Rayz@localhost/phonepe_pulse')

    # define the SQL query
    query = """
        SELECT State, Year, Quarter,Pincode, 
        Total_transaction_count, Total_transaction_amount, Region
        FROM phonepe_pulse.top_trans_pin
    """

    # execute the query and store the results in a pandas DataFrame
    df = pd.read_sql_query(query, engine)

    # set the primary key on the DataFrame
    # df.set_index(['State', 'Year', 'Quarter', 'District', 'Region'], inplace=True)
    # close the database connection
    engine.dispose()

    return df


def get_map_user_data():
    
    
    # establish a connection to the database using SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:Rayz@localhost/phonepe_pulse')

    # define the SQL query
    query = """
        SELECT State, Year, Quarter, District, Registered_user,
            App_opening, Latitude, Longitude, Region
        FROM phonepe_pulse.map_user
    """

    # execute the query and store the results in a pandas DataFrame
    df = pd.read_sql_query(query, engine)

    # set the primary key on the DataFrame
    # df.set_index(['State', 'Year', 'Quarter', 'District', 'Region'], inplace=True)
    # close the database connection
    engine.dispose()

    return df


def get_top_user_data():
    
    
    # establish a connection to the database using SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:Rayz@localhost/phonepe_pulse')

    # define the SQL query
    query = """
        SELECT State, Year, Quarter,District,
        Registered_user, Region
        FROM phonepe_pulse.top_user_dist
    """

    # execute the query and store the results in a pandas DataFrame
    df = pd.read_sql_query(query, engine)

    # set the primary key on the DataFrame
    # df.set_index(['State', 'Year', 'Quarter', 'District', 'Region'], inplace=True)
    # close the database connection
    engine.dispose()

    return df


def get_agg_user_pin_data():
    
    
    # establish a connection to the database using SQLAlchemy
    engine = create_engine('mysql+mysqlconnector://root:Rayz@localhost/phonepe_pulse')

    # define the SQL query
    query = """
        SELECT State, Year, Quarter,Pincode, 
        Registered_user, Region
        FROM phonepe_pulse.top_user_pin
    """

    # execute the query and store the results in a pandas DataFrame
    df = pd.read_sql_query(query, engine)

    # set the primary key on the DataFrame
    # df.set_index(['State', 'Year', 'Quarter', 'District', 'Region'], inplace=True)
    # close the database connection
    engine.dispose()

    return df


