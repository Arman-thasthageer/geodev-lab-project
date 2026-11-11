import geopandas as gpd

source = gpd.read_file(
    "../../data/processed/settlements_utm44_clipped.gpkg",
    layer="settlements"
)

access = gpd.read_file(
    "../../data/week4/settlements_5km_access.gpkg",
    layer="settlements_5km_access"
)

# Create a geometry-based key to avoid duplicate-name joins.
source["_geom_key"] = source.geometry.to_wkb().map(bytes.hex)
access["_geom_key"] = access.geometry.to_wkb().map(bytes.hex)

population = source[["_geom_key", "population"]].copy()

# A geometry key must identify only one source population record.
duplicates = population["_geom_key"].duplicated(keep=False)
if duplicates.any():
    raise ValueError(
        "Duplicate source geometries found. Stop and inspect these records."
    )

joined = access.drop(columns=["population"], errors="ignore").merge(
    population,
    on="_geom_key",
    how="left",
    validate="many_to_one"
)

joined = joined.drop(columns=["_geom_key"])

joined["population_available"] = joined["population"].notna()

joined.drop(columns="geometry").to_csv(
    "data/settlements_accessibility_population.csv",
    index=False
)

print("Corrected population join")
print("Source settlements:", len(source))
print("Accessibility records:", len(access))
print("Joined records:", len(joined))
print("Population available:", int(joined["population"].notna().sum()))
print("Population missing:", int(joined["population"].isna().sum()))
print("\nAccess status:")
print(joined["access_status"].value_counts(dropna=False))

if len(joined) != len(access):
    raise ValueError("Record count changed unexpectedly.")
