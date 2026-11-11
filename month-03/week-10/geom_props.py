import geopandas as gpd

boundary = gpd.read_file(
    "../../data/processed/villupuram_boundary_utm44.gpkg",
    layer="villupuram_boundary"
)
facilities = gpd.read_file(
    "../../data/processed/health_facilities_utm44_clipped.gpkg",
    layer="health_facilities"
)
settlements = gpd.read_file(
    "../../data/processed/settlements_utm44_clipped.gpkg",
    layer="settlements"
)

print("CRS:", boundary.crs)
print("District area (sq. km):", round(boundary.geometry.area.sum() / 1_000_000, 2))
print("District boundary length (km):", round(boundary.geometry.length.sum() / 1000, 2))
print("Health facilities:", len(facilities))
print("Settlements:", len(settlements))
print("Point settlements:", int((settlements.geom_type == "Point").sum()))
print("Polygon settlements:", int((settlements.geom_type == "Polygon").sum()))
