import xarray as xr
import pandas as pd
import glob

files = glob.glob("raw_argo_profiles/*.nc")

all_data = []

for file in files:

    ds = xr.open_dataset(file)

    # Possible variable names
    pressure_candidates = ['PRES_ADJUSTED', 'PRES']
    temp_candidates = ['TEMP_ADJUSTED', 'TEMP', 'TEMP_DOXY', 'TEMP_PH']
    sal_candidates = ['PSAL_ADJUSTED', 'PSAL']

    # Find available variable
    pressure_var = next((v for v in pressure_candidates if v in ds), None)
    temp_var = next((v for v in temp_candidates if v in ds), None)
    sal_var = next((v for v in sal_candidates if v in ds), None)

    # Skip file if essential variables missing
    if pressure_var is None or temp_var is None:
        print("Skipping file:", file)
        continue

    pressure = ds[pressure_var][0].values
    temperature = ds[temp_var][0].values

    # Salinity optional
    if sal_var:
        salinity = ds[sal_var][0].values
    else:
        salinity = [None] * len(pressure)

    lat = ds['LATITUDE'].values[0]
    lon = ds['LONGITUDE'].values[0]
    time = ds['JULD'].values[0]
    float_id = ds['PLATFORM_NUMBER'].values[0]

    df = pd.DataFrame({
        "pressure": pressure,
        "temperature": temperature,
        "salinity": salinity
    })

    df["latitude"] = lat
    df["longitude"] = lon
    df["time"] = time
    df["float_id"] = float_id

    df = df.dropna(subset=["pressure", "temperature"])

    all_data.append(df)

combined = pd.concat(all_data, ignore_index=True)

combined.to_csv("argo_combined_dataset.csv", index=False)

print("Processing finished")
print("Total records:", len(combined))