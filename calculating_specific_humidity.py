#Calculating specific humidity - needs testing

import xarray as xr
import numpy as np

# Load ERA5 data using xarray (assuming you have downloaded it)
# Replace 'your_file.nc' with your actual data file
data = xr.open_dataset('your_file.nc')

# Extract required variables
t2m = data['t2m'] - 273.15  # Convert K to °C
d2m = data['d2m'] - 273.15  # Convert K to °C
sp = data['sp'] / 100  # Convert Pa to hPa

# Calculate saturation vapor pressure (es) and actual vapor pressure (e)
es = 6.11 * 10**((7.5 * t2m) / (t2m + 237.3))  # Saturation vapor pressure in hPa
e = 6.11 * 10**((7.5 * d2m) / (d2m + 237.3))  # Actual vapor pressure in hPa

# Calculate mixing ratio (r)
r = (0.622 * e) / (sp - e)  # Note: sp is now in hPa

# Calculate specific humidity (q)
q = r / (1 + r)

# Convert to g/kg
specific_humidity_g_kg = q * 1000  # Convert kg/kg to g/kg

# If you want to convert to a DataFrame or process further
specific_humidity_g_kg = specific_humidity_g_kg.compute()  # Use .compute() for lazy evaluation

# Print or visualize the results
print(specific_humidity_g_kg)

