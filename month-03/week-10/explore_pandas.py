import geopandas as gpd
import pandas as pd

path = "../../data/processed/settlements_utm44_clipped.gpkg"
settlements = gpd.read_file(path, layer="settlements")

print("Villupuram settlement dataset")
print("Rows:", len(settlements))
print("Columns:", list(settlements.columns))
print("\nFirst five records:")
print(settlements.drop(columns="geometry").head().to_string(index=False))
print("\nSettlement types:")
print(settlements["place"].value_counts(dropna=False))
print("\nPopulation summary:")
print(pd.to_numeric(settlements["population"], errors="coerce").describe())
print("Missing population:", settlements["population"].isna().sum())
