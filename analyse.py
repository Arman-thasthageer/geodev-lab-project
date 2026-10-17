import csv

THRESHOLD = 10000

def classify_ward(population):
    if population >= THRESHOLD:
        return "Large"
    return "Small"

with open("wards.csv", "r", encoding="utf-8-sig", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        ward = row["ward"]
        population = int(row["population"])
        category = classify_ward(population)
        print(f"{ward}: population={population}, category={category}")
