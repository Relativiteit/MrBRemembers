# author Alejo Cain 23 august

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Creating window
plt.figure(figsize=(14, 14))

# init basemap coordinates Iwate Japan
# m = Basemap(llcrnrlat=51.85,
#             llcrnrlon=4.34,
#             urcrnrlat=51.97,
#             urcrnrlon=4.52,
#             resolution='h')

# Initialize the basemap california
m = Basemap(llcrnrlat=30,
            llcrnrlon=-126,
            urcrnrlat=45,
            urcrnrlon=-114,
            resolution='h')

# Get the area of interest imagery
m.arcgisimage(service='ESRI_Imagery_World_2D',
              xpixels=2500, verbose=True, alpha=.6)

#  Draw the coasts
m.drawcoastlines(color='blu', linewidth=3)

# Draw the states
m.drawstates(color='red', linewidth=3)


# Read in data on all cities
# cities = pd.read_csv('jp.csv')
# change index
cities = pd.read_csv('uscities.csv')

# print(cities["prefecture"])  # does not take column admin_name why?
'''
# Choose only cities in Iwate,. iso2
cities = cities.loc[cities.iso2 == 'Iwate':]
print(cities)
'''
# Choose only cities in california
cities = cities.loc[cities.state_id == 'CA', :]

# Get all the data from the dataframe
lat, lon = cities['lat'], cities['lng']
population, density = cities['population'], cities['density']

# Scatter the points, using size and color but no label
plt.scatter(lon, lat, label=None,
            c=np.log10(population), s=10*np.log(density),
            cmap='viridis', linewidth=0, alpha=.4)
plt.axis(aspect='equal')
plt.xlabel('longitude')
plt.ylabel('latitude')
plt.colorbar(label='log$_{10}$(population)')
plt.clim(3, 7)

# make a guide for the user
for density in [1, 50//3, 50]:
    plt.scatter([], [], c='k', alpha=0.3, s=5*np.log(density),
                label='10* log('+str(density) + ')')
plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1, title='City Density')

# add a title
plt.title('California Cities: Density and Population')
