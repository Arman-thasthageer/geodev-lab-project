import geopandas as gpd

access = gpd.read_file(
    "../../data/week4/settlements_5km_access.gpkg",
    layer="settlements_5km_access"
)

# The source accessibility layer already contains population.
# Preserve its original settlement-level records without another join.
table = access.drop(columns="geometry").copy()

table.to_csv("wards_table.csv", index=False)
table.to_csv("data/settlements_accessibility.csv", index=False)

print("Corrected course output")
print("Records:", len(table))
print("Population available:", int(table["population"].notna().sum()))
print("Population missing:", int(table["population"].isna().sum()))
print("\nAccess status:")
print(table["access_status"].value_counts(dropna=False))

if len(table) != 124:
    raise ValueError("Expected 124 settlement records. Investigate before upload.")
