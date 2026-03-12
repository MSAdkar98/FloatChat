import xarray as xr
import glob

files = glob.glob("raw_argo_profiles/*.nc")

for f in files:

    ds = xr.open_dataset(f)

    print("\nFile:", f)
    print("Profiles:", ds.sizes.get("N_PROF"))
    print("Levels:", ds.sizes.get("N_LEVELS"))


for f in files:
    ds = xr.open_dataset(f)
    lat = ds["LATITUDE"].values[0]
    lon = ds["LONGITUDE"].values[0]

    print(f, "->", lat, lon)