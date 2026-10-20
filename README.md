# geodev-lab-project
GeoDev Africa – Villupuram GIS Project

# geodev-lab-project

GeoDev Africa – Villupuram GIS Project
## Month 2: Development Environment and Early Python

### Week 5: Python and VS Code Setup
Set up Python, Visual Studio Code, and the terminal. Created and successfully ran `hello.py`.

### Week 6: Project Environments with uv

**Objective:** Set up a Python project environment using `uv` and install the pandas library.

**Tasks completed:**
- Installed and verified `uv` version `0.13.0`.
- Initialized the Python project using `uv init --bare`.
- Added `pandas` as a project dependency using `uv add pandas`.
- Created a Python virtual environment (`.venv`).
- Generated `pyproject.toml` to record project configuration and dependencies.
- Generated `uv.lock` to lock dependency versions.
- Created `check.py` to verify the pandas installation.
- Successfully executed the script using `uv run check.py`.

**Verification output:**

```text
uv 0.13.0
Week 6: Python project setup successful!
Pandas version: 3.0.6
```

**Files submitted:**
- `pyproject.toml`
- `uv.lock`
- `check.py`
- `screenshots/week6.png`

**Outcome:** Successfully configured a reproducible Python project environment with `uv`, installed pandas, and verified the installation by printing its version.

**Note:** The `.venv` directory is kept locally and is not uploaded to GitHub.
### Week 7: Python Programming and Ward Analysis

**Objective:** Apply Python fundamentals to read ward data from a CSV file and classify wards as large or small.

**Tasks completed:**
- Created `wards.csv` containing ward names and population values.
- Created `analyse.py` to read and analyse the CSV data.
- Practised variables, data types, loops, conditions, lists, and functions.
- Executed the program using the `uv` project environment.
- Verified that the program successfully classified the sample wards.

**Files:**
- `wards.csv`
- `analyse.py`
- `screenshots/week7.png`

**Outcome:** Successfully built and executed a Python program that reads ward population data and classifies each ward using a population threshold.

**Note:** The current implementation uses sample ward data and a threshold of 10,000 people. The dataset and classification rule should match the official Week 7 learning pack before final submission.
### Week 8: Python, Files and Data Inspection

**Objective:** Practise reading CSV data and generating summary statistics for numeric columns using Python and pandas.

**Tasks completed:**
- Created `mydata.csv` containing practice data with two numeric columns: `depth` and `yield`.
- Created `inspect_data.py` to read the CSV dataset using pandas.
- Calculated summary statistics for both numeric columns, including count, mean, minimum, and maximum.
- Printed the summary results as Python dictionaries.
- Executed the program successfully using the existing `uv` project environment.

**Verification output:**

```text
WEEK 8: DATA INSPECTION
Dataset: mydata.csv

{'column': 'depth', 'count': 5, 'mean': 13.38, 'min': 8.7, 'max': 20.1}
{'column': 'yield', 'count': 5, 'mean': 142.0, 'min': 95.0, 'max': 210.0}
```

**Files:**
- `mydata.csv`
- `inspect_data.py`
- `screenshots/week8.png`

**Outcome:** Successfully read a CSV dataset, inspected two numeric columns, calculated summary statistics, and displayed the results using Python dictionaries.

**Note:** The dataset contains illustrative practice values and does not represent actual field measurements.
