import geopandas as gpd

facilities = gpd.read_file(
    "../../data/processed/health_facilities_utm44_clipped.gpkg",
    layer="health_facilities"
)

facilities.to_file("data/my_facilities_points.geojson", driver="GeoJSON")

print("Independent point-layer export")
print("Health facility points:", len(facilities))
print("CRS:", facilities.crs)
print("Output: data/my_facilities_points.geojson")
