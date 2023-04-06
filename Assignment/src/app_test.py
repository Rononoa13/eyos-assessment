import csv
import os
from models.database import get_country_code_from_dim_country, get_store_id_from_dim_stores_table, add_csv_data_to_dim_stores_table
from models.database import connection
# 
# create a cursor
cursor = connection.cursor()

#  Set the path to the CSV file
dim_country_csv_file_path = os.path.join('data', 'dim_country.csv')
sample_csv_file_path = os.path.join('data', 'sample_csv.csv')

'''
lookup function that returns a value from a dictionary based on a key:
Get country code when country name is provided.
'''

def get_store_code():

    # Return a capitalized version of the string.

    # Open a CSV file
    with open(dim_country_csv_file_path) as file, open(sample_csv_file_path) as sample_file:
        # Create a reader object to read from input file
        dim_country_reader = csv.DictReader(file)
        sample_csv_reader = csv.DictReader(sample_file)


        for sf_row, dc_row in zip(sample_csv_reader, dim_country_reader):
            store_name = sf_row['store_name']
            country_name = sf_row['country_name']
            street_name = sf_row['street_name']
            pin_code = sf_row['pin_code']
            lvl1_geog = sf_row['lvl1_geog']
            lvl2_geog = sf_row['lvl2_goeg']
            lvl3_geog = sf_row['lvl3_geog']
        
        store_code = country_name + str(new_store_id)

        new_store_id = add_csv_data_to_dim_stores_table(store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_geog, lvl3_geog)