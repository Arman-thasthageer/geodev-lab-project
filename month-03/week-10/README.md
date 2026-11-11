# Month 3 ? Week 10: GeoPandas with Villupuram Data

## Project
This week applies pandas and GeoPandas to the actual Villupuram district GIS project developed in earlier months.

## Actual source datasets
All source data are reused from the existing repository:
- 169 clipped health facility points
- 9,431 clipped road features
- 124 settlement features (118 points and 6 polygons)
- Villupuram district boundary
- Week 4 settlement accessibility layer

All processed spatial layers use **EPSG:32644 (WGS 84 / UTM zone 44N)**.

## Guided scripts
1. `explore_pandas.py` ? inspect settlement attributes and missing population.
2. `filter_sort.py` ? filter and sort settlements outside the 5 km coverage.
3. `explore_layer.py` ? inspect the four actual GIS layers.
4. `geom_props.py` ? calculate district area and boundary length.
5. `csv_to_points.py` ? export actual facility coordinates to CSV and reconstruct points.
6. `join_population.py` ? join original population attributes to accessibility records.
7. `make_map.py` ? map roads, settlements, facilities and coverage status.
8. `save_outputs.py` ? export settlement-level accessibility data.

## Independent challenge
- `my_explore.py` ? independent settlement and population summary.
- `my_points.py` ? export actual health facility points.
- `my_join.py` ? count facilities within 5 km of each settlement representative point.
- `my_map.py` ? create an independent coverage map.

## Main outputs
- `facilities_map.png`
- `wards_table.csv`
- `my_map.png`
- `data/settlements_accessibility.csv`
- `data/settlements_accessibility_population.csv`
- `data/my_settlement_facility_counts.csv`
- `data/health_facilities_coordinates.csv`
- `data/health_facilities_from_csv.geojson`

## Important interpretation and limitations
The course-required filename `wards_table.csv` is retained, but its rows are actual settlement records. The source project does not contain a verified ward-level population dataset. Do not interpret this file as ward statistics.

The Week 4 5 km coverage classification is a straight-line buffer analysis, not road-network travel distance or travel time. The independent facility count uses 5 km Euclidean buffers around settlement representative points. It does not estimate driving or walking accessibility.

Population is missing for many settlements in the source data. Missing values are kept missing; no population values are invented or imputed.

## Run
From this folder, run the scripts with `py script_name.py`. Required packages: geopandas, pandas and matplotlib.
