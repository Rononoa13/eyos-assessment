import csv
import database_3

# Open csv file
def insert_into_dim_country_table():
    with open("dim_country.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            # print(row)
            # Insert data from csv to the table
            database_3.insert_into_table(row['country_id'], row['country_code'], row['country_name'])

def load_data_to_table():
    # Open csv file
    with open('table_structure.csv') as file:
        
        reader = csv.DictReader(file)
        i = 1
        for row in reader:
            country_code = database_3.get_country_code(row['country_name'])
            store_code = f"{country_code}{i}"
            i += 1
            database_3.insert_into_dim_stores(store_code, row['store_name'], country_code, row['street_name'], row['pin_code'], row['lvl1_geog'], row['lvl2_goeg'], row['lvl3_geog'])


load_data_to_table()