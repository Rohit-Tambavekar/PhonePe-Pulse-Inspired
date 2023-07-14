import mysql.connector
from gitCloneOrPull import *

def sql_connection():
    conn = mysql.connector.connect(
                host="localhost",
                port=3306,
                user = "root",
                password = 'Rayz'
    )
    
    cursor = conn.cursor()
    
    
    return conn, cursor

def create_db_table():
    
    conn,cur = sql_connection()
    
    cur.execute("DROP DATABASE IF EXISTS phonepe_pulse")

    cur.execute("CREATE DATABASE phonepe_pulse")

    cur.execute("USE phonepe_pulse")
    
    cur.execute('''CREATE TABLE agg_trans (
                    State VARCHAR(50),
                    Year YEAR,
                    Quarter VARCHAR(4),
                    Transaction_type VARCHAR(50),
                    Transaction_count INTEGER,
                    Transaction_amount FLOAT(50,15),
                    Region VARCHAR(50),
                    PRIMARY KEY (State(50), Year, Quarter, Transaction_type(50), Region(50))
                 )''')
    
    
    cur.execute('''CREATE TABLE agg_user (
                        State VARCHAR(50),
                        Year YEAR,
                        Quarter VARCHAR(4),
                        Brand VARCHAR(50),
                        Brand_count INTEGER,
                        Brand_percentage FLOAT,
                        Region VARCHAR(50),
                        PRIMARY KEY (State(50), Year, Quarter, Brand(50), Region(50))
                    )''')
    
    ##########################################################
    cur.execute('''CREATE TABLE map_trans (
                        State VARCHAR(50),
                        Year YEAR,
                        Quarter VARCHAR(4),
                        District VARCHAR(50),
                        Transaction_count INTEGER,
                        Transaction_amount DOUBLE PRECISION, 
                        Latitude DOUBLE PRECISION,
                        Longitude DOUBLE PRECISION,
                        Region VARCHAR(50),
                        PRIMARY KEY (State(50), Year, Quarter, District(50), Region(50))
                    )''')
    
    
    cur.execute('''CREATE TABLE map_user (
                        State VARCHAR(50),
                        Year YEAR,
                        Quarter VARCHAR(4),
                        District VARCHAR(50),
                        Registered_user INTEGER,
                        App_opening INTEGER,
                        Latitude DOUBLE PRECISION,
                        Longitude DOUBLE PRECISION,
                        Region VARCHAR(50),
                        PRIMARY KEY (State(50), Year, Quarter, District(50), Region(50))
                    )''')
    
    
    cur.execute('''CREATE TABLE top_trans_dist (
                        State VARCHAR(50),
                        Year YEAR,
                        Quarter VARCHAR(4),
                        District VARCHAR(50),
                        Total_transaction_count INTEGER,
                        Total_transaction_amount DOUBLE PRECISION,
                        Latitude DOUBLE PRECISION,
                        Longitude DOUBLE PRECISION,
                        Region VARCHAR(50),
                        PRIMARY KEY (State(50), Year, Quarter, District(50), Region(50))
                    )''')
    
    
    cur.execute('''CREATE TABLE top_trans_pin (
                        State VARCHAR(50),
                        Year YEAR,
                        Quarter VARCHAR(4),
                        Pincode VARCHAR(50),
                        Total_transaction_count INTEGER,
                        Total_transaction_amount DOUBLE PRECISION,
                        Region VARCHAR(50),
                        PRIMARY KEY (State(50), Year, Quarter, Pincode(50), Region(50))
                    )''')
    
    
    cur.execute('''CREATE TABLE top_user_dist (
                        State VARCHAR(50),
                        Year YEAR,
                        Quarter VARCHAR(4),
                        District VARCHAR(50),
                        Registered_user INTEGER,
                        Latitude DOUBLE PRECISION,
                        Longitude DOUBLE PRECISION,
                        Region VARCHAR(50),
                        PRIMARY KEY (State(50), Year, Quarter, District(50), Region(50))
                    )''')
    
    
    cur.execute('''CREATE TABLE top_user_pin (
                        State VARCHAR(50),
                        Year YEAR,
                        Quarter VARCHAR(4),
                        Pincode VARCHAR(50),
                        Registered_user INTEGER,
                        Region VARCHAR(50),
                        PRIMARY KEY (State(50), Year, Quarter, Pincode(50), Region(50))
                    )''')
    
    
    
    
    cur.execute('''CREATE TABLE state_lat_long (
                        State VARCHAR(50),
                        Latitude FLOAT,
                        Longitude FLOAT,
                        Region VARCHAR(50),
                        PRIMARY KEY (State(50), Latitude, Longitude, Region(50))
                    )''')
    
    
    conn.commit()
    
    cur.close()
    conn.close()

def push_data_to_sql():
    
    conn,cur = sql_connection()
    
    cur.execute("USE phonepe_pulse")
    
    all_df_names = {
                    'agg_trans': agg_trans_state_df,
                    'agg_user': agg_user_state_df,
                    'map_trans': agg_map_state_trans_df,
                    'map_user': agg_map_state_user_df,
                    'top_trans_dist': top_state_trans_df,
                    'top_trans_pin': top_state_trans_pin_df,
                    'top_user_dist': top_state_user_df,
                    'top_user_pin': top_state_user_pin_df,
                    'state_lat_long':all_state_df
                }
    
    table_columns = {
                    'agg_trans': list(agg_trans_state_df.columns),
                    'agg_user': list(agg_user_state_df.columns),
                    'map_trans': list(agg_map_state_trans_df.columns),
                    'map_user': list(agg_map_state_user_df.columns),
                    'top_trans_dist': list(top_state_trans_df.columns),
                    'top_trans_pin': list(top_state_trans_pin_df.columns),
                    'top_user_dist': list(top_state_user_df.columns),
                    'top_user_pin': list(top_state_user_pin_df.columns),
                    'state_lat_long':list(all_state_df.columns)
                }
    
    for table_name in all_df_names.keys():
        df = all_df_names[table_name]
        columns = table_columns[table_name]
        placeholders = ', '.join(['%s'] * len(columns))
        query = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({placeholders})"
        for _, row in df.iterrows():
            data = tuple(row[column] for column in columns)
            try:
                cur.execute(query, data)
            except Exception as e:
                print(f"Error executing query: {table_name}{e}")
        conn.commit()
    print("Data successfully pushed into MySQL tables")

create_db_table()
push_data_to_sql()
