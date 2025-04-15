import numpy as np
import xarray as xr
import xarray as xr
import xesmf as xe
import os
import hashlib
from dask.distributed import Client
from dask.diagnostics import ProgressBar
import json

log("Starting data loading...")

# Paths to your NetCDF files
paths = "/run/media/adamh/Elements/training_data/era5_model_levels_*.nc"

# Open and combine all files
log("Opening and combining NetCDF files...")
ds = xr.open_mfdataset(paths, combine='by_coords')

# Extract temperature
log("Extracting temperature variable...")
temp = ds['t']  # adjust if needed

# Select model levels 58 to 137
log("Selecting model levels 58 to 137...")
temp = temp.isel(model_level=slice(-80, None))  #58 to 137

#================================================================

log("Loading ClimT grid...")
climt_load = np.load('/run/media/adamh/Elements/climt_lat_lon.npz')
climt_lat, climt_lon = climt_load['latitude'], climt_load['longitude']

# Create a new grid for the regridding
climt_grid = xr.Dataset(
    {
        'lat': (['lat'], climt_lat),
        'lon': (['lon'], climt_lon),
    }
)

def xr_regrid_all(ds, climt_grid, method='bilinear', weight_dir='/run/media/adamh/Elements/regrid_weights/'):
    """
    Regrid the entire dataset at once, without looping over individual time steps.
    """
    # Create a unique hash for the grid config to name the weight file
    grid_id = hashlib.md5((str(ds['latitude'].values.tobytes()) +
                           str(ds['longitude'].values.tobytes()) +
                           str(climt_grid['lat'].values.tobytes()) +
                           str(climt_grid['lon'].values.tobytes()) +
                           method).encode()).hexdigest()
    
    os.makedirs(weight_dir, exist_ok=True)
    weight_path = os.path.join(weight_dir, f'{method}_{grid_id}.nc')

    log(f"Creating regridder with weights file: {weight_path}")
    regridder = xe.Regridder(ds, climt_grid, method=method, periodic=True,
                             filename=weight_path,
                             reuse_weights=os.path.exists(weight_path))

    log("Regridding entire dataset...")
    regridded_ds = regridder(ds)

    # Convert pressure levels (if present)
    if 'pressure_level' in regridded_ds.coords:
        regridded_ds = regridded_ds.assign_coords(
            pressure_level=np.flip(regridded_ds.pressure_level.values) * 100
        )

    log("Regridding complete.")
    return regridded_ds


log("Regridding temperature data...")
temp_regridded = xr_regrid_all(temp, climt_grid)
log("Process complete.")

#=====================================================================================================

# Step 1: Start Dask Client (dashboard opens at localhost:8787)
client = Client()
display(client)  # For showing dashboard link in Jupyter

# Step 2: Load your dataset (replace this with your actual loading code)
# If you've already got it loaded in `temp_regridded`, skip this step
# temp_regridded = xr.open_zarr('your_dataset_path.zarr', chunks='auto')

# Step 3: Compute global mean and std with a progress bar
print("🔍 Computing global mean and std...")

with ProgressBar():
    global_mean = temp_regridded.mean().compute()
    global_std = temp_regridded.std().compute()

print(f"\n Global mean: {global_mean.values:.4f}")
print(f" Global std: {global_std.values:.4f}")

# Optional: Save to file for future reuse
stats = {
    'global_mean': float(global_mean.values),
    'global_std': float(global_std.values)
}

with open('normalisation_stats.json', 'w') as f:
    json.dump(stats, f)

print(" Saved normalisation stats to normalisation_stats.json")
