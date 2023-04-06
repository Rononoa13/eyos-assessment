import csv
import os
from models.database import get_country_code_from_dim_country, get_store_id_from_dim_stores_table, add_csv_data_to_dim_stores_table, add_pre_data_to_dim_stores_table, get_length_store_id_from_dim_stores_table
#  Set the path to the CSV file
dim_country_csv_file_path = os.path.join('data', 'dim_country.csv')
sample_csv_file_path = os.path.join('data', 'sample_csv.csv')

'''
lookup function that returns a value from a dictionary based on a key:
Get country code when country name is provided.
'''

row_count = get_length_store_id_from_dim_stores_table() #returns 2 at first cause 2 data in dim_stores
# Open a CSV file
with open(dim_country_csv_file_path) as file, open(sample_csv_file_path) as sample_file:
    dim_country_reader = csv.DictReader(file)
    sample_file_reader = csv.DictReader(sample_file)
 
    # zip() function to match corresponding rows from each file. 
    for sf_row, dc_row in zip(sample_file_reader, dim_country_reader):
        # Look up the country code from the dim_country table
        # Input country name from sample_csv
        country_code = get_country_code_from_dim_country(dc_row['country_name'])

        store_name = sf_row['store_name']
        street_name = sf_row['street_name']
        pin_code = sf_row['pin_code']
        lvl1_geog = sf_row['lvl1_geog']
        lvl2_geog = sf_row['lvl2_goeg']
        lvl3_geog = sf_row['lvl3_geog']
        
        store_code = country_code + str(row_count + 1)
        new_id = add_csv_data_to_dim_stores_table(store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_geog, lvl3_geog)
        store_code = country_code + str(new_id)
        print(store_code, store_name, country_code, street_name, pin_code, lvl1_geog, lvl2_geog, lvl3_geog)
        