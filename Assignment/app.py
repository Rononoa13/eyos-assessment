import pandas as pd
import database

# Read from pandas
dim_stores = pd.read_excel('table_structure.xlsx', sheet_name='dim_stores').drop(0)
dim_lookup_geog = pd.read_excel('table_structure.xlsx', sheet_name='dim_lookup_geog')
dim_geog = pd.read_excel('table_structure.xlsx', sheet_name='dim_geog')
dim_country = pd.read_excel('table_structure.xlsx', sheet_name='dim_country')
sample_csv = pd.read_excel('table_structure.xlsx', sheet_name='Sample csv data').drop(0)



def country():
    print(database.lookup_country('india'))


country()