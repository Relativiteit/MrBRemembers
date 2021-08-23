# author Alejo Cain 23 august

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Creating window
plt.figure(figsize=(14, 14))

# init basemap coordinates Iwate Japan
m = Basemap(llcrnrlat=39,
            llcrnrlon=-146,
            urcrnrlat=39,
            urcrnrlon=-141,
            resolution='h')

# Get the area of interest imagery
m.arcgisimage(service='ESRI_Imagery_World_2D',
              xpixels=2500, verbose=True, alpha=.6)

#  Draw the coasts
m.drawcoastlines(color='blu', linewidth=3)

# Draw the states
m.drawstates(color='red', linewidth=3)
