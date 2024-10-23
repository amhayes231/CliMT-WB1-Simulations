Unsure if I have done this correctly, please see the code snipet below to verify if so.
NOTE: climt saves the lat and lon coordinates in the dataarray of each variable as an index (ie [0,1,...,62] etc.) which
then references two seperate dataarrays for the actual lat and lon coords respectively. The indexing chosen here aligns with
a cross section from approximately (-15deg, 280deg)  to (-15deg, 320deg)

-------------------------------------------------------------------------------------

import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

#Data to be plotted:
  #t0 = initial conditions for model provided by ERA5
  #t1 = state of model after one 10min timestep

# Extract the desired latitude and longitude
lat_index = 37  # Index for latitude == -15deg
lon_range = slice(100, 115)  # Slicing from longitude 100 to 114 == (280deg, 320deg)

#Slicing datasets
t0_plot = t0.isel(lat=lat_index, lon=lon_range)
t1_plot = t1.isel(lat=lat_index, lon=lon_range)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(20, 6))  # 1 row, 2 columns

# First plot
pcm1 = axs[0].pcolormesh(t0_plot.lon, t0_plot.mid_levels, t0_plot, shading='auto', cmap='coolwarm')
fig.colorbar(pcm1, ax=axs[0], label='Temperature (K)')
axs[0].set_xlabel('Longitude')
axs[0].set_ylabel('Mid Levels')
axs[0].set_title('Temperature Profile Across Andes (ERA5)')

# Second plot
pcm2 = axs[1].pcolormesh(t1_plot.lon, t1_plot.mid_levels, t1_plot, shading='auto', cmap='coolwarm')
fig.colorbar(pcm2, ax=axs[1], label='Temperature (K)')
axs[1].set_xlabel('Longitude')
axs[1].set_ylabel('Mid Levels')
axs[1].set_title('Temperature Profile Across Andes (Climt at $t_1$)')

# Adjust layout
plt.tight_layout()
plt.show()

  

