# Create a simple database using sqlite3
import sqlite3

connection = sqlite3.connect('assessment.db')

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
# -------------------------- Create dim_geog table -------------------------------
# CREATE_DIM_GEOG = '''
# CREATE TABLE dim_geog (
#     country_id INTEGER PRIMARY KEY,
# )
# '''
# -------------------------- Create dim_geog table -------------------------------
INSERT_DATA_TO_DIM_COUNTRY_TABLE = '''
INSERT INTO dim_country (country_id, country_code, country_name)
    VALUES (?, ?, ?)
'''


SELECT_COUNTRY_CODE = '''
SELECT country_code FROM dim_country WHERE lower(country_name) = lower(?);
'''

def create_table():
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_DIM_COUNTRY_TABLE)
        cursor.execute(CREATE_DIM_STORES_TABLE)

# create_table()

# Insert data into dim store before loading data from sample csv.
INSERT_DATA_TO_DIM_STORES_TABLE = '''
INSERT INTO dim_stores (store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_geog)
    VALUES 
    ('IND1', '7-11-store1', 'IND', 'thomas street', 600098, 'Tamil Nadu', 'Chennai'),
    ('ID2', 'Test Store Jakarta', 'ID', 'Jl Durian 19 Sumatera Utara', 20235, 'Medan', 'Sumatera Utara') 
'''
INSERT_INTO_DIM_STORES = '''
INSERT INTO dim_stores (store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_geog, lvl3_geog) VALUES (?, ?, ?, ?, ?, ?, ?, ?);"
'''

with connection:
    cursor = connection.cursor()
    cursor.execute(INSERT_DATA_TO_DIM_STORES_TABLE)


def insert_into_table(country_id, country_code, country_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_DATA_TO_DIM_COUNTRY_TABLE, (country_id, country_code, country_name))


def get_country_code(country_name):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_COUNTRY_CODE, (country_name, ))
        return cursor.fetchone()
    
def insert_into_dim_stores(store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_goeg, lvl3_geog):
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_INTO_DIM_STORES, (store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_goeg, lvl3_geog))
# def get_country_code():
#     with connection:
#         cursor = connection.cursor()
#         cursor.execute(SELECT_COUNTRY_CODE, ('India', ))
#         return cursor.fetchone()
# print(get_country_code())
