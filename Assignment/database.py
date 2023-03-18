# from app import *
# Create a simple database using sqlite3

import sqlite3

connection = sqlite3.connect('countries.db')


CREATE_DIM_COUNTRY_TABLE = '''
            CREATE TABLE IF NOT EXISTS dim_country (
            country_id, country_code, country_name
            );
        '''
CREATE_DIM_GEOG_TABLE = '''
            CREATE TABLE IF NOT EXISTS dim_geog (
            lvl_id, lvl_code, lvl_name
            );
        '''
CREATE_DIM_LOOKUP_GEOG = '''
            CREATE TABLE IF NOT EXISTS dim_lookup_geog (
            country_id, country_code, lvl1, lvl2, lvl3
            );
        '''
CREATE_DIM_STORES = '''
            CREATE TABLE IF NOT EXISTS dim_stores (
            store_id, store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_geog, lvl3_geog
            );
        '''

CREATE_SAMPLE_CSV = '''
            CREATE TABLE IF NOT EXISTS sample_csv (
            store_name, country_name, street_name, pin_code, lvl1_geog, lvl2_goeg, lvl3_geog
            );
        '''
# Create Table 
def create_table():
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_DIM_COUNTRY_TABLE)
        cursor.execute(CREATE_DIM_GEOG_TABLE)
        cursor.execute(CREATE_DIM_LOOKUP_GEOG)
        cursor.execute(CREATE_DIM_STORES)
        cursor.execute(CREATE_SAMPLE_CSV)

# 
SELECT_COUNTRY_CODE = "SELECT country_code FROM dim_country WHERE country_name = ?;"

def lookup_country(country_code):
    with connection:
        cursor = connection.cursor
        cursor.execute(SELECT_COUNTRY_CODE, (country_code, ))
        cursor.fetchone()[0]

# with connection:
#     cursor = connection.cursor()
#     answer = cursor.execute(f"SELECT country_code FROM dim_country WHERE country_name = {};")
#     print(answer.fetchone())