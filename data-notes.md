# Week 2 — Data Notes

## Project

Which settlements in Villupuram district, Tamil Nadu, are more than 5 km by road from the nearest public health facility?

---

## 1. Villupuram District Boundary

**Source:** Tamil Nadu GIS (TNGIS)

**Source link:** https://www.tngis.tn.gov.in/

**Geometry:** Polygon

**Features:** 1

**Purpose:** Used to define the study area for Villupuram district.

**Observations:** The boundary is used to limit the spatial datasets to the study area.

---

## 2. OSM Settlements

**Source:** OpenStreetMap

**Source link:** https://www.openstreetmap.org/

**Download method:** Python using OSMnx

**Features:** 131

**Geometry:**
- Point: 124
- Polygon: 7

**Key information:** Settlement names and OSM place information.

**Observations:** The dataset contains both point and polygon geometries. Some OSM features may have missing names or other attributes because OpenStreetMap coverage depends on mapping completeness.

---

## 3. OSM Health Facilities

**Source:** OpenStreetMap

**Source link:** https://www.openstreetmap.org/

**Download method:** Python using OSMnx

**Geometry:** Point/polygon features depending on the mapped facility.

**Purpose:** Used to identify public health facilities for the healthcare accessibility analysis.

**Observations:** OpenStreetMap health-facility coverage may be incomplete, so the facilities will be cross-checked with an official government source during later analysis.

---

## 4. Road Network

**Source:** OpenStreetMap

**Source link:** https://www.openstreetmap.org/

**Download method:** OpenStreetMap road dataset

**Geometry:** LineString

**Purpose:** Used for the future road-network accessibility analysis.

**Observations:** The road dataset contains different road classes. Some roads may have missing names or other attributes. Road classification will be reviewed before calculating network distance.

---

## 5. Census Population Data

**Source:** Census of India 2011

**Source link:** https://censusindia.gov.in/

**File:** DDW_PCA3306_2011_MDDS with UI.xlsx

**Rows:** 1,867

**Columns:** 94

**Geometry:** Non-spatial table

**Key columns:**
- State
- District
- Subdistt
- Town/Village
- Level
- Name
- No_HH
- TOT_P
- TOT_M
- TOT_F

**Observations:** The Census table contains population and settlement information but does not contain latitude/longitude coordinates. Spatial settlement geometry will therefore be handled separately.

---

## Week 2 Summary

The project data has been obtained from real sources and prepared for GIS analysis. OpenStreetMap data provides settlement, health-facility and road information, while Census data provides population information. The datasets will be inspected and combined in later weeks to assess healthcare accessibility.
