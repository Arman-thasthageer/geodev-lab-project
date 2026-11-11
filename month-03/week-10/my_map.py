import geopandas as gpd
import matplotlib.pyplot as plt

boundary = gpd.read_file(
    "../../data/processed/villupuram_boundary_utm44.gpkg",
    layer="villupuram_boundary"
)
facilities = gpd.read_file(
    "../../data/processed/health_facilities_utm44_clipped.gpkg",
    layer="health_facilities"
)
access = gpd.read_file(
    "../../data/week4/settlements_5km_access.gpkg",
    layer="settlements_5km_access"
)

inside = access[access["access_status"] == "Within 5 km"]
outside = access[access["access_status"] == "Outside 5 km"]

fig, ax = plt.subplots(figsize=(10, 10))
boundary.boundary.plot(ax=ax, color="black", linewidth=1.2)
inside.plot(ax=ax, color="seagreen", markersize=9, label="Within 5 km")
outside.plot(ax=ax, color="red", marker="^", markersize=20, label="Outside 5 km")
facilities.plot(ax=ax, color="navy", marker="*", markersize=15, label="Health facilities")

ax.set_title("Independent Analysis: Villupuram Health Facility Coverage")
ax.set_xlabel("Easting (metres)")
ax.set_ylabel("Northing (metres)")
ax.legend()
ax.set_aspect("equal")
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig("my_map.png", dpi=300, bbox_inches="tight")
plt.close(fig)

print("Created my_map.png")
