ERA5 DATA HAS DEGRADDED, THIS .TXT SHOWS HOW THIS DEGREDATION AFFECTS THE RESULTS AT HAND. DATA DOWNLOADED PRE DEGREDATION IS AVAILABLE 
AND IS USED TO CONDUCT THESE COMPARISONS. SEE BELOW FOR SOURCES REGRADING THIS. NOTE EVEN POST FIX THERE ARE STILL DISCREPANCIES:

https://eur01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fforum.ecmwf.int%2Ft%2Fera5-data-from-1st-january-2025-was-degraded-and-is-being-corrected%2F10689&data=05%7C02%7Camh231%40bath.ac.uk%7Caad73f8aaffa46db537908dd3ea79ae9%7C377e3d224ea1422db0ad8fcc89406b9e%7C0%7C0%7C638735611772332423%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=VGHXz5L3Bwxz9GUKGdhbKP3d4HYqdFKzLNeLfdvvG08%3D&reserved=0

RESULTS: GIVEN THE MAX MEAN ERROR IS e-6, ALONG WITH ANALYSIS OF RESULTING SIMULATIONS USING PRE AND POST DATA DEGRREDATION
IT IS DEEMED THIS DEGREGATION WILL NOT BE IMPACTFUL TO THE FINAL RESULTS, SIMULATIONS WILL PROCEED AS NORMAL.


=============================================== SINGLE LEVELS =========================================================

newly obtained data from api req =  <xarray.Dataset> Size: 4MB
Dimensions:     (latitude: 721, longitude: 1440)
Coordinates:
    number      int64 8B ...
    valid_time  datetime64[ns] 8B 2018-01-01
  * latitude    (latitude) float64 6kB 90.0 89.75 89.5 ... -89.5 -89.75 -90.0
  * longitude   (longitude) float64 12kB 0.0 0.25 0.5 0.75 ... 359.2 359.5 359.8
    expver      <U4 16B ...
Data variables:
    msl         (latitude, longitude) float32 4MB ...
Attributes:
    GRIB_centre:             ecmf
    GRIB_centreDescription:  European Centre for Medium-Range Weather Forecasts
    GRIB_subCentre:          0
    Conventions:             CF-1.7
    institution:             European Centre for Medium-Range Weather Forecasts
    history:                 2025-01-25T11:50 GRIB to CDM+CF via cfgrib-0.9.1...



previously used data for old sims =  <xarray.Dataset> Size: 4MB
Dimensions:     (latitude: 721, longitude: 1440)
Coordinates:
    number      int64 8B ...
    valid_time  datetime64[ns] 8B 2018-01-01
  * latitude    (latitude) float64 6kB 90.0 89.75 89.5 ... -89.5 -89.75 -90.0
  * longitude   (longitude) float64 12kB 0.0 0.25 0.5 0.75 ... 359.2 359.5 359.8
    expver      <U4 16B ...
Data variables:
    msl         (latitude, longitude) float32 4MB ...
Attributes:
    GRIB_centre:             ecmf
    GRIB_centreDescription:  European Centre for Medium-Range Weather Forecasts
    GRIB_subCentre:          0
    Conventions:             CF-1.7
    institution:             European Centre for Medium-Range Weather Forecasts
    history:                 2024-12-11T11:01 GRIB to CDM+CF via cfgrib-0.9.1...



(api_data_single['valid_time'].values - old_data_single['valid_time'].values).mean() =  0 nanoseconds
(api_data_single['longitude'].values - old_data_single['longitude'].values).mean() =  0.0
(api_data_single['latitude'].values - old_data_single['latitude'].values).mean() =  0.0
(api_data_single['msl'].values - old_data_single['msl'].values).mean() =  0.0

=============================================== PRESSURE LEVELS =========================================================

newly obtained data from api req =  <xarray.Dataset> Size: 1GB
Dimensions:         (latitude: 721, longitude: 1440, pressure_level: 37)
Coordinates:
    number          int64 8B ...
    valid_time      datetime64[ns] 8B 2018-01-01
  * latitude        (latitude) float64 6kB 90.0 89.75 89.5 ... -89.75 -90.0
  * longitude       (longitude) float64 12kB 0.0 0.25 0.5 ... 359.2 359.5 359.8
    expver          <U4 16B ...
  * pressure_level  (pressure_level) float64 296B 1.0 2.0 3.0 ... 975.0 1e+03
Data variables:
    d               (pressure_level, latitude, longitude) float32 154MB ...
    z               (pressure_level, latitude, longitude) float32 154MB ...
    q               (pressure_level, latitude, longitude) float32 154MB ...
    t               (pressure_level, latitude, longitude) float32 154MB ...
    u               (pressure_level, latitude, longitude) float32 154MB ...
    v               (pressure_level, latitude, longitude) float32 154MB ...
    vo              (pressure_level, latitude, longitude) float32 154MB ...
Attributes:
    GRIB_centre:             ecmf
    GRIB_centreDescription:  European Centre for Medium-Range Weather Forecasts
    GRIB_subCentre:          0
    Conventions:             CF-1.7
    institution:             European Centre for Medium-Range Weather Forecasts
    history:                 2025-01-24T10:37 GRIB to CDM+CF via cfgrib-0.9.1...



previously used data for old sims =  <xarray.Dataset> Size: 2GB
Dimensions:    (longitude: 1440, latitude: 721, level: 37)
Coordinates:
  * longitude  (longitude) float32 6kB 0.0 0.25 0.5 0.75 ... 359.2 359.5 359.8
  * latitude   (latitude) float32 3kB 90.0 89.75 89.5 ... -89.5 -89.75 -90.0
  * level      (level) int32 148B 1 2 3 5 7 10 20 ... 875 900 925 950 975 1000
    time       datetime64[ns] 8B 2018-01-01
Data variables:
    d          (level, latitude, longitude) float64 307MB ...
    z          (level, latitude, longitude) float64 307MB ...
    q          (level, latitude, longitude) float64 307MB ...
    t          (level, latitude, longitude) float64 307MB ...
    u          (level, latitude, longitude) float64 307MB ...
    v          (level, latitude, longitude) float64 307MB ...
    vo         (level, latitude, longitude) float64 307MB ...
Attributes:
    Conventions:  CF-1.6
    history:      2024-09-02 10:50:14 GMT by grib_to_netcdf-2.28.1: /opt/ecmw...



(api_data['valid_time'].values - old_data['time'].values).mean() =  0 nanoseconds
(api_data['longitude'].values - old_data['longitude'].values).mean() =  0.0
(api_data['latitude'].values - old_data['latitude'].values).mean() =  0.0
(api_data['pressure_level'].values - old_data['level'].values).mean() =  0.0
(api_data['d'].values - old_data['d'].values).mean() =  -1.0075380344550254e-12
(api_data['z'].values - old_data['z'].values).mean() =  -0.0011475703620580165
(api_data['q'].values - old_data['q'].values).mean() =  -4.309749629771563e-09
(api_data['t'].values - old_data['t'].values).mean() =  -1.033884399639329e-06
(api_data['u'].values - old_data['u'].values).mean() =  1.130735248155182e-07
(api_data['v'].values - old_data['v'].values).mean() =  3.194428431349863e-07
(api_data['vo'].values - old_data['vo'].values).mean() =  2.6458210026194273e-12

=============================================== REGRIDDING =========================================================

api_data =  <xarray.Dataset> Size: 34kB
Dimensions:     (lat: 64, lon: 128)
Coordinates:
    number      int64 8B ...
    valid_time  datetime64[ns] 8B 2018-01-01
    expver      <U4 16B ...
  * lat         (lat) float64 512B 87.86 85.1 82.31 ... -82.31 -85.1 -87.86
  * lon         (lon) float64 1kB 0.0 2.812 5.625 8.438 ... 351.6 354.4 357.2
Data variables:
    msl         (lat, lon) float32 33kB ...
Attributes:
    regrid_method:  conservative



old_data =  <xarray.Dataset> Size: 17MB
Dimensions:                         (lat: 64, lon: 128, level: 37)
Coordinates:
    time                            datetime64[ns] 8B ...
  * lat                             (lat) float64 512B 87.86 85.1 ... -87.86
  * lon                             (lon) float64 1kB 0.0 2.812 ... 354.4 357.2
  * level                           (level) int32 148B 100000 97500 ... 200 100
    number                          int64 8B ...
    valid_time                      datetime64[ns] 8B ...
    expver                          <U4 16B ...
Data variables:
    divergence_of_wind_regrid       (level, lat, lon) float64 2MB ...
    geopotential_regrid             (level, lat, lon) float64 2MB ...
    specific_humidity_regrid        (level, lat, lon) float64 2MB ...
    air_temperature_regrid          (level, lat, lon) float64 2MB ...
    eastward_wind_regrid            (level, lat, lon) float64 2MB ...
    northward_wind_regrid           (level, lat, lon) float64 2MB ...
    relative_vorticity_regrid       (level, lat, lon) float64 2MB ...
    dewpoint_temperature_regrid     (lat, lon) float64 66kB ...
    surface_temperature_regrid      (lat, lon) float64 66kB ...
    surface_geopotential_regrid     (lat, lon) float64 66kB ...
    surface_pressure_regrid         (lat, lon) float64 66kB ...
    mean_sea_level_pressure_regrid  (lat, lon) float32 33kB ...



(api_data.valid_time.values - old_data.time.values).mean() =  0 nanoseconds
(api_data.lat.values - old_data.lat.values).mean() =  0.0
(api_data.lon.values - old_data.lon.values).mean() =  0.0
(api_data.pressure_level.values - old_data.level.values).mean() =  0.0
(api_data['d'].values - old_data['divergence_of_wind_regrid'].values).mean() =  -2.674572115364598e-13
(api_data['z'].values - old_data['geopotential_regrid'].values).mean() =  -0.0004993339479328886
(api_data['q'].values - old_data['specific_humidity_regrid'].values).mean() =  -4.3415758787729736e-09
(api_data['t'].values - old_data['air_temperature_regrid'].values).mean() =  -9.148024589688695e-07
(api_data['u'].values - old_data['eastward_wind_regrid'].values).mean() =  -6.917938474530739e-08
(api_data['v'].values - old_data['northward_wind_regrid'].values).mean() =  -1.0222987671759073e-07
(api_data['vo'].values - old_data['relative_vorticity_regrid'].values).mean() =  4.035909805622549e-14
(api_data_p['msl'].values - old_data['mean_sea_level_pressure_regrid'].values).mean() =  0.0

=============================================== INTERPOLATING =========================================================

api_data =  <xarray.Dataset> Size: 17MB
Dimensions:         (mid_levels: 37, lat: 64, lon: 128, pressure_level: 37)
Coordinates:
    number          int64 8B ...
    expver          <U4 16B ...
  * lat             (lat) float64 512B 87.86 85.1 82.31 ... -82.31 -85.1 -87.86
  * lon             (lon) float64 1kB 0.0 2.812 5.625 ... 351.6 354.4 357.2
  * pressure_level  (pressure_level) float64 296B 1e+05 9.75e+04 ... 200.0 100.0
    valid_time      datetime64[ns] 8B 2018-01-01
Dimensions without coordinates: mid_levels
Data variables:
    d               (mid_levels, lat, lon) float64 2MB ...
    z               (mid_levels, lat, lon) float64 2MB ...
    q               (mid_levels, lat, lon) float64 2MB ...
    t               (mid_levels, lat, lon) float64 2MB ...
    u               (mid_levels, lat, lon) float64 2MB ...
    v               (mid_levels, lat, lon) float64 2MB ...
    vo              (mid_levels, lat, lon) float64 2MB ...
Attributes:
    regrid_method:  conservative



old_data =  <xarray.Dataset> Size: 17MB
Dimensions:                          (lat: 64, lon: 128, mid_levels: 37)
Coordinates:
  * lat                              (lat) float64 512B 87.86 85.1 ... -87.86
  * lon                              (lon) float64 1kB 0.0 2.812 ... 354.4 357.2
    time                             datetime64[ns] 8B ...
    number                           int64 8B ...
    valid_time                       datetime64[ns] 8B ...
    expver                           <U4 16B ...
Dimensions without coordinates: mid_levels
Data variables:
    divergence_of_wind_interpolated  (mid_levels, lat, lon) float64 2MB ...
    geopotential_interpolated        (mid_levels, lat, lon) float64 2MB ...
    specific_humidity_interpolated   (mid_levels, lat, lon) float64 2MB ...
    air_temperature_interpolated     (mid_levels, lat, lon) float64 2MB ...
    eastward_wind_interpolated       (mid_levels, lat, lon) float64 2MB ...
    northward_wind_interpolated      (mid_levels, lat, lon) float64 2MB ...
    relative_vorticity_interpolated  (mid_levels, lat, lon) float64 2MB ...
    dewpoint_temperature_regrid      (lat, lon) float64 66kB ...
    surface_temperature_regrid       (lat, lon) float64 66kB ...
    surface_geopotential_regrid      (lat, lon) float64 66kB ...
    surface_pressure_regrid          (lat, lon) float64 66kB ...
    mean_sea_level_pressure_regrid   (lat, lon) float32 33kB ...



(api_data.valid_time.values - old_data.time.values).mean() =  0 nanoseconds
(api_data.lat.values - old_data.lat.values).mean() =  0.0
(api_data.lon.values - old_data.lon.values).mean() =  0.0
(api_data.mid_levels.values - old_data.mid_levels.values).mean() =  0.0
(api_data['d'].values - old_data['divergence_of_wind_regrid'].values).mean() =  2.387385891914787e-13
(api_data['z'].values - old_data['geopotential_regrid'].values).mean() =  -0.00029948189081765894
(api_data['q'].values - old_data['specific_humidity_regrid'].values).mean() =  -2.2405801230912147e-09
(api_data['t'].values - old_data['air_temperature_regrid'].values).mean() =  -1.1230299001866083e-06
(api_data['u'].values - old_data['eastward_wind_regrid'].values).mean() =  -1.488579952167825e-07
(api_data['v'].values - old_data['northward_wind_regrid'].values).mean() =  -3.01947407201255e-08
(api_data['vo'].values - old_data['relative_vorticity_regrid'].values).mean() =  1.2806735807764016e-12


==============================================================================================================
=================================================== SUMMARY ==================================================
==============================================================================================================


| Variable                        | Base Data Error       | Regrid Data Error     | Interpolation Error    |
|---------------------------------|-----------------------|-----------------------|------------------------|
| `msl`                           | 0.0                   | 0.0                   | 0.0                    |
| `d`                             | -1.01e-12             | -2.67e-13             | 2.39e-13               |
| `z`                             | -1.15e-3              | -5.00e-4              | -3.00e-4               |
| `q`                             | -4.31e-9              | -4.34e-9              | -2.24e-9               |
| `t`                             | -1.03e-6              | -9.15e-7              | -1.12e-6               |
| `u`                             | 1.13e-7               | -6.92e-8              | -1.49e-7               |
| `v`                             | 3.19e-7               | -1.02e-7              | -3.02e-8               |
| `vo`                            | 2.65e-12              | 4.04e-14              | 1.28e-12               |


