import geopandas as gpd

settlements = gpd.read_file(
    "../../data/processed/settlements_utm44_clipped.gpkg",
    layer="settlements"
)
access = gpd.read_file(
    "../../data/week4/settlements_5km_access.gpkg",
    layer="settlements_5km_access"
)

print("Independent Villupuram settlement analysis")
print("Total settlements:", len(settlements))
print("\nBy settlement type:")
print(settlements["place"].value_counts(dropna=False))
print("\nPopulation data:")
print("Available:", int(settlements["population"].notna().sum()))
print("Missing:", int(settlements["population"].isna().sum()))
print("\n5 km coverage:")
print(access["access_status"].value_counts(dropna=False))
