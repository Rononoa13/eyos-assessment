# Create a simple database using sqlite3
import sqlite3

connection = sqlite3.connect('assessment.db')
# 
# Create dim_country table in a database
# 
CREATE_DIM_COUNTRY_TABLE = '''
            CREATE TABLE IF NOT EXISTS "dim_country" (
                "country_id" INTEGER,
                "country_code" TEXT,
                "country_name" TEXT
);
'''
# -------------------------- Create dim_stores table -------------------------------
CREATE_DIM_STORES_TABLE = '''
CREATE TABLE dim_stores (
    store_id INTEGER PRIMARY KEY,
    store_code TEXT,
    store_name TEXT,
    country_code TEXT,
    street_name TEXT,
    pin_code REAL,
    lvl1_geog TEXT,
    lvl2_geog TEXT,
    lvl3_geog TEXT
)
'''

SELECT_COUNTRY_CODE = '''
SELECT country_code FROM dim_country WHERE lower(country_name) = lower(?);
'''
SELECT_STORE_ID = '''
SELECT store_id FROM dim_stores;
'''

# 
# 
# 
INSERT_INTO_DIM_COUNTRY = '''
INSERT INTO dim_country (country_id, country_code, country_name)
    VALUES (?, ?, ?)
'''
# Insert data into dim store before loading data from sample csv.
INSERT_PRE_DATA_TO_DIM_STORES_TABLE = '''
INSERT INTO dim_stores (store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_geog)
    VALUES 
    ('IND1', '7-11-store1', 'IND', 'thomas street', 600098, 'Tamil Nadu', 'Chennai'),
    ('ID2', 'Test Store Jakarta', 'ID', 'Jl Durian 19 Sumatera Utara', 20235, 'Medan', 'Sumatera Utara') 
'''
INSERT_CSV_DATA_TO_DIM_STORE_TABLE = '''
INSERT INTO dim_stores (store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_geog, lvl3_geog)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
'''
# 
# Create table
# 
def create_dim_country_table():
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_DIM_COUNTRY_TABLE)

def create_dim_stores_table():
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_DIM_STORES_TABLE)

# 
# Get `country_code` from dim_country table
# 
def get_country_code_from_dim_country(country_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_COUNTRY_CODE, (country_name, ))
        return cursor.fetchone()[0]
# print(get_country_code_from_dim_country('thaiLAND'))

# 
#  Get `store_code` from sample_csv
# 
def get_store_id_from_dim_stores_table():
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_STORE_ID)
        for row in cursor.fetchall():
            yield row[0]

# for row in get_store_id_from_dim_stores_table():
#     print(row)

def get_length_store_id_from_dim_stores_table():
    with connection:
        cursor = connection.cursor()
        store_id_length = cursor.execute("SELECT COUNT(*) FROM dim_stores")
        return store_id_length.fetchone()[0]
# print(get_length_store_id_from_dim_stores_table())


# 
# Insert data into dim country
# 
def add_entry_to_dim_country_table(country_id, country_code, country_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_INTO_DIM_COUNTRY, (country_id, country_code, country_name))
# 
# Insert data into dim stores
#
def add_pre_data_to_dim_stores_table():
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_PRE_DATA_TO_DIM_STORES_TABLE)
        

def add_csv_data_to_dim_stores_table(store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_geog, lvl3_geog,):
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_CSV_DATA_TO_DIM_STORE_TABLE, (store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_geog, lvl3_geog,))
        new_id = cursor.lastrowid
        return new_id

# def get_last_inserted_row_id():
#     with connection:
#         cursor = connection.cursor()
#         new_id = cursor.lastrowid
#         return new_id
# print(get_last_inserted_row_id())

# create_dim_country_table()
# create_dim_stores_table()

# if __name__ == "__main__":
# # Function call to create database table
#     create_dim_country_table()
#     create_dim_stores_table()
