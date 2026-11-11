import geopandas as gpd

path = "../../data/week4/settlements_5km_access.gpkg"
access = gpd.read_file(path, layer="settlements_5km_access")

outside = access[access["access_status"] == "Outside 5 km"].copy()
outside = outside.sort_values("name", na_position="last")

print("Settlements outside the 5 km straight-line coverage area:")
print(outside[["name", "place", "access_status"]].to_string(index=False))
print("\nOutside count:", len(outside))
outside.drop(columns="geometry").to_csv(
    "data/settlements_outside_5km.csv", index=False
)
