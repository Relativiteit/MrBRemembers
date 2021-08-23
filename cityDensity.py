import pandas as pd
import numpy as np

# Read in data on all cities
# cities = pd.read_csv('jp.csv')
# change index
cities = pd.read_csv('jp.csv')

print(cities["prefecture"])  # does not take column admin_name why?
saved_column = cities.column_name
names = cities.Name

'''
# Choose only cities in Iwate,. iso2
cities = cities.loc[cities.iso2 == 'Iwate':]
print(cities)
'''
