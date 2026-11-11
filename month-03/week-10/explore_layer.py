import geopandas as gpd

datasets = [
    ("Health facilities", "../../data/processed/health_facilities_utm44_clipped.gpkg", "health_facilities"),
    ("Road network", "../../data/processed/roads_utm44_clipped.gpkg", "roads"),
    ("Settlements", "../../data/processed/settlements_utm44_clipped.gpkg", "settlements"),
    ("District boundary", "../../data/processed/villupuram_boundary_utm44.gpkg", "villupuram_boundary"),
]

for label, path, layer in datasets:
    gdf = gpd.read_file(path, layer=layer)
    print(f"\n{label}")
    print("Features:", len(gdf))
    print("CRS:", gdf.crs)
    print("Geometry types:", gdf.geom_type.value_counts().to_dict())
    print("Fields:", [c for c in gdf.columns if c != "geometry"])
