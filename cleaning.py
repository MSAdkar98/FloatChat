import pandas as pd

# Load extracted dataset
df = pd.read_csv("argo_combined_dataset.csv")

# Remove rows with missing core values
df = df.dropna(subset=["pressure", "temperature"])

# Convert pressure to numeric (safety)
df["pressure"] = pd.to_numeric(df["pressure"], errors="coerce")

# Remove invalid measurements
df = df.dropna()

df = df[
    (df["latitude"] >= -30) &
    (df["latitude"] <= 30) &
    (df["longitude"] >= 40) &
    (df["longitude"] <= 110)
]

# Depth filter (pressure ≈ depth in meters)
df = df[df["pressure"] <= 1000]

# Remove unrealistic temperatures
df = df[
    (df["temperature"] > -2) &
    (df["temperature"] < 40)
]

# Reset index
df = df.reset_index(drop=True)

# Save cleaned dataset
df.to_csv("argo_cleaned_bay_of_bengal.csv", index=False)

print("Cleaning complete")
print("Remaining records:", len(df))