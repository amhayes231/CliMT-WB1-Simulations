import os
import glob
import numpy as np
import xarray as xr
import xesmf as xe
from datetime import datetime
from dask.diagnostics import ProgressBar
from dask import delayed, compute
import warnings
from datetime import datetime

# Suppress specific warning message from xesmf
warnings.filterwarnings(
    "ignore", 
    message="Latitude is outside of \\[-90, 90\\]", 
    module="xesmf.backend"
)

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

# Directories
base_dir = "/mnt/Elements/training_data/"
output_dir = "/mnt/Elements/regridded_data/"
climt_load = np.load('/run/media/adamh/X6/test_levels/climt_lat_lon.npz')

all_era5_level_files = sorted(glob.glob(os.path.join(base_dir, "era5_model_levels_20*.nc")))
all_era5_level_z_files = sorted(glob.glob(os.path.join(base_dir, "era5_model_levels_z_*.nc")))
all_era5_surface_files = sorted(glob.glob(os.path.join(base_dir, "era5_surface_levels_*.nc")))
log(f"Found {len(all_era5_level_files)} files to process.")
log(f"Found {len(all_era5_level_z_files)} files to process.")
log(f"Found {len(all_era5_surface_files)} files to process.")


# Open and process each year's data in chunks
train_hours = [0, 6, 12, 18]
test_hours = [1, 7, 13, 19]

# load without chunking on valid_time, rechunk valid_time after loading
log(f"Starting merge for ds1...")
ds1 = xr.open_mfdataset(all_era5_level_files, engine="h5netcdf", combine="by_coords", parallel=True, chunks={'latitude': 32, 'longitude': 32, 'model_level': 32})
ds1 = ds1.chunk({"valid_time": 100, "latitude": 32, "longitude": 32, "model_level": 32})
log(f"Done.")
log(f"Starting merge for ds2...")
ds2 = xr.open_mfdataset(all_era5_level_z_files, engine="h5netcdf", combine="by_coords", parallel=True, chunks={'latitude': 32, 'longitude': 32, 'model_level': 32})
ds2 = ds2.chunk({"valid_time": 100, "latitude": 32, "longitude": 32, "model_level": 32})
log(f"Done.")
log(f"Starting merge for ds3...")
ds3 = xr.open_mfdataset(all_era5_surface_files, engine="h5netcdf", combine="by_coords", parallel=True, chunks={'latitude': 32, 'longitude': 32})
ds3 = ds3.chunk({"valid_time": 100, "latitude": 32, "longitude": 32})
log(f"Done.")
# Assuming ds1, ds2, and ds3 have different variables but the same 'valid_time'
log(f"Starting merge for all...")
ds = xr.merge([ds1, ds2, ds3])
log(f"Merge complete.")

# Ensure 'valid_time' is in datetime format
if "valid_time" in ds.coords and not ds["valid_time"].dtype == "datetime64[ns]":
    ds["valid_time"] = ds["valid_time"].astype("datetime64[ns]")

#=======================================================================================

# Suppress specific warning message from xesmf
warnings.filterwarnings(
    "ignore", 
    message="Latitude is outside of \\[-90, 90\\]", 
    module="xesmf.backend"
)

# Load ClimT grid
climt_lat, climt_lon = climt_load['latitude'], climt_load['longitude']

climt_grid = xr.Dataset(
    {
        'lat': (['lat'], climt_lat),
        'lon': (['lon'], climt_lon),
    }
).chunk({"lat": 32, "lon": 32})

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def xr_regrid(ds, target_grid):
    chunk_dict = {"valid_time": 64, "latitude": 32, "longitude": 32}
    if "model_level" in ds.dims:
        chunk_dict["model_level"] = 32

    ds = ds.chunk(chunk_dict)

    regridder = xe.Regridder(ds, target_grid, method='conservative', periodic=True)

    regridded = regridder(ds, output_chunks={"lat": 32, "lon": 32})

    if 'pressure_level' in regridded.coords:
        regridded = regridded.assign_coords(
            pressure_level=np.flip(regridded.pressure_level.values) * 100
        )

    return regridded.chunk({"lat": 32, "lon": 32, "valid_time": 64})

# Train and test hours
train_hours = [0, 6, 12, 18]
test_hours = [1, 7, 13, 19]

# Years to process
years = range(2014, 2024)

save_tasks = []

log("Starting to process years...")

for i, year in enumerate(years):
    log(f"Processing year {year} ({i+1}/{len(years)})")

    ds_year = ds.sel(valid_time=ds.valid_time.dt.year == year)
    total_steps = ds_year.valid_time.size
    log(f"  Total time steps: {total_steps}")

    ds_train = ds_year.sel(valid_time=ds_year.valid_time.dt.hour.isin(train_hours))
    ds_test = ds_year.sel(valid_time=ds_year.valid_time.dt.hour.isin(test_hours))

    valid_times_train = ds_train.valid_time.dt.floor('D').values
    valid_times_test = ds_test.valid_time.dt.floor('D').values

    unique_days = np.unique(np.concatenate([valid_times_train, valid_times_test]))

    for dt in unique_days:
        py_dt = dt.astype("M8[ms]").astype(datetime)
        y, m, d = py_dt.year, py_dt.month, py_dt.day

        log(f"Processing {y}-{m:02d}-{d:02d}...")

        ds_train_day = ds_train.sel(valid_time=ds_train.valid_time.dt.floor('D') == dt)
        ds_test_day = ds_test.sel(valid_time=ds_test.valid_time.dt.floor('D') == dt)

        if ds_train_day.valid_time.size == 0 and ds_test_day.valid_time.size == 0:
            log(f"  Skipping {y}-{m:02d}-{d:02d} (no data).")
            continue

        ds_train_regrid = xr_regrid(ds_train_day, climt_grid)
        ds_test_regrid = xr_regrid(ds_test_day, climt_grid)

        train_day_dir = os.path.join(output_dir, "train", str(y), f"{m:02d}")
        test_day_dir = os.path.join(output_dir, "test", str(y), f"{m:02d}")
        os.makedirs(train_day_dir, exist_ok=True)
        os.makedirs(test_day_dir, exist_ok=True)

        train_day_path = os.path.join(train_day_dir, f"{y}{m:02d}{d:02d}_train.nc")
        test_day_path = os.path.join(test_day_dir, f"{y}{m:02d}{d:02d}_test.nc")

        # Delayed saving
        save_train = delayed(ds_train_regrid.to_netcdf)(train_day_path)
        save_test = delayed(ds_test_regrid.to_netcdf)(test_day_path)

        save_tasks.extend([save_train, save_test])

        # Trigger compute every 10 days
        if len(save_tasks) >= 10:
            log("Computing batch of 10 days...")
            compute(*save_tasks)
            save_tasks.clear()

# Final leftovers
if save_tasks:
    log("Computing final batch...")
    compute(*save_tasks)

log("All data processed and saved.")
