import xarray as xr

file = "R1902845_003.nc"

ds = xr.open_dataset(file)

lat = float(ds["LATITUDE"].values[0])
lon = float(ds["LONGITUDE"].values[0])

print("Latitude:", lat)
print("Longitude:", lon)

# Bay of Bengal bounds
if 5 <= lat <= 23 and 80 <= lon <= 100:
    print("Inside Bay of Bengal")
else:
    print("Outside Bay of Bengal")