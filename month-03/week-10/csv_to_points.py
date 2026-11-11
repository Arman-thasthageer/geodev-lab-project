import geopandas as gpd
import pandas as pd

facilities = gpd.read_file(
    "../../data/processed/health_facilities_utm44_clipped.gpkg",
    layer="health_facilities"
)

# Export coordinates from the real facility point geometries.
table = facilities.drop(columns="geometry").copy()
table["x_utm44"] = facilities.geometry.x
table["y_utm44"] = facilities.geometry.y
table.to_csv("data/health_facilities_coordinates.csv", index=False)

# Reconstruct points from those exported coordinates.
coordinates = pd.read_csv("data/health_facilities_coordinates.csv")
points = gpd.GeoDataFrame(
    coordinates,
    geometry=gpd.points_from_xy(coordinates["x_utm44"], coordinates["y_utm44"]),
    crs="EPSG:32644"
)
points.to_file("data/health_facilities_from_csv.geojson", driver="GeoJSON")

print("Real facility points exported and reconstructed.")
print("Facilities:", len(points))
print("CRS:", points.crs)
