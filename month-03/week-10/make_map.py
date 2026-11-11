import geopandas as gpd
import matplotlib.pyplot as plt

boundary = gpd.read_file(
    "../../data/processed/villupuram_boundary_utm44.gpkg",
    layer="villupuram_boundary"
)
roads = gpd.read_file(
    "../../data/processed/roads_utm44_clipped.gpkg",
    layer="roads"
)
facilities = gpd.read_file(
    "../../data/processed/health_facilities_utm44_clipped.gpkg",
    layer="health_facilities"
)
access = gpd.read_file(
    "../../data/week4/settlements_5km_access.gpkg",
    layer="settlements_5km_access"
)

fig, ax = plt.subplots(figsize=(11, 11))
boundary.boundary.plot(ax=ax, color="black", linewidth=1.2, label="District boundary")
roads.plot(ax=ax, color="lightgrey", linewidth=0.25, alpha=0.65)

inside = access[access["access_status"] == "Within 5 km"]
outside = access[access["access_status"] == "Outside 5 km"]

inside.plot(ax=ax, color="green", markersize=10, alpha=0.75, label="Settlement within 5 km")
outside.plot(ax=ax, color="red", markersize=18, marker="^", label="Settlement outside 5 km")
facilities.plot(ax=ax, color="blue", markersize=13, marker="*", label="Health facility")

ax.set_title("Villupuram: Health Facilities and 5 km Settlement Coverage")
ax.set_xlabel("Easting (metres) ? EPSG:32644")
ax.set_ylabel("Northing (metres) ? EPSG:32644")
ax.legend(loc="best")
ax.set_aspect("equal")
ax.grid(alpha=0.2)
fig.tight_layout()
fig.savefig("facilities_map.png", dpi=300, bbox_inches="tight")
plt.close(fig)

print("Created facilities_map.png")
print("Facilities:", len(facilities))
print("Settlements:", len(access))
print("Within 5 km:", len(inside))
print("Outside 5 km:", len(outside))
