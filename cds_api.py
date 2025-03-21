import cdsapi
import datetime


def download_era5_data(start_date, end_date, output_dir="/run/media/adamh/Elements/training_data/"):
    c = cdsapi.Client()

    # Model level data (excluding z)
    c.retrieve(
        "reanalysis-era5-complete",
        {
            "class": "ea",
            "expver": "1",
            "levtype": "ml",
            "levelist": "1/to/137",
            "param": "130.128/131.128/132.128/155.128/138.128/133.128",  # t, u, v, d, vo, q
            "date": f"{start_date}/to/{end_date}",
            "time": ["00:00", "01:00", "06:00", "07:00", "12:00", "13:00", "18:00", "19:00"],
            "step": "0",
            "grid": "1.5/1.5",
            "area": [90, -180, -90, 180],
            "format": "netcdf",
        },
        f"{output_dir}era5_model_levels_{start_date}_{end_date}.nc",
    )

    # Model level data for geopotential (z)
    c.retrieve(
        "reanalysis-era5-complete",
        {
            "class": "ea",
            "expver": "1",
            "levtype": "ml",
            "levelist": "1/to/137",
            "param": "129.128",  # z
            "date": f"{start_date}/to/{end_date}",
            "time": ["00:00", "01:00", "06:00", "07:00", "12:00", "13:00", "18:00", "19:00"],
            "step": "0",
            "grid": "1.5/1.5",
            "area": [90, -180, -90, 180],
            "format": "netcdf",
        },
        f"{output_dir}era5_model_levels_z_{start_date}_{end_date}.nc",
    )

    # Surface level data for MSLP
    c.retrieve(
        "reanalysis-era5-complete",
        {
            "class": "ea",
            "expver": "1",
            "levtype": "sfc",
            "param": "151.128",  # MSLP
            "date": f"{start_date}/to/{end_date}",
            "time": ["00:00", "01:00", "06:00", "07:00", "12:00", "13:00", "18:00", "19:00"],
            "step": "0",
            "grid": "1.5/1.5",
            "area": [90, -180, -90, 180],
            "format": "netcdf",
        },
        f"{output_dir}era5_surface_levels_{start_date}_{end_date}.nc",
    )


# Loop over the date range in 10-day increments
start_date = datetime.date(2014, 8, 31)
end_date = datetime.date(2024, 12, 31)
delta = datetime.timedelta(days=10)

current_date = start_date
while current_date <= end_date:
    next_date = min(current_date + delta, end_date)
    download_era5_data(current_date.strftime("%Y-%m-%d"), next_date.strftime("%Y-%m-%d"))
    current_date = next_date + datetime.timedelta(days=1)