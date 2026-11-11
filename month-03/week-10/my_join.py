import geopandas as gpd
import pandas as pd

settlements = gpd.read_file(
    "../../data/processed/settlements_utm44_clipped.gpkg",
    layer="settlements"
)
facilities = gpd.read_file(
    "../../data/processed/health_facilities_utm44_clipped.gpkg",
    layer="health_facilities"
)
access = gpd.read_file(
    "../../data/week4/settlements_5km_access.gpkg",
    layer="settlements_5km_access"
)

# Use representative points so polygon settlements are handled consistently.
settlement_points = settlements.copy()
settlement_points["geometry"] = settlement_points.geometry.representative_point()
settlement_points = settlement_points.reset_index(drop=True)
settlement_points["_settlement_id"] = settlement_points.index

# Count actual health facility points within 5,000 metres of each
# settlement representative point. This is Euclidean, not road-network distance.
buffers = settlement_points[["_settlement_id", "name", "place", "geometry"]].copy()
buffers["geometry"] = buffers.geometry.buffer(5000)

matches = gpd.sjoin(
    buffers,
    facilities[["geometry"]],
    how="left",
    predicate="intersects"
)

counts = (
    matches.groupby("_settlement_id")["index_right"]
    .nunique()
    .rename("facilities_within_5km")
    .reset_index()
)

result = settlement_points.drop(columns="geometry").merge(
    counts, on="_settlement_id", how="left"
)
result["facilities_within_5km"] = (
    result["facilities_within_5km"].fillna(0).astype(int)
)

access_table = access[["name", "place", "access_status"]].drop_duplicates(
    subset=["name", "place"]
)
result = result.merge(access_table, on=["name", "place"], how="left")
result.to_csv("data/my_settlement_facility_counts.csv", index=False)

print("Settlement-to-facility spatial join complete.")
print("Settlements:", len(result))
print("Total facilities counted within settlement 5 km buffers:",
      int(result["facilities_within_5km"].sum()))
print("Output: data/my_settlement_facility_counts.csv")
