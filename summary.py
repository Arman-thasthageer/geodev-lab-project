import pandas as pd


def read_data(filename):
    """Read a CSV file and return its data."""
    return pd.read_csv(filename)


def summarise_column(data, column):
    """Calculate summary statistics for one numeric column."""
    values = pd.to_numeric(data[column], errors="coerce").dropna()

    return {
        "count": int(values.count()),
        "smallest": float(values.min()),
        "largest": float(values.max()),
        "average": float(values.mean())
    }


def summarise_all(data):
    """Print summary statistics for every numeric column."""
    numeric_columns = data.select_dtypes(include="number").columns

    for column in numeric_columns:
        summary = summarise_column(data, column)

        print(
            f"{column}: "
            f"count={summary['count']}, "
            f"smallest={summary['smallest']}, "
            f"largest={summary['largest']}, "
            f"average={summary['average']:.2f}"
        )


# Run the analysis
filename = "mydata.csv"
data = read_data(filename)

print("WEEK 9: DATA SUMMARY")
print("Dataset:", filename)
summarise_all(data)
