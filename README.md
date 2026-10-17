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
