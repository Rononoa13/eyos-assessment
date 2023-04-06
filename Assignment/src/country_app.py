import csv
import os
'''
Get country code when country name is provided.
'''
# Set the path to the CSV file
csv_file_path = os.path.join('data', 'dim_country.csv')

def get_store_code():

    # Return a capitalized version of the string.
    user_country = input('Enter a country name: ').capitalize()

    # Open a CSV file
    with open(csv_file_path) as file:

        # Create a reader object to read from input file
        reader = csv.DictReader(file)
        for row in reader:
            if user_country == row['country_name']:
                return row['country_code']

        return f"Country Not Found"


print(get_store_code())
